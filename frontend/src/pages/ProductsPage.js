import { useState, useEffect } from 'react';
import { Link, useParams, useSearchParams } from 'react-router-dom';
import axios from 'axios';
import { Search, SlidersHorizontal, X } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../components/ui/select';
import { Checkbox } from '../components/ui/checkbox';
import { Sheet, SheetContent, SheetTrigger } from '../components/ui/sheet';
import { Layout } from '../components/Layout';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

const categoryNames = {
  caps: 'Capser',
  tshirts: 'T-skjorter',
  hoodies: 'Gensere & Hoodies',
  jackets: 'Jakker',
  workwear: 'Arbeidsklær',
  accessories: 'Tilbehør',
};

const printMethods = [
  { id: 'print', label: 'Trykk' },
  { id: 'embroidery', label: 'Brodering' },
];

export const ProductsPage = () => {
  const { category } = useParams();
  const [searchParams, setSearchParams] = useSearchParams();
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState(searchParams.get('search') || '');
  const [selectedMethods, setSelectedMethods] = useState([]);
  const [priceRange, setPriceRange] = useState('');
  const [filtersOpen, setFiltersOpen] = useState(false);

  useEffect(() => {
    fetchProducts();
  }, [category, searchParams]);

  const fetchProducts = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (category) params.append('category', category);
      if (searchParams.get('search')) params.append('search', searchParams.get('search'));
      if (searchParams.get('method')) params.append('print_method', searchParams.get('method'));
      if (searchParams.get('min_price')) params.append('min_price', searchParams.get('min_price'));
      if (searchParams.get('max_price')) params.append('max_price', searchParams.get('max_price'));

      const res = await axios.get(`${API}/products?${params.toString()}`);
      setProducts(res.data);
    } catch (err) {
      console.error('Failed to fetch products:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = (e) => {
    e.preventDefault();
    if (search) {
      searchParams.set('search', search);
    } else {
      searchParams.delete('search');
    }
    setSearchParams(searchParams);
  };

  const handleMethodToggle = (method) => {
    const newMethods = selectedMethods.includes(method)
      ? selectedMethods.filter(m => m !== method)
      : [...selectedMethods, method];
    setSelectedMethods(newMethods);
    
    if (newMethods.length === 1) {
      searchParams.set('method', newMethods[0]);
    } else {
      searchParams.delete('method');
    }
    setSearchParams(searchParams);
  };

  const handlePriceChange = (value) => {
    setPriceRange(value);
    if (value === 'under200') {
      searchParams.set('max_price', '200');
      searchParams.delete('min_price');
    } else if (value === '200-500') {
      searchParams.set('min_price', '200');
      searchParams.set('max_price', '500');
    } else if (value === 'over500') {
      searchParams.set('min_price', '500');
      searchParams.delete('max_price');
    } else {
      searchParams.delete('min_price');
      searchParams.delete('max_price');
    }
    setSearchParams(searchParams);
  };

  const clearFilters = () => {
    setSearch('');
    setSelectedMethods([]);
    setPriceRange('');
    setSearchParams({});
  };

  const FilterContent = () => (
    <div className="space-y-6">
      <div>
        <h4 className="font-semibold text-slate-900 mb-3">Trykkmetode</h4>
        <div className="space-y-2">
          {printMethods.map(method => (
            <label key={method.id} className="flex items-center gap-2 cursor-pointer">
              <Checkbox
                checked={selectedMethods.includes(method.id)}
                onCheckedChange={() => handleMethodToggle(method.id)}
              />
              <span className="text-sm text-slate-700">{method.label}</span>
            </label>
          ))}
        </div>
      </div>

      <div>
        <h4 className="font-semibold text-slate-900 mb-3">Pris</h4>
        <Select value={priceRange} onValueChange={handlePriceChange}>
          <SelectTrigger data-testid="price-filter">
            <SelectValue placeholder="Alle priser" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="all">Alle priser</SelectItem>
            <SelectItem value="under200">Under 200 kr</SelectItem>
            <SelectItem value="200-500">200 - 500 kr</SelectItem>
            <SelectItem value="over500">Over 500 kr</SelectItem>
          </SelectContent>
        </Select>
      </div>

      {(search || selectedMethods.length > 0 || priceRange) && (
        <Button variant="outline" size="sm" onClick={clearFilters} className="w-full">
          <X className="w-4 h-4 mr-2" /> Fjern filtre
        </Button>
      )}
    </div>
  );

  return (
    <Layout>
      <div className="bg-slate-50 min-h-screen">
        <div className="max-w-7xl mx-auto px-4 md:px-8 py-8">
          {/* Header */}
          <div className="mb-8">
            <h1 className="font-manrope text-3xl md:text-4xl font-bold text-slate-900" data-testid="products-title">
              {category ? categoryNames[category] || 'Produkter' : 'Alle produkter'}
            </h1>
            <p className="mt-2 text-slate-600">
              {products.length} produkter{category ? ` i ${categoryNames[category]?.toLowerCase()}` : ''}
            </p>
          </div>

          {/* Search & Filter Bar */}
          <div className="flex flex-col md:flex-row gap-4 mb-8">
            <form onSubmit={handleSearch} className="flex-1 flex gap-2">
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                <Input
                  type="text"
                  placeholder="Søk etter produkter..."
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  className="pl-10"
                  data-testid="search-input"
                />
              </div>
              <Button type="submit" variant="secondary" data-testid="search-btn">
                Søk
              </Button>
            </form>

            {/* Mobile Filter Button */}
            <Sheet open={filtersOpen} onOpenChange={setFiltersOpen}>
              <SheetTrigger asChild className="md:hidden">
                <Button variant="outline" data-testid="mobile-filter-btn">
                  <SlidersHorizontal className="w-4 h-4 mr-2" /> Filtre
                </Button>
              </SheetTrigger>
              <SheetContent side="left" className="w-80">
                <h3 className="font-semibold text-lg mb-6">Filtre</h3>
                <FilterContent />
              </SheetContent>
            </Sheet>
          </div>

          <div className="flex gap-8">
            {/* Desktop Sidebar */}
            <aside className="hidden md:block w-64 flex-shrink-0">
              <Card className="p-6">
                <h3 className="font-semibold text-lg mb-6">Filtre</h3>
                <FilterContent />
              </Card>
            </aside>

            {/* Products Grid */}
            <div className="flex-1">
              {loading ? (
                <div className="grid grid-cols-2 lg:grid-cols-3 gap-6">
                  {[1,2,3,4,5,6].map(i => (
                    <div key={i} className="aspect-square bg-slate-200 rounded-xl animate-pulse" />
                  ))}
                </div>
              ) : products.length === 0 ? (
                <div className="text-center py-16">
                  <p className="text-slate-500 text-lg">Ingen produkter funnet</p>
                  <Button variant="outline" className="mt-4" onClick={clearFilters}>
                    Fjern filtre
                  </Button>
                </div>
              ) : (
                <div className="grid grid-cols-2 lg:grid-cols-3 gap-6">
                  {products.map((product) => (
                    <Link
                      key={product.id}
                      to={`/produkt/${product.slug}`}
                      className="group"
                      data-testid={`product-card-${product.slug}`}
                    >
                      <Card className="overflow-hidden border-0 shadow-sm hover:shadow-md transition-all">
                        <div className="aspect-square bg-slate-100 relative overflow-hidden">
                          <img
                            src={product.variants?.[0]?.images?.[0] || 'https://via.placeholder.com/400'}
                            alt={product.name}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                          />
                          {product.print_methods?.length > 0 && (
                            <div className="absolute top-3 left-3 flex gap-1">
                              {product.print_methods.includes('embroidery') && (
                                <span className="bg-blue-600 text-white text-xs px-2 py-1 rounded">Brodering</span>
                              )}
                              {product.print_methods.includes('print') && (
                                <span className="bg-slate-900 text-white text-xs px-2 py-1 rounded">Trykk</span>
                              )}
                            </div>
                          )}
                        </div>
                        <div className="p-4">
                          <p className="text-xs text-slate-500 mb-1">{product.brand}</p>
                          <h3 className="font-semibold text-slate-900 group-hover:text-blue-600 transition-colors line-clamp-1">
                            {product.name}
                          </h3>
                          <p className="mt-2 text-lg font-bold text-slate-900">fra {product.base_price} kr</p>
                          <p className="text-xs text-slate-500 mt-1">
                            {product.variants?.length || 0} farger · {product.delivery_days} virkedager
                          </p>
                        </div>
                      </Card>
                    </Link>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default ProductsPage;
