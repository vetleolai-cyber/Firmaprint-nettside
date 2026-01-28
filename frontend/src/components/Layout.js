import { Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';
import { ShoppingBag, Menu, X, User, ChevronDown } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Sheet, SheetContent, SheetTrigger } from '../components/ui/sheet';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '../components/ui/dropdown-menu';
import { useAuth, useCart } from '../context/AppContext';

const categories = [
  { name: 'Capser', slug: 'caps' },
  { name: 'T-skjorter', slug: 'tshirts' },
  { name: 'Gensere & Hoodies', slug: 'hoodies' },
  { name: 'Jakker', slug: 'jackets' },
  { name: 'Arbeidsklær', slug: 'workwear' },
  { name: 'Tilbehør', slug: 'accessories' },
];

export const Header = () => {
  const [mobileOpen, setMobileOpen] = useState(false);
  const { user, logout } = useAuth();
  const { itemCount } = useCart();
  const navigate = useNavigate();

  return (
    <header className="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-xl border-b border-slate-200/50">
      <div className="max-w-7xl mx-auto px-4 md:px-8">
        <div className="flex h-16 items-center justify-between">
          {/* Logo */}
          <Link to="/" className="flex items-center gap-2" data-testid="logo-link">
            <span className="font-manrope font-bold text-xl tracking-tight text-slate-900">
              Firma<span className="text-blue-600">print</span>
            </span>
          </Link>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center gap-6">
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <button className="flex items-center gap-1 text-sm font-medium text-slate-700 hover:text-slate-900 transition-colors" data-testid="products-dropdown">
                  Produkter <ChevronDown className="w-4 h-4" />
                </button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="start" className="w-48">
                {categories.map((cat) => (
                  <DropdownMenuItem key={cat.slug} asChild>
                    <Link to={`/kategori/${cat.slug}`} className="w-full" data-testid={`nav-${cat.slug}`}>
                      {cat.name}
                    </Link>
                  </DropdownMenuItem>
                ))}
                <DropdownMenuItem asChild>
                  <Link to="/produkter" className="w-full font-medium" data-testid="nav-all-products">
                    Se alle produkter
                  </Link>
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>

            <Link to="/brodyr-vs-trykk" className="text-sm font-medium text-slate-700 hover:text-slate-900 transition-colors" data-testid="nav-brodyr">
              Brodering vs Trykk
            </Link>
            <Link to="/bedrift" className="text-sm font-medium text-slate-700 hover:text-slate-900 transition-colors" data-testid="nav-bedrift">
              Bedrift
            </Link>
            <Link to="/kontakt" className="text-sm font-medium text-slate-700 hover:text-slate-900 transition-colors" data-testid="nav-kontakt">
              Kontakt
            </Link>
          </nav>

          {/* Actions */}
          <div className="flex items-center gap-2">
            {user ? (
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" size="sm" className="hidden md:flex gap-2" data-testid="user-menu">
                    <User className="w-4 h-4" />
                    {user.name.split(' ')[0]}
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent align="end">
                  <DropdownMenuItem asChild>
                    <Link to="/mine-ordrer">Mine ordrer</Link>
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={logout}>
                    Logg ut
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            ) : (
              <Button variant="ghost" size="sm" className="hidden md:flex" onClick={() => navigate('/logg-inn')} data-testid="login-btn">
                Logg inn
              </Button>
            )}

            <Button variant="outline" size="sm" className="relative" onClick={() => navigate('/handlekurv')} data-testid="cart-btn">
              <ShoppingBag className="w-4 h-4" />
              {itemCount > 0 && (
                <span className="absolute -top-1 -right-1 w-5 h-5 bg-blue-600 text-white text-xs rounded-full flex items-center justify-center">
                  {itemCount}
                </span>
              )}
            </Button>

            <Button className="hidden md:flex bg-slate-900 hover:bg-slate-800" onClick={() => navigate('/kontakt')} data-testid="get-quote-btn">
              Få tilbud
            </Button>

            {/* Mobile Menu */}
            <Sheet open={mobileOpen} onOpenChange={setMobileOpen}>
              <SheetTrigger asChild className="md:hidden">
                <Button variant="ghost" size="icon" data-testid="mobile-menu-btn">
                  {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
                </Button>
              </SheetTrigger>
              <SheetContent side="right" className="w-80">
                <nav className="flex flex-col gap-4 mt-8">
                  <p className="text-xs font-semibold text-slate-500 uppercase tracking-wider">Kategorier</p>
                  {categories.map((cat) => (
                    <Link
                      key={cat.slug}
                      to={`/kategori/${cat.slug}`}
                      className="text-lg font-medium text-slate-900 hover:text-blue-600 transition-colors"
                      onClick={() => setMobileOpen(false)}
                    >
                      {cat.name}
                    </Link>
                  ))}
                  <hr className="my-2" />
                  <Link to="/produkter" className="text-lg font-medium text-slate-900" onClick={() => setMobileOpen(false)}>
                    Alle produkter
                  </Link>
                  <Link to="/brodyr-vs-trykk" className="text-lg font-medium text-slate-900" onClick={() => setMobileOpen(false)}>
                    Brodering vs Trykk
                  </Link>
                  <Link to="/bedrift" className="text-lg font-medium text-slate-900" onClick={() => setMobileOpen(false)}>
                    Bedrift
                  </Link>
                  <Link to="/kontakt" className="text-lg font-medium text-slate-900" onClick={() => setMobileOpen(false)}>
                    Kontakt
                  </Link>
                  <hr className="my-2" />
                  {user ? (
                    <>
                      <Link to="/mine-ordrer" className="text-lg font-medium text-slate-900" onClick={() => setMobileOpen(false)}>
                        Mine ordrer
                      </Link>
                      <button className="text-lg font-medium text-slate-500 text-left" onClick={() => { logout(); setMobileOpen(false); }}>
                        Logg ut
                      </button>
                    </>
                  ) : (
                    <Link to="/logg-inn" className="text-lg font-medium text-blue-600" onClick={() => setMobileOpen(false)}>
                      Logg inn
                    </Link>
                  )}
                </nav>
              </SheetContent>
            </Sheet>
          </div>
        </div>
      </div>
    </header>
  );
};

export const Footer = () => {
  return (
    <footer className="bg-slate-900 text-slate-300">
      <div className="max-w-7xl mx-auto px-4 md:px-8 py-16">
        <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
          <div className="col-span-2 md:col-span-1">
            <span className="font-manrope font-bold text-xl text-white">
              Firma<span className="text-blue-400">print</span>
            </span>
            <p className="mt-4 text-sm text-slate-400">
              Profilklær med logo – trykk og brodering, levert raskt til din bedrift.
            </p>
          </div>

          <div>
            <h4 className="font-semibold text-white mb-4">Produkter</h4>
            <ul className="space-y-2 text-sm">
              <li><Link to="/kategori/tshirts" className="hover:text-white transition-colors">T-skjorter</Link></li>
              <li><Link to="/kategori/hoodies" className="hover:text-white transition-colors">Gensere & Hoodies</Link></li>
              <li><Link to="/kategori/caps" className="hover:text-white transition-colors">Capser</Link></li>
              <li><Link to="/kategori/jackets" className="hover:text-white transition-colors">Jakker</Link></li>
              <li><Link to="/kategori/workwear" className="hover:text-white transition-colors">Arbeidsklær</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold text-white mb-4">Informasjon</h4>
            <ul className="space-y-2 text-sm">
              <li><Link to="/brodyr-vs-trykk" className="hover:text-white transition-colors">Brodering vs Trykk</Link></li>
              <li><Link to="/bedrift" className="hover:text-white transition-colors">Bedrift</Link></li>
              <li><Link to="/faq" className="hover:text-white transition-colors">FAQ</Link></li>
              <li><Link to="/om-oss" className="hover:text-white transition-colors">Om oss</Link></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold text-white mb-4">Kontakt</h4>
            <ul className="space-y-2 text-sm">
              <li>hei@firmaprint.no</li>
              <li>+47 123 45 678</li>
              <li className="pt-2">
                <Link to="/personvern" className="hover:text-white transition-colors">Personvern</Link>
              </li>
              <li>
                <Link to="/vilkar" className="hover:text-white transition-colors">Kjøpsvilkår</Link>
              </li>
            </ul>
          </div>
        </div>

        <div className="border-t border-slate-800 mt-12 pt-8 text-sm text-slate-500 text-center">
          © {new Date().getFullYear()} Firmaprint.no. Alle rettigheter forbeholdt.
        </div>
      </div>
    </footer>
  );
};

export const Layout = ({ children }) => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-1">{children}</main>
      <Footer />
    </div>
  );
};
