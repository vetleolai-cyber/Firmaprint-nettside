import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import {
  ArrowRight,
  Zap,
  Truck,
  BadgeCheck,
  Star,
  ChevronRight,
} from "lucide-react";
import { Button } from "../components/ui/button";
import { Card } from "../components/ui/card";
import { Layout } from "../components/Layout";

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

const categories = [
  {
    id: "tshirts",
    name: "T-skjorter",
    icon: "👕",
    image:
      "https://images.unsplash.com/photo-1581655353564-df123a1eb820?w=400",
  },
  {
    id: "hoodies",
    name: "Gensere & Hoodies",
    icon: "🧥",
    image:
      "https://images.pexels.com/photos/7688469/pexels-photo-7688469.jpeg?w=400",
  },
  {
    id: "caps",
    name: "Capser",
    icon: "🧢",
    image:
      "https://images.pexels.com/photos/12025472/pexels-photo-12025472.jpeg?w=400",
  },
  {
    id: "jackets",
    name: "Jakker",
    icon: "🧥",
    image:
      "https://images.pexels.com/photos/3763234/pexels-photo-3763234.jpeg?w=400",
  },
  {
    id: "workwear",
    name: "Arbeidsklær",
    icon: "👷",
    image:
      "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=400",
  },
  {
    id: "accessories",
    name: "Tilbehør",
    icon: "👜",
    image:
      "https://images.unsplash.com/photo-1597633544424-4da83d50be55?w=400",
  },
];

const steps = [
  {
    number: "01",
    title: "Velg plagg",
    description: "Finn riktig plagg fra vår katalog med høykvalitets profilklær.",
  },
  {
    number: "02",
    title: "Last opp logo",
    description: "Last opp din logo og plasser den akkurat der du vil ha den.",
  },
  {
    number: "03",
    title: "Velg metode",
    description: "Velg mellom trykk eller brodering basert på dine behov.",
  },
  {
    number: "04",
    title: "Bestill",
    description: "Fullfør bestillingen og få varene levert raskt til deg.",
  },
];

const reviews = [
  {
    name: "Anders Bergström",
    company: "Bergström Bygg AS",
    rating: 5,
    text: "Fantastisk service og kvalitet! Vi fikk arbeidsklær til hele teamet med brodert logo. Veldig fornøyd!",
  },
  {
    name: "Mette Hansen",
    company: "Løpegruppen Oslo",
    rating: 5,
    text: "Bestilte t-skjorter til løpearrangementet vårt. Trykket var perfekt og leveringen var rask.",
  },
  {
    name: "Erik Nilsen",
    company: "Tech Startup",
    rating: 5,
    text: "Vi bruker Firmaprint til alle våre hoodies og caps. Enkel bestillingsprosess og topp kvalitet.",
  },
];

// Gjør products “always array” uansett hva API returnerer
function normalizeProductsPayload(payload) {
  // Vanlige varianter:
  // 1) [ ...products ]
  // 2) { items: [ ... ] }
  // 3) { products: [ ... ] }
  // 4) { data: [ ... ] }
  // 5) { data: { items: [...] } } osv
  if (Array.isArray(payload)) return payload;

  const candidates = [
    payload?.items,
    payload?.products,
    payload?.data,
    payload?.data?.items,
    payload?.data?.products,
  ];

  for (const c of candidates) {
    if (Array.isArray(c)) return c;
  }

  return [];
}

// Sikker slug fallback (så det ikke krasjer om slug mangler)
function getProductSlug(p) {
  return (
    p?.slug ||
    p?.handle ||
    p?.id ||
    (p?.name ? String(p.name).toLowerCase().replace(/\s+/g, "-") : "produkt")
  );
}

export const HomePage = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");

  const backendOk = useMemo(() => {
    return Boolean(process.env.REACT_APP_BACKEND_URL);
  }, []);

  useEffect(() => {
    let isMounted = true;

    const fetchProducts = async () => {
      setLoading(true);
      setLoadError("");

      // Hvis backend URL ikke er satt i Vercel, vil API bli "undefined/api" og feile.
      if (!backendOk) {
        if (!isMounted) return;
        setProducts([]);
        setLoadError(
          "REACT_APP_BACKEND_URL er ikke satt i Vercel. Legg den inn som Environment Variable."
        );
        setLoading(false);
        return;
      }

      try {
        const res = await axios.get(`${API}/products?featured=true&limit=4`, {
          timeout: 15000,
        });

        const list = normalizeProductsPayload(res.data);

        // Debug (du kan fjerne senere)
        console.log("Products response:", res.data);
        console.log("Normalized list length:", list.length);

        if (!isMounted) return;
        setProducts(list);
      } catch (err) {
        console.error("Failed to fetch products:", err);

        const msg =
          err?.response?.data?.message ||
          err?.message ||
          "Kunne ikke hente produkter.";

        if (!isMounted) return;
        setProducts([]);
        setLoadError(msg);
      } finally {
        if (!isMounted) return;
        setLoading(false);
      }
    };

    fetchProducts();

    return () => {
      isMounted = false;
    };
  }, [backendOk]);

  return (
    <Layout>
      {/* Hero Section */}
      <section
        className="relative overflow-hidden bg-gradient-to-br from-slate-50 to-slate-100"
        data-testid="hero-section"
      >
        <div className="max-w-7xl mx-auto px-4 md:px-8 py-16 md:py-24">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <div className="inline-flex items-center gap-2 bg-blue-50 text-blue-700 px-3 py-1 rounded-full text-sm font-medium mb-6">
                <Zap className="w-4 h-4" />
                Rask levering i hele Norge
              </div>

              <h1 className="font-manrope text-4xl md:text-5xl lg:text-6xl font-bold tracking-tight text-slate-900 leading-tight">
                Profilklær med logo —{" "}
                <span className="text-blue-600">trykk og brodering</span>
              </h1>

              <p className="mt-6 text-lg text-slate-600 leading-relaxed max-w-xl">
                Fra t-skjorter til arbeidsklær. Design selv med vår enkle logo-editor
                og få profesjonelle profilklær levert raskt til din bedrift.
              </p>

              <div className="mt-8 flex flex-col sm:flex-row gap-4">
                <Button
                  size="lg"
                  className="bg-slate-900 hover:bg-slate-800 h-12 px-8"
                  asChild
                  data-testid="hero-cta-products"
                >
                  <Link to="/produkter">
                    Se produkter <ArrowRight className="ml-2 w-4 h-4" />
                  </Link>
                </Button>

                <Button
                  size="lg"
                  variant="outline"
                  className="h-12 px-8"
                  asChild
                  data-testid="hero-cta-quote"
                >
                  <Link to="/kontakt">Få tilbud</Link>
                </Button>
              </div>

              <div className="mt-10 flex items-center gap-8 text-sm text-slate-600">
                <div className="flex items-center gap-2">
                  <BadgeCheck className="w-5 h-5 text-green-600" />
                  Gratis frakt over 2000kr
                </div>
                <div className="flex items-center gap-2">
                  <Truck className="w-5 h-5 text-blue-600" />
                  5-10 virkedager
                </div>
              </div>
            </div>

            <div className="relative hidden lg:block">
              <div className="relative aspect-square rounded-2xl overflow-hidden shadow-2xl">
                <img
                  src="https://images.pexels.com/photos/7688457/pexels-photo-7688457.jpeg"
                  alt="Team i profilklær"
                  className="w-full h-full object-cover"
                />
              </div>

              <div className="absolute -bottom-6 -left-6 bg-white rounded-xl shadow-lg p-4 flex items-center gap-3">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center">
                  <Star className="w-6 h-6 text-blue-600" />
                </div>
                <div>
                  <p className="font-semibold text-slate-900">500+ bedrifter</p>
                  <p className="text-sm text-slate-500">stoler på oss</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Categories */}
      <section className="py-16 md:py-24 bg-white" data-testid="categories-section">
        <div className="max-w-7xl mx-auto px-4 md:px-8">
          <div className="text-center mb-12">
            <h2 className="font-manrope text-3xl md:text-4xl font-bold text-slate-900">
              Våre kategorier
            </h2>
            <p className="mt-4 text-lg text-slate-600">
              Finn de perfekte plaggene for din bedrift
            </p>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            {categories.map((cat) => (
              <Link
                key={cat.id}
                to={`/kategori/${cat.id}`}
                className="group relative aspect-square rounded-xl overflow-hidden bg-slate-100"
                data-testid={`cat-${cat.id}`}
              >
                <img
                  src={cat.image}
                  alt={cat.name}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-900/80 to-transparent" />
                <div className="absolute bottom-4 left-4 right-4">
                  <p className="text-white font-semibold text-sm md:text-base">
                    {cat.name}
                  </p>
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="py-16 md:py-24 bg-slate-50" data-testid="how-it-works-section">
        <div className="max-w-7xl mx-auto px-4 md:px-8">
          <div className="text-center mb-12">
            <h2 className="font-manrope text-3xl md:text-4xl font-bold text-slate-900">
              Slik funker det
            </h2>
            <p className="mt-4 text-lg text-slate-600">
              Fire enkle steg til profilklær med din logo
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {steps.map((step, i) => (
              <div key={i} className="relative">
                <div className="text-5xl font-bold text-slate-200 mb-4">
                  {step.number}
                </div>
                <h3 className="font-semibold text-xl text-slate-900 mb-2">
                  {step.title}
                </h3>
                <p className="text-slate-600">{step.description}</p>
                {i < steps.length - 1 && (
                  <ChevronRight className="hidden lg:block absolute top-8 -right-4 w-8 h-8 text-slate-300" />
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Featured Products */}
      <section className="py-16 md:py-24 bg-white" data-testid="featured-products-section">
        <div className="max-w-7xl mx-auto px-4 md:px-8">
          <div className="flex items-center justify-between mb-12">
            <div>
              <h2 className="font-manrope text-3xl md:text-4xl font-bold text-slate-900">
                Bestselgere
              </h2>
              <p className="mt-2 text-lg text-slate-600">
                Våre mest populære produkter
              </p>
            </div>

            <Button variant="outline" asChild data-testid="view-all-products">
              <Link to="/produkter">
                Se alle <ArrowRight className="ml-2 w-4 h-4" />
              </Link>
            </Button>
          </div>

          {loading ? (
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
              {[1, 2, 3, 4].map((i) => (
                <div
                  key={i}
                  className="aspect-square bg-slate-100 rounded-xl animate-pulse"
                />
              ))}
            </div>
          ) : loadError ? (
            <div className="rounded-xl border border-red-200 bg-red-50 p-4 text-red-800">
              <p className="font-semibold">Kunne ikke hente produkter</p>
              <p className="text-sm mt-1">{loadError}</p>
              <p className="text-sm mt-2">
                Tips: Sjekk at <code>REACT_APP_BACKEND_URL</code> er satt i Vercel
                (Project → Settings → Environment Variables).
              </p>
            </div>
          ) : products.length === 0 ? (
            <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 text-slate-700">
              <p className="font-semibold">Ingen produkter å vise enda</p>
              <p className="text-sm mt-1">
                Når backend har produkter (featured=true), dukker de opp her.
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-2 lg:grid-cols-4 gap-6">
              {products.map((product) => {
                const slug = getProductSlug(product);

                return (
                  <Link
                    key={product?.id || slug}
                    to={`/produkt/${slug}`}
                    className="group"
                    data-testid={`product-${slug}`}
                  >
                    <Card className="overflow-hidden border-0 shadow-sm hover:shadow-md transition-shadow">
                      <div className="aspect-square bg-slate-100 relative overflow-hidden">
                        <img
                          src={
                            product?.variants?.[0]?.images?.[0] ||
                            product?.image ||
                            "https://via.placeholder.com/400"
                          }
                          alt={product?.name || "Produkt"}
                          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                        />
                      </div>
                      <div className="p-4">
                        <p className="text-xs text-slate-500 mb-1">
                          {product?.brand || " "}
                        </p>
                        <h3 className="font-semibold text-slate-900 group-hover:text-blue-600 transition-colors">
                          {product?.name || "Produkt"}
                        </h3>
                        <p className="mt-2 text-lg font-bold text-slate-900">
                          fra {product?.base_price ?? product?.price ?? "-"} kr
                        </p>
                      </div>
                    </Card>
                  </Link>
                );
              })}
            </div>
          )}
        </div>
      </section>

      {/* Reviews */}
      <section className="py-16 md:py-24 bg-slate-900" data-testid="reviews-section">
        <div className="max-w-7xl mx-auto px-4 md:px-8">
          <div className="text-center mb-12">
            <h2 className="font-manrope text-3xl md:text-4xl font-bold text-white">
              Hva kundene sier
            </h2>
            <p className="mt-4 text-lg text-slate-400">
              Over 500 bedrifter stoler på oss
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {reviews.map((review, i) => (
              <Card key={i} className="p-6 bg-slate-800 border-slate-700">
                <div className="flex gap-1 mb-4">
                  {[...Array(review.rating)].map((_, j) => (
                    <Star
                      key={j}
                      className="w-5 h-5 fill-yellow-400 text-yellow-400"
                    />
                  ))}
                </div>
                <p className="text-slate-300 mb-4">"{review.text}"</p>
                <div>
                  <p className="font-semibold text-white">{review.name}</p>
                  <p className="text-sm text-slate-500">{review.company}</p>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 md:py-24 bg-blue-600" data-testid="cta-section">
        <div className="max-w-7xl mx-auto px-4 md:px-8 text-center">
          <h2 className="font-manrope text-3xl md:text-4xl font-bold text-white">
            Klar til å komme i gang?
          </h2>
          <p className="mt-4 text-lg text-blue-100 max-w-2xl mx-auto">
            Få et uforpliktende tilbud på profilklær til din bedrift. Vi hjelper deg
            med alt fra design til levering.
          </p>

          <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
            <Button
              size="lg"
              className="bg-white text-blue-600 hover:bg-blue-50 h-12 px-8"
              asChild
              data-testid="cta-get-quote"
            >
              <Link to="/kontakt">Få tilbud</Link>
            </Button>

            <Button
              size="lg"
              variant="outline"
              className="border-white text-white hover:bg-blue-700 h-12 px-8"
              asChild
              data-testid="cta-call"
            >
              <a href="tel:+4712345678">Ring oss: +47 123 45 678</a>
            </Button>
          </div>
        </div>
      </section>
    </Layout>
  );
};

export default HomePage;
