import { useState } from 'react';
import { Link } from 'react-router-dom';
import { ChevronDown, ChevronUp, Search, HelpCircle, Truck, Image, Palette, Ruler, Shirt, RefreshCw, CreditCard, Clock } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Layout } from '../components/Layout';

const faqCategories = [
  {
    id: 'files',
    name: 'Filkrav',
    icon: Image,
    questions: [
      {
        q: 'Hvilke filformater aksepterer dere?',
        a: 'Vi aksepterer PNG, JPG, SVG og PDF. For best resultat anbefaler vi vektorfiler (SVG, AI, EPS, PDF) for brodyr, og høyoppløselige rasterbilder (PNG, JPG med minst 300 DPI) for trykk.'
      },
      {
        q: 'Hva er minimumskrav til oppløsning?',
        a: 'For trykk anbefaler vi minst 300 DPI i trykkstørrelsen. For brodyr trenger vi vektorgrafikk for best resultat. Bilder under 300 DPI kan se uskarpe eller pikselerte ut.'
      },
      {
        q: 'Kan dere hjelpe med logo-tilpasning?',
        a: 'Ja! Vi tilbyr profesjonell logokonvertering og -tilpasning. Kontakt oss for et tilbud på designtjenester.'
      }
    ]
  },
  {
    id: 'delivery',
    name: 'Levering',
    icon: Truck,
    questions: [
      {
        q: 'Hvor lang er leveringstiden?',
        a: 'Standard leveringstid er 5-10 virkedager fra godkjent design. Dette inkluderer produksjonstid og frakt. Hastelevering er tilgjengelig mot tillegg.'
      },
      {
        q: 'Hvor mye koster frakt?',
        a: 'Frakt er gratis for bestillinger over 2000 kr. Under dette beløpet koster standard frakt 99 kr. Vi sender med Posten/Bring.'
      },
      {
        q: 'Kan jeg spore bestillingen min?',
        a: 'Ja, du mottar et sporingsnummer på e-post når bestillingen er sendt. Du kan følge pakken via Posten/Bring sine nettsider.'
      }
    ]
  },
  {
    id: 'sizes',
    name: 'Størrelser',
    icon: Ruler,
    questions: [
      {
        q: 'Hvordan finner jeg riktig størrelse?',
        a: 'Hver produktside har en størrelsesguide. Vi anbefaler å måle et plagg du allerede har og sammenligne med guiden. Ved tvil, gå opp en størrelse.'
      },
      {
        q: 'Kan jeg bestille prøver først?',
        a: 'Ja, du kan bestille prøveeksemplarer uten logo for å sjekke passform og kvalitet. Kontakt oss for prøvebestilling.'
      },
      {
        q: 'Hva gjør jeg hvis størrelsen ikke passer?',
        a: 'Plagg uten trykk/brodyr kan byttes innen 14 dager. Plagg med dekor kan ikke byttes, så sjekk størrelsen nøye før bestilling.'
      }
    ]
  },
  {
    id: 'wash',
    name: 'Vask og stell',
    icon: RefreshCw,
    questions: [
      {
        q: 'Hvordan vasker jeg plagg med trykk?',
        a: 'Vask på 40°C, vreng plagget, unngå tørketrommel på høy varme. Ikke bruk blekemiddel. Følg alltid vaskelappen på plagget.'
      },
      {
        q: 'Er brodyrte plagg vaskbare?',
        a: 'Ja! Brodering er svært holdbart og tåler vanlig maskinvask. Vi anbefaler vask på 40-60°C avhengig av plaggtype.'
      },
      {
        q: 'Hvor lenge holder trykket?',
        a: 'Med riktig vask holder moderne trykk i mange år. Vrenging av plagget og unngåelse av høy varme forlenger levetiden betydelig.'
      }
    ]
  },
  {
    id: 'colors',
    name: 'Farger',
    icon: Palette,
    questions: [
      {
        q: 'Kan dere matche en spesifikk Pantone-farge?',
        a: 'Ja, vi kan matche Pantone-farger for både trykk og brodyr. Oppgi Pantone-koden i bestillingen, så tilpasser vi fargene.'
      },
      {
        q: 'Hvorfor kan farger se annerledes ut på skjerm vs. plagg?',
        a: 'Skjermer og fysiske materialer gjengir farger forskjellig. For nøyaktig fargegjengivelse, oppgi Pantone/CMYK-verdier. Vi sender gjerne fargeprøver.'
      },
      {
        q: 'Hvor mange farger kan jeg ha i logoen?',
        a: 'For trykk (digitaltrykk) er antall farger ubegrenset. For brodyr anbefaler vi maks 8-10 farger for best resultat og pris.'
      }
    ]
  },
  {
    id: 'payment',
    name: 'Betaling',
    icon: CreditCard,
    questions: [
      {
        q: 'Hvilke betalingsmetoder aksepterer dere?',
        a: 'Vi aksepterer Visa, Mastercard og faktura for bedriftskunder. Fakturabetaling har 14 dagers betalingsfrist.'
      },
      {
        q: 'Må jeg betale på forskudd?',
        a: 'For privatpersoner kreves full betaling ved bestilling. Bedriftskunder med avtale kan betale på faktura.'
      },
      {
        q: 'Kan jeg få faktura til bedriften min?',
        a: 'Ja, bedriftskunder kan velge fakturabetaling. Oppgi organisasjonsnummer og fakturaadresse ved checkout.'
      }
    ]
  }
];

export const FAQPage = () => {
  const [search, setSearch] = useState('');
  const [openItems, setOpenItems] = useState({});
  const [selectedCategory, setSelectedCategory] = useState(null);

  const toggleItem = (categoryId, index) => {
    const key = `${categoryId}-${index}`;
    setOpenItems(prev => ({ ...prev, [key]: !prev[key] }));
  };

  const filteredCategories = faqCategories.map(cat => ({
    ...cat,
    questions: cat.questions.filter(q =>
      q.q.toLowerCase().includes(search.toLowerCase()) ||
      q.a.toLowerCase().includes(search.toLowerCase())
    )
  })).filter(cat => cat.questions.length > 0);

  const displayCategories = selectedCategory
    ? filteredCategories.filter(c => c.id === selectedCategory)
    : filteredCategories;

  return (
    <Layout>
      <div className="bg-slate-50 min-h-screen">
        {/* Hero */}
        <section className="bg-white border-b py-16">
          <div className="max-w-4xl mx-auto px-4 md:px-8 text-center">
            <div className="w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center mx-auto mb-6">
              <HelpCircle className="w-8 h-8 text-blue-600" />
            </div>
            <h1 className="font-manrope text-3xl md:text-4xl font-bold text-slate-900" data-testid="faq-title">
              Ofte stilte spørsmål
            </h1>
            <p className="mt-4 text-lg text-slate-600">
              Finn svar på vanlige spørsmål om produkter, levering og mer
            </p>

            {/* Search */}
            <div className="mt-8 max-w-xl mx-auto relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
              <Input
                type="text"
                placeholder="Søk i FAQ..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="pl-12 h-12"
                data-testid="faq-search"
              />
            </div>
          </div>
        </section>

        {/* Category filters */}
        <div className="max-w-4xl mx-auto px-4 md:px-8 py-6">
          <div className="flex flex-wrap gap-2 justify-center">
            <Button
              variant={selectedCategory === null ? 'default' : 'outline'}
              size="sm"
              onClick={() => setSelectedCategory(null)}
            >
              Alle
            </Button>
            {faqCategories.map(cat => (
              <Button
                key={cat.id}
                variant={selectedCategory === cat.id ? 'default' : 'outline'}
                size="sm"
                onClick={() => setSelectedCategory(cat.id)}
              >
                <cat.icon className="w-4 h-4 mr-1" />
                {cat.name}
              </Button>
            ))}
          </div>
        </div>

        {/* FAQ Content */}
        <div className="max-w-4xl mx-auto px-4 md:px-8 pb-16">
          {displayCategories.length === 0 ? (
            <div className="text-center py-16">
              <p className="text-slate-500">Ingen resultater funnet</p>
              <Button variant="outline" className="mt-4" onClick={() => { setSearch(''); setSelectedCategory(null); }}>
                Fjern filtre
              </Button>
            </div>
          ) : (
            <div className="space-y-8">
              {displayCategories.map((category) => (
                <div key={category.id}>
                  <div className="flex items-center gap-3 mb-4">
                    <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                      <category.icon className="w-5 h-5 text-blue-600" />
                    </div>
                    <h2 className="font-semibold text-xl text-slate-900">{category.name}</h2>
                  </div>

                  <div className="space-y-3">
                    {category.questions.map((item, index) => {
                      const isOpen = openItems[`${category.id}-${index}`];
                      return (
                        <Card
                          key={index}
                          className={`overflow-hidden transition-colors ${isOpen ? 'border-blue-200' : ''}`}
                        >
                          <button
                            onClick={() => toggleItem(category.id, index)}
                            className="w-full flex items-center justify-between p-4 text-left hover:bg-slate-50 transition-colors"
                            data-testid={`faq-item-${category.id}-${index}`}
                          >
                            <span className="font-medium text-slate-900 pr-4">{item.q}</span>
                            {isOpen ? (
                              <ChevronUp className="w-5 h-5 text-slate-400 flex-shrink-0" />
                            ) : (
                              <ChevronDown className="w-5 h-5 text-slate-400 flex-shrink-0" />
                            )}
                          </button>
                          {isOpen && (
                            <div className="px-4 pb-4">
                              <p className="text-slate-600 leading-relaxed">{item.a}</p>
                            </div>
                          )}
                        </Card>
                      );
                    })}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* CTA */}
        <section className="bg-white border-t py-16">
          <div className="max-w-4xl mx-auto px-4 md:px-8 text-center">
            <h2 className="font-manrope text-xl md:text-2xl font-bold text-slate-900">
              Fant du ikke svaret?
            </h2>
            <p className="mt-2 text-slate-600">Kontakt oss direkte så hjelper vi deg</p>
            <Button className="mt-6" asChild>
              <Link to="/kontakt">Kontakt oss</Link>
            </Button>
          </div>
        </section>
      </div>
    </Layout>
  );
};

export default FAQPage;
