import { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { Upload, ZoomIn, ZoomOut, AlertTriangle, Minus, Plus, RotateCw } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { RadioGroup, RadioGroupItem } from '../components/ui/radio-group';
import { Slider } from '../components/ui/slider';
import { Layout } from '../components/Layout';
import { useCart } from '../context/AppContext';
import { toast } from 'sonner';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

export const ProductPage = () => {
  const { slug } = useParams();
  const navigate = useNavigate();
  const { addToCart } = useCart();
  const containerRef = useRef(null);
  const fileInputRef = useRef(null);

  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [selectedVariant, setSelectedVariant] = useState(0);
  const [selectedSize, setSelectedSize] = useState('');
  const [quantity, setQuantity] = useState(1);

  // Logo customizer state
  const [logoPreview, setLogoPreview] = useState(null);
  const [logoPosition, setLogoPosition] = useState({ x: 50, y: 50 });
  const [logoScale, setLogoScale] = useState(1);
  const [logoRotation, setLogoRotation] = useState(0);
  const [selectedArea, setSelectedArea] = useState('');
  const [printMethod, setPrintMethod] = useState('print');
  const [designPrice, setDesignPrice] = useState(0);
  const [warnings, setWarnings] = useState([]);
  const [logoSize, setLogoSize] = useState({ width: 0, height: 0 });

  // Dragging state
  const [isDragging, setIsDragging] = useState(false);
  const [dragOffset, setDragOffset] = useState({ x: 0, y: 0 });

  // Fetch product on mount
  useEffect(() => {
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
    fetchProduct();
  }, [slug]);

  // Calculate price when design changes
  useEffect(() => {
    const calculatePrice = async () => {
      if (!logoPreview || !product) return;

      try {
        const res = await axios.post(`${API}/pricing/calculate`, null, {
          params: {
            print_method: printMethod,
            print_area: selectedArea,
            quantity: quantity
          }
        });
        setDesignPrice(res.data.price_per_item);
      } catch (err) {
        console.error('Failed to calculate price:', err);
        // Fallback to fixed prices
        if (printMethod === 'embroidery') {
          setDesignPrice(89);
        } else {
          const largeAreas = ['full_back', 'back', 'center_chest'];
          setDesignPrice(largeAreas.includes(selectedArea) ? 79 : 59);
        }
      }
    };

    if (logoPreview && product) {
      calculatePrice();
    } else {
      setDesignPrice(0);
    }
  }, [logoPreview, quantity, printMethod, product, selectedArea]);

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
        setLogoPreview(event.target.result);
        setLogoSize({ width: img.width, height: img.height });

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

  const handleMouseDown = (e) => {
    if (!logoPreview) return;
    e.preventDefault();
    
    const container = containerRef.current;
    if (!container) return;
    
    const rect = container.getBoundingClientRect();
    const area = product.print_areas.find(a => a.name === selectedArea);
    if (!area) return;

    // Calculate area bounds in pixels
    const areaX = (area.x / 100) * rect.width;
    const areaY = (area.y / 100) * rect.height;
    const areaW = (area.width / 100) * rect.width;
    const areaH = (area.height / 100) * rect.height;

    // Current logo position in pixels
    const logoX = areaX + (logoPosition.x / 100) * areaW;
    const logoY = areaY + (logoPosition.y / 100) * areaH;

    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;

    // Check if click is on logo
    const logoDisplaySize = 80 * logoScale;
    if (Math.abs(mouseX - logoX) < logoDisplaySize/2 && Math.abs(mouseY - logoY) < logoDisplaySize/2) {
      setIsDragging(true);
      setDragOffset({ x: mouseX - logoX, y: mouseY - logoY });
    }
  };

  const handleMouseMove = (e) => {
    if (!isDragging || !logoPreview || !product) return;
    
    const container = containerRef.current;
    if (!container) return;

    const rect = container.getBoundingClientRect();
    const area = product.print_areas.find(a => a.name === selectedArea);
    if (!area) return;

    const areaX = (area.x / 100) * rect.width;
    const areaY = (area.y / 100) * rect.height;
    const areaW = (area.width / 100) * rect.width;
    const areaH = (area.height / 100) * rect.height;

    const mouseX = e.clientX - rect.left - dragOffset.x;
    const mouseY = e.clientY - rect.top - dragOffset.y;

    const newX = Math.max(0, Math.min(100, ((mouseX - areaX) / areaW) * 100));
    const newY = Math.max(0, Math.min(100, ((mouseY - areaY) / areaH) * 100));

    setLogoPosition({ x: newX, y: newY });
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  const handleAddToCart = async () => {
    if (!selectedSize) {
      toast.error('Vennligst velg en størrelse');
      return;
    }

    const area = product.print_areas.find(a => a.name === selectedArea);
    const designObj = logoPreview ? {
      logo_url: logoPreview,
      logo_preview: logoPreview,
      position_x: logoPosition.x,
      position_y: logoPosition.y,
      scale: logoScale,
      rotation: logoRotation,
      view: 'front',
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
  const currentArea = product.print_areas.find(a => a.name === selectedArea);

  return (
    <Layout>
      <div className="bg-white">
        <div className="max-w-7xl mx-auto px-4 md:px-8 py-8">
          <div className="grid lg:grid-cols-12 gap-8">
            {/* Left: Product Preview with Logo Overlay */}
            <div className="lg:col-span-7">
              <div className="sticky top-24">
                <div className="bg-slate-50 rounded-2xl p-4 md:p-8">
                  {/* Product Image Container */}
                  <div 
                    ref={containerRef}
                    className="relative w-full aspect-square bg-white rounded-xl overflow-hidden shadow-inner select-none"
                    onMouseDown={handleMouseDown}
                    onMouseMove={handleMouseMove}
                    onMouseUp={handleMouseUp}
                    onMouseLeave={handleMouseUp}
                    style={{ cursor: logoPreview ? (isDragging ? 'grabbing' : 'grab') : 'default' }}
                    data-testid="product-preview"
                  >
                    {/* Product Image */}
                    <img
                      src={variant?.images?.[0] || 'https://via.placeholder.com/500'}
                      alt={product.name}
                      className="w-full h-full object-contain"
                      draggable={false}
                      onError={(e) => {
                        // Fallback to placeholder if image fails to load
                        e.target.src = `https://placehold.co/500x500/f1f5f9/64748b?text=${encodeURIComponent(product.name)}`;
                      }}
                    />
                    
                    {/* Print Area Overlay */}
                    {currentArea && (
                      <div
                        className="absolute border-2 border-dashed border-blue-500 bg-blue-500/5 pointer-events-none"
                        style={{
                          left: `${currentArea.x}%`,
                          top: `${currentArea.y}%`,
                          width: `${currentArea.width}%`,
                          height: `${currentArea.height}%`,
                        }}
                      >
                        <span className="absolute -top-6 left-0 text-xs font-medium text-blue-600 bg-white px-2 py-0.5 rounded shadow-sm">
                          {currentArea.name_no}
                        </span>
                      </div>
                    )}

                    {/* Logo Overlay */}
                    {logoPreview && currentArea && (
                      <div
                        className="absolute pointer-events-none"
                        style={{
                          left: `${currentArea.x + (logoPosition.x / 100) * currentArea.width}%`,
                          top: `${currentArea.y + (logoPosition.y / 100) * currentArea.height}%`,
                          transform: `translate(-50%, -50%) scale(${logoScale}) rotate(${logoRotation}deg)`,
                        }}
                      >
                        <img
                          src={logoPreview}
                          alt="Logo"
                          className="max-w-[80px] max-h-[80px] object-contain drop-shadow-lg"
                          draggable={false}
                        />
                      </div>
                    )}
                  </div>

                  {/* Print Area Selector */}
                  {product.print_areas && product.print_areas.length > 1 && (
                    <div className="flex flex-wrap justify-center gap-2 mt-4">
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

                  {/* Logo Controls */}
                  {logoPreview && (
                    <Card className="mt-4 p-4">
                      <p className="text-sm text-slate-600 mb-3">
                        <strong>Tips:</strong> Dra logoen for å plassere den i trykkområdet
                      </p>
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                        <div>
                          <Label className="text-xs text-slate-500">Størrelse</Label>
                          <div className="flex items-center gap-1 mt-1">
                            <Button variant="outline" size="icon" className="h-8 w-8" onClick={() => setLogoScale(Math.max(0.3, logoScale - 0.1))}>
                              <ZoomOut className="w-4 h-4" />
                            </Button>
                            <span className="text-sm font-mono w-10 text-center">{Math.round(logoScale * 100)}%</span>
                            <Button variant="outline" size="icon" className="h-8 w-8" onClick={() => setLogoScale(Math.min(2, logoScale + 0.1))}>
                              <ZoomIn className="w-4 h-4" />
                            </Button>
                          </div>
                        </div>
                        <div>
                          <Label className="text-xs text-slate-500">Rotasjon</Label>
                          <div className="flex items-center gap-1 mt-1">
                            <Button variant="outline" size="icon" className="h-8 w-8" onClick={() => setLogoRotation(logoRotation - 15)}>
                              <RotateCw className="w-4 h-4 scale-x-[-1]" />
                            </Button>
                            <span className="text-sm font-mono w-10 text-center">{logoRotation}°</span>
                            <Button variant="outline" size="icon" className="h-8 w-8" onClick={() => setLogoRotation(logoRotation + 15)}>
                              <RotateCw className="w-4 h-4" />
                            </Button>
                          </div>
                        </div>
                        <div className="col-span-2 flex items-end gap-2">
                          <Button variant="outline" size="sm" onClick={() => { setLogoPosition({ x: 50, y: 50 }); setLogoScale(1); setLogoRotation(0); }}>
                            Nullstill
                          </Button>
                          <Button variant="outline" size="sm" className="text-red-600 hover:text-red-700" onClick={() => { setLogoPreview(null); setWarnings([]); }}>
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
                  <Label>Farge: <span className="font-semibold">{variant.color}</span></Label>
                  <div className="flex flex-wrap gap-2 mt-2">
                    {product.variants.map((v, i) => (
                      <button
                        key={i}
                        onClick={() => setSelectedVariant(i)}
                        className={`w-10 h-10 rounded-full border-2 transition-all ${selectedVariant === i ? 'border-blue-600 ring-2 ring-blue-200' : 'border-slate-200 hover:border-slate-300'}`}
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
                  {!logoPreview ? (
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
                      <img src={logoPreview} alt="Logo" className="w-16 h-16 object-contain bg-white rounded-lg border p-1" />
                      <div className="flex-1">
                        <p className="font-semibold text-slate-900">Logo lastet opp ✓</p>
                        <p className="text-sm text-slate-500">Dra logoen på bildet for å plassere</p>
                      </div>
                      <Button variant="outline" size="sm" onClick={() => fileInputRef.current?.click()}>
                        Bytt
                      </Button>
                    </div>
                  )}
                </Card>

                {/* Print method */}
                {logoPreview && product.print_methods.length > 0 && (
                  <div>
                    <Label>Trykkmetode</Label>
                    <RadioGroup value={printMethod} onValueChange={setPrintMethod} className="mt-2">
                      {product.print_methods.includes('print') && (
                        <div className="flex items-center space-x-2 p-3 border rounded-lg hover:bg-slate-50 cursor-pointer" onClick={() => setPrintMethod('print')}>
                          <RadioGroupItem value="print" id="print" />
                          <div>
                            <Label htmlFor="print" className="font-medium cursor-pointer">Trykk</Label>
                            <p className="text-xs text-slate-500">Best for fotorealistiske motiver og store trykk</p>
                          </div>
                        </div>
                      )}
                      {product.print_methods.includes('embroidery') && (
                        <div className="flex items-center space-x-2 p-3 border rounded-lg hover:bg-slate-50 cursor-pointer" onClick={() => setPrintMethod('embroidery')}>
                          <RadioGroupItem value="embroidery" id="embroidery" />
                          <div>
                            <Label htmlFor="embroidery" className="font-medium cursor-pointer">Brodering</Label>
                            <p className="text-xs text-slate-500">Premium og holdbart, perfekt for logoer</p>
                          </div>
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
                      <span className="text-slate-600">Plagg ({quantity} stk à {product.base_price} kr)</span>
                      <span>{(product.base_price * quantity).toFixed(2)} kr</span>
                    </div>
                    {logoPreview && (
                      <div className="flex justify-between text-sm">
                        <span className="text-slate-600">{printMethod === 'embroidery' ? 'Brodering' : 'Trykk'} ({quantity} stk)</span>
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
                <div className="text-sm text-slate-600 space-y-2 pt-4 border-t">
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
