import { useState, useEffect, useRef, useCallback } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Upload, Move, RotateCw, ZoomIn, ZoomOut, Check, AlertTriangle, ChevronLeft, ChevronRight, Minus, Plus } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { RadioGroup, RadioGroupItem } from '../components/ui/radio-group';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui/select';
import { Slider } from '../components/ui/slider';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Layout } from '../components/Layout';
import { useCart } from '../context/AppContext';
import { toast } from 'sonner';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

export const ProductPage = () => {
  const { slug } = useParams();
  const navigate = useNavigate();
  const { addToCart } = useCart();
  const canvasRef = useRef(null);
  const fileInputRef = useRef(null);

  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedVariant, setSelectedVariant] = useState(0);
  const [selectedSize, setSelectedSize] = useState('');
  const [quantity, setQuantity] = useState(1);
  const [activeView, setActiveView] = useState('front');

  // Logo customizer state
  const [logo, setLogo] = useState(null);
  const [logoPreview, setLogoPreview] = useState(null);
  const [logoPosition, setLogoPosition] = useState({ x: 50, y: 50 });
  const [logoScale, setLogoScale] = useState(1);
  const [logoRotation, setLogoRotation] = useState(0);
  const [selectedArea, setSelectedArea] = useState('');
  const [printMethod, setPrintMethod] = useState('print');
  const [designPrice, setDesignPrice] = useState(0);
  const [warnings, setWarnings] = useState([]);

  // Dragging state
  const [isDragging, setIsDragging] = useState(false);
  const [dragStart, setDragStart] = useState({ x: 0, y: 0 });

  useEffect(() => {
    fetchProduct();
  }, [slug]);

  useEffect(() => {
    if (logo && product) {
      calculatePrice();
      drawCanvas();
    }
  }, [logo, logoPosition, logoScale, logoRotation, quantity, printMethod, selectedVariant, product]);

  const fetchProduct = async () => {
    try {
      const res = await axios.get(`${API}/products/${slug}`);
      setProduct(res.data);
      if (res.data.variants?.[0]?.sizes?.[0]) {
        setSelectedSize(res.data.variants[0].sizes[0]);
      }
      if (res.data.print_areas?.[0]) {
        setSelectedArea(res.data.print_areas[0].name);
      }
      if (res.data.print_methods?.[0]) {
        setPrintMethod(res.data.print_methods.includes('embroidery') ? 'embroidery' : 'print');
      }
    } catch (err) {
      console.error('Failed to fetch product:', err);
      toast.error('Kunne ikke laste produktet');
    } finally {
      setLoading(false);
    }
  };

  const calculatePrice = async () => {
    if (!logo) return;

    const area = product.print_areas.find(a => a.name === selectedArea);
    if (!area) return;

    const widthCm = area.max_width_cm * logoScale;
    const heightCm = area.max_height_cm * logoScale;

    try {
      const res = await axios.post(`${API}/pricing/calculate`, null, {
        params: {
          print_method: printMethod,
          width_cm: widthCm,
          height_cm: heightCm,
          quantity: quantity,
          complexity: 'normal'
        }
      });
      setDesignPrice(res.data.price_per_item);
    } catch (err) {
      console.error('Failed to calculate price:', err);
    }
  };

  const handleFileUpload = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const allowedTypes = ['image/png', 'image/jpeg', 'image/svg+xml'];
    if (!allowedTypes.includes(file.type)) {
      toast.error('Ugyldig filtype. Bruk PNG, JPG eller SVG.');
      return;
    }

    if (file.size > 10 * 1024 * 1024) {
      toast.error('Filen er for stor. Maks 10MB.');
      return;
    }

    const reader = new FileReader();
    reader.onload = (event) => {
      const img = new Image();
      img.onload = () => {
        setLogo(img);
        setLogoPreview(event.target.result);

        // Check resolution warnings
        const newWarnings = [];
        if (img.width < 300 || img.height < 300) {
          newWarnings.push('Logoen har lav oppløsning. For best resultat, bruk minst 300x300 piksler.');
        }
        setWarnings(newWarnings);
      };
      img.src = event.target.result;
    };
    reader.readAsDataURL(file);
  };

  const drawCanvas = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas || !product) return;

    const ctx = canvas.getContext('2d');
    const variant = product.variants[selectedVariant];

    // Load product image
    const productImg = new Image();
    productImg.crossOrigin = 'anonymous';
    productImg.onload = () => {
      canvas.width = 500;
      canvas.height = 500;

      // Draw product
      ctx.drawImage(productImg, 0, 0, 500, 500);

      // Draw print area overlay
      const area = product.print_areas.find(a => a.name === selectedArea);
      if (area) {
        const areaX = (area.x / 100) * 500;
        const areaY = (area.y / 100) * 500;
        const areaW = (area.width / 100) * 500;
        const areaH = (area.height / 100) * 500;

        ctx.strokeStyle = '#2563EB';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.strokeRect(areaX, areaY, areaW, areaH);
        ctx.setLineDash([]);

        // Draw logo if exists
        if (logo) {
          const logoX = areaX + (logoPosition.x / 100) * areaW;
          const logoY = areaY + (logoPosition.y / 100) * areaH;
          const logoW = logo.width * logoScale * 0.3;
          const logoH = logo.height * logoScale * 0.3;

          ctx.save();
          ctx.translate(logoX, logoY);
          ctx.rotate((logoRotation * Math.PI) / 180);
          ctx.drawImage(logo, -logoW / 2, -logoH / 2, logoW, logoH);
          ctx.restore();
        }
      }
    };
    productImg.src = variant?.images?.[0] || 'https://via.placeholder.com/500';
  }, [product, selectedVariant, selectedArea, logo, logoPosition, logoScale, logoRotation]);

  const handleCanvasMouseDown = (e) => {
    if (!logo) return;
    const rect = canvasRef.current.getBoundingClientRect();
    setIsDragging(true);
    setDragStart({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top
    });
  };

  const handleCanvasMouseMove = (e) => {
    if (!isDragging || !logo) return;
    const rect = canvasRef.current.getBoundingClientRect();
    const area = product.print_areas.find(a => a.name === selectedArea);
    if (!area) return;

    const areaX = (area.x / 100) * 500;
    const areaY = (area.y / 100) * 500;
    const areaW = (area.width / 100) * 500;
    const areaH = (area.height / 100) * 500;

    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    const newX = Math.max(0, Math.min(100, ((mouseX - areaX) / areaW) * 100));
    const newY = Math.max(0, Math.min(100, ((mouseY - areaY) / areaH) * 100));

    setLogoPosition({ x: newX, y: newY });
  };

  const handleCanvasMouseUp = () => {
    setIsDragging(false);
  };

  const handleAddToCart = async () => {
    if (!selectedSize) {
      toast.error('Vennligst velg en størrelse');
      return;
    }

    const area = product.print_areas.find(a => a.name === selectedArea);
    const designObj = logo ? {
      logo_url: logoPreview,
      logo_preview: logoPreview,
      position_x: logoPosition.x,
      position_y: logoPosition.y,
      scale: logoScale,
      rotation: logoRotation,
      view: activeView,
      print_area: selectedArea,
      print_method: printMethod,
      width_cm: area ? area.max_width_cm * logoScale : 10,
      height_cm: area ? area.max_height_cm * logoScale : 10,
      colors: [],
      complexity: 'normal',
      warnings: warnings
    } : null;

    try {
      await addToCart({
        product_id: product.id,
        variant_color: product.variants[selectedVariant].color,
        size: selectedSize,
        quantity: quantity,
        design: designObj
      });
      toast.success('Lagt til i handlekurven!');
    } catch (err) {
      toast.error('Kunne ikke legge til i handlekurven');
    }
  };

  if (loading) {
    return (
      <Layout>
        <div className="max-w-7xl mx-auto px-4 md:px-8 py-8">
          <div className="grid lg:grid-cols-2 gap-8">
            <div className="aspect-square bg-slate-100 rounded-xl animate-pulse" />
            <div className="space-y-4">
              <div className="h-8 bg-slate-100 rounded w-3/4 animate-pulse" />
              <div className="h-4 bg-slate-100 rounded w-1/2 animate-pulse" />
              <div className="h-32 bg-slate-100 rounded animate-pulse" />
            </div>
          </div>
        </div>
      </Layout>
    );
  }

  if (!product) {
    return (
      <Layout>
        <div className="max-w-7xl mx-auto px-4 md:px-8 py-16 text-center">
          <h1 className="text-2xl font-bold text-slate-900">Produkt ikke funnet</h1>
          <Button className="mt-4" onClick={() => navigate('/produkter')}>
            Tilbake til produkter
          </Button>
        </div>
      </Layout>
    );
  }

  const variant = product.variants[selectedVariant];
  const totalPrice = (product.base_price + designPrice) * quantity;

  return (
    <Layout>
      <div className="bg-white">
        <div className="max-w-7xl mx-auto px-4 md:px-8 py-8">
          <div className="grid lg:grid-cols-12 gap-8">
            {/* Left: Canvas/Preview */}
            <div className="lg:col-span-7">
              <div className="sticky top-24">
                <div className="bg-slate-50 rounded-2xl p-4 md:p-8">
                  <canvas
                    ref={canvasRef}
                    width={500}
                    height={500}
                    className="w-full aspect-square rounded-xl cursor-move bg-white shadow-inner"
                    onMouseDown={handleCanvasMouseDown}
                    onMouseMove={handleCanvasMouseMove}
                    onMouseUp={handleCanvasMouseUp}
                    onMouseLeave={handleCanvasMouseUp}
                    data-testid="product-canvas"
                  />

                  {/* View selector */}
                  {product.print_areas && product.print_areas.length > 1 && (
                    <div className="flex justify-center gap-2 mt-4">
                      {product.print_areas.map((area) => (
                        <Button
                          key={area.name}
                          variant={selectedArea === area.name ? 'default' : 'outline'}
                          size="sm"
                          onClick={() => setSelectedArea(area.name)}
                          data-testid={`area-${area.name}`}
                        >
                          {area.name_no}
                        </Button>
                      ))}
                    </div>
                  )}

                  {/* Logo controls */}
                  {logo && (
                    <Card className="mt-4 p-4">
                      <div className="grid grid-cols-3 gap-4">
                        <div>
                          <Label className="text-xs text-slate-500">Skala</Label>
                          <div className="flex items-center gap-2 mt-1">
                            <Button variant="outline" size="icon" className="h-8 w-8" onClick={() => setLogoScale(Math.max(0.2, logoScale - 0.1))}>
                              <ZoomOut className="w-4 h-4" />
                            </Button>
                            <span className="text-sm font-mono w-12 text-center">{Math.round(logoScale * 100)}%</span>
                            <Button variant="outline" size="icon" className="h-8 w-8" onClick={() => setLogoScale(Math.min(2, logoScale + 0.1))}>
                              <ZoomIn className="w-4 h-4" />
                            </Button>
                          </div>
                        </div>
                        <div>
                          <Label className="text-xs text-slate-500">Rotasjon</Label>
                          <div className="flex items-center gap-2 mt-1">
                            <Slider
                              value={[logoRotation]}
                              min={-180}
                              max={180}
                              step={5}
                              onValueChange={([val]) => setLogoRotation(val)}
                              className="w-full"
                            />
                          </div>
                          <span className="text-xs text-slate-500">{logoRotation}°</span>
                        </div>
                        <div className="flex items-end">
                          <Button variant="outline" size="sm" onClick={() => { setLogo(null); setLogoPreview(null); setWarnings([]); }}>
                            Fjern logo
                          </Button>
                        </div>
                      </div>
                    </Card>
                  )}

                  {/* Warnings */}
                  {warnings.length > 0 && (
                    <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded-lg">
                      {warnings.map((warn, i) => (
                        <div key={i} className="flex items-start gap-2 text-sm text-yellow-800">
                          <AlertTriangle className="w-4 h-4 mt-0.5 flex-shrink-0" />
                          {warn}
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* Right: Product info & options */}
            <div className="lg:col-span-5">
              <div className="space-y-6">
                <div>
                  <p className="text-sm text-slate-500">{product.brand}</p>
                  <h1 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900" data-testid="product-name">
                    {product.name}
                  </h1>
                  <p className="mt-2 text-slate-600">{product.description}</p>
                </div>

                {/* Color selector */}
                <div>
                  <Label>Farge: {variant.color}</Label>
                  <div className="flex gap-2 mt-2">
                    {product.variants.map((v, i) => (
                      <button
                        key={i}
                        onClick={() => setSelectedVariant(i)}
                        className={`w-10 h-10 rounded-full border-2 transition-all ${selectedVariant === i ? 'border-blue-600 ring-2 ring-blue-200' : 'border-slate-200'}`}
                        style={{ backgroundColor: v.color_hex }}
                        title={v.color}
                        data-testid={`color-${v.color}`}
                      />
                    ))}
                  </div>
                </div>

                {/* Size selector */}
                <div>
                  <Label>Størrelse</Label>
                  <div className="flex flex-wrap gap-2 mt-2">
                    {variant.sizes.map((size) => (
                      <Button
                        key={size}
                        variant={selectedSize === size ? 'default' : 'outline'}
                        size="sm"
                        onClick={() => setSelectedSize(size)}
                        data-testid={`size-${size}`}
                      >
                        {size}
                      </Button>
                    ))}
                  </div>
                </div>

                {/* Logo upload */}
                <Card className="p-4 border-dashed border-2 border-slate-200 bg-slate-50">
                  <input
                    ref={fileInputRef}
                    type="file"
                    accept=".png,.jpg,.jpeg,.svg"
                    onChange={handleFileUpload}
                    className="hidden"
                    data-testid="logo-upload-input"
                  />
                  {!logo ? (
                    <button
                      onClick={() => fileInputRef.current?.click()}
                      className="w-full flex flex-col items-center gap-3 py-6 hover:bg-slate-100 rounded-lg transition-colors"
                      data-testid="upload-logo-btn"
                    >
                      <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                        <Upload className="w-6 h-6 text-blue-600" />
                      </div>
                      <div className="text-center">
                        <p className="font-semibold text-slate-900">Last opp logo</p>
                        <p className="text-sm text-slate-500">PNG, JPG eller SVG (maks 10MB)</p>
                      </div>
                    </button>
                  ) : (
                    <div className="flex items-center gap-4">
                      <img src={logoPreview} alt="Logo" className="w-16 h-16 object-contain bg-white rounded-lg border" />
                      <div className="flex-1">
                        <p className="font-semibold text-slate-900">Logo lastet opp</p>
                        <p className="text-sm text-slate-500">Dra logoen på bildet for å plassere</p>
                      </div>
                      <Button variant="outline" size="sm" onClick={() => fileInputRef.current?.click()}>
                        Bytt
                      </Button>
                    </div>
                  )}
                </Card>

                {/* Print method */}
                {logo && product.print_methods.length > 0 && (
                  <div>
                    <Label>Trykkmetode</Label>
                    <RadioGroup value={printMethod} onValueChange={setPrintMethod} className="mt-2">
                      {product.print_methods.includes('print') && (
                        <div className="flex items-center space-x-2">
                          <RadioGroupItem value="print" id="print" />
                          <Label htmlFor="print" className="font-normal cursor-pointer">
                            Trykk – Best for fotorealistiske motiver
                          </Label>
                        </div>
                      )}
                      {product.print_methods.includes('embroidery') && (
                        <div className="flex items-center space-x-2">
                          <RadioGroupItem value="embroidery" id="embroidery" />
                          <Label htmlFor="embroidery" className="font-normal cursor-pointer">
                            Brodyr – Premium og holdbart
                          </Label>
                        </div>
                      )}
                    </RadioGroup>
                  </div>
                )}

                {/* Quantity */}
                <div>
                  <Label>Antall</Label>
                  <div className="flex items-center gap-3 mt-2">
                    <Button
                      variant="outline"
                      size="icon"
                      onClick={() => setQuantity(Math.max(product.min_quantity, quantity - 1))}
                      disabled={quantity <= product.min_quantity}
                      data-testid="qty-decrease"
                    >
                      <Minus className="w-4 h-4" />
                    </Button>
                    <Input
                      type="number"
                      value={quantity}
                      onChange={(e) => setQuantity(Math.max(product.min_quantity, parseInt(e.target.value) || 1))}
                      className="w-20 text-center"
                      min={product.min_quantity}
                      data-testid="qty-input"
                    />
                    <Button variant="outline" size="icon" onClick={() => setQuantity(quantity + 1)} data-testid="qty-increase">
                      <Plus className="w-4 h-4" />
                    </Button>
                    {product.min_quantity > 1 && (
                      <span className="text-sm text-slate-500">Min. {product.min_quantity} stk</span>
                    )}
                  </div>
                </div>

                {/* Price summary */}
                <Card className="p-4 bg-slate-50">
                  <div className="space-y-2">
                    <div className="flex justify-between text-sm">
                      <span className="text-slate-600">Plagg ({quantity} stk)</span>
                      <span>{(product.base_price * quantity).toFixed(2)} kr</span>
                    </div>
                    {logo && (
                      <div className="flex justify-between text-sm">
                        <span className="text-slate-600">{printMethod === 'embroidery' ? 'Brodyr' : 'Trykk'} ({quantity} stk)</span>
                        <span>{(designPrice * quantity).toFixed(2)} kr</span>
                      </div>
                    )}
                    <hr />
                    <div className="flex justify-between font-bold text-lg">
                      <span>Totalt</span>
                      <span data-testid="total-price">{totalPrice.toFixed(2)} kr</span>
                    </div>
                    <p className="text-xs text-slate-500">eks. mva · Frakt beregnes ved checkout</p>
                  </div>
                </Card>

                {/* Add to cart */}
                <Button
                  size="lg"
                  className="w-full bg-slate-900 hover:bg-slate-800 h-12"
                  onClick={handleAddToCart}
                  data-testid="add-to-cart-btn"
                >
                  Legg i handlekurv
                </Button>

                {/* Product details */}
                <div className="text-sm text-slate-600 space-y-2">
                  <div className="flex justify-between">
                    <span>Leveringstid:</span>
                    <span className="font-medium">{product.delivery_days} virkedager</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Materiale:</span>
                    <span className="font-medium">{product.materials?.join(', ')}</span>
                  </div>
                  <div className="flex justify-between">
                    <span>Passform:</span>
                    <span className="font-medium">{product.fit}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ProductPage;
