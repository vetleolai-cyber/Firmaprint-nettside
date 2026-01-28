import { Link } from 'react-router-dom';
import { Check, X, ArrowRight, Sparkles, Shirt } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Layout } from '../components/Layout';

const comparisonData = [
  { feature: 'Holdbarhet', embroidery: 'Utmerket – tåler mange vask', print: 'God – avhenger av trykktype' },
  { feature: 'Detaljer', embroidery: 'Begrenset – best for enklere logoer', print: 'Utmerket – kan gjengi foto og gradienter' },
  { feature: 'Følelse', embroidery: 'Premium, tekstur', print: 'Glatt, ingen tekstur' },
  { feature: 'Best for', embroidery: 'Polo, jakker, caps, arbeidsklær', print: 'T-skjorter, hoodies, promomateriell' },
  { feature: 'Minsteantall', embroidery: 'Ofte 5-10 stk', print: 'Fra 1 stk' },
  { feature: 'Oppsettskostnad', embroidery: 'Høyere (digitalisering)', print: 'Lavere' },
  { feature: 'Flerfarget logo', embroidery: 'Dyrere per farge', print: 'Inkludert (digitaltrykk)' },
];

const recommendations = [
  {
    product: 'T-skjorter',
    recommendation: 'Trykk',
    reason: 'Fleksibelt, kostnadseffektivt for alle antall, kan trykke store motiver.',
    icon: '👕'
  },
  {
    product: 'Polo/Skjorter',
    recommendation: 'Brodering',
    reason: 'Premium følelse, holder seg pent over tid, profesjonelt utseende.',
    icon: '👔'
  },
  {
    product: 'Hoodies/Gensere',
    recommendation: 'Begge',
    reason: 'Trykk for store motiver, brodering for diskret brystlogo.',
    icon: '🧥'
  },
  {
    product: 'Caps',
    recommendation: 'Brodering',
    reason: 'Standard for caps, holder seg best på buet overflate.',
    icon: '🧢'
  },
  {
    product: 'Jakker',
    recommendation: 'Brodering',
    reason: 'Tåler vær og vind, premium utseende.',
    icon: '🧥'
  },
  {
    product: 'Arbeidsklær',
    recommendation: 'Brodering',
    reason: 'Svært holdbart, tåler industrivask og tøff bruk.',
    icon: '👷'
  },
];

export const PrintVsEmbroideryPage = () => {
  return (
    <Layout>
      {/* Hero */}
      <section className="bg-gradient-to-br from-slate-50 to-slate-100 py-16 md:py-24">
        <div className="max-w-4xl mx-auto px-4 md:px-8 text-center">
          <h1 className="font-manrope text-3xl md:text-5xl font-bold text-slate-900" data-testid="print-vs-embroidery-title">
            Brodering vs Trykk
          </h1>
          <p className="mt-6 text-lg text-slate-600 max-w-2xl mx-auto">
            Lurer du på hvilken dekorasjonsmetode som passer best for dine profilklær? Vi hjelper deg med å velge riktig.
          </p>
        </div>
      </section>

      {/* Comparison cards */}
      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4 md:px-8">
          <div className="grid md:grid-cols-2 gap-8">
            {/* Embroidery card */}
            <Card className="p-8 border-2 border-blue-200 relative overflow-hidden">
              <div className="absolute top-0 right-0 bg-blue-600 text-white text-xs px-3 py-1 rounded-bl-lg font-medium">
                Premium
              </div>
              <div className="flex items-center gap-4 mb-6">
                <div className="w-16 h-16 bg-blue-100 rounded-2xl flex items-center justify-center">
                  <Sparkles className="w-8 h-8 text-blue-600" />
                </div>
                <div>
                  <h2 className="font-manrope text-2xl font-bold text-slate-900">Brodering</h2>
                  <p className="text-slate-600">Brodert logo med tråd</p>
                </div>
              </div>
              
              <ul className="space-y-3">
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Ekstremt holdbar – varer i årevis</span>
                </li>
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Premium, profesjonelt utseende</span>
                </li>
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Tåler industrivask og tøff bruk</span>
                </li>
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Flott tekstur og 3D-effekt</span>
                </li>
                <li className="flex items-start gap-3">
                  <X className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-500">Begrenset detaljnivå</span>
                </li>
                <li className="flex items-start gap-3">
                  <X className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-500">Kan ikke gjengi foto/gradienter</span>
                </li>
              </ul>

              <p className="mt-6 text-sm text-slate-600 bg-blue-50 p-3 rounded-lg">
                <strong>Best for:</strong> Polo, jakker, caps, arbeidsklær, bedriftsprofilering
              </p>
            </Card>

            {/* Print card */}
            <Card className="p-8 border-2 border-slate-200">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-16 h-16 bg-slate-100 rounded-2xl flex items-center justify-center">
                  <Shirt className="w-8 h-8 text-slate-600" />
                </div>
                <div>
                  <h2 className="font-manrope text-2xl font-bold text-slate-900">Trykk</h2>
                  <p className="text-slate-600">Digitalt eller serigrafisk trykk</p>
                </div>
              </div>
              
              <ul className="space-y-3">
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Ubegrenset antall farger</span>
                </li>
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Kan gjengi foto og gradienter</span>
                </li>
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Lavere pris per enhet</span>
                </li>
                <li className="flex items-start gap-3">
                  <Check className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-700">Store motiver mulig (f.eks. hele ryggen)</span>
                </li>
                <li className="flex items-start gap-3">
                  <X className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-500">Mindre holdbart enn brodering</span>
                </li>
                <li className="flex items-start gap-3">
                  <X className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
                  <span className="text-slate-500">Kan falme ved mye vask</span>
                </li>
              </ul>

              <p className="mt-6 text-sm text-slate-600 bg-slate-50 p-3 rounded-lg">
                <strong>Best for:</strong> T-skjorter, hoodies, store motiver, events, promotering
              </p>
            </Card>
          </div>
        </div>
      </section>

      {/* Comparison table */}
      <section className="py-16 bg-slate-50">
        <div className="max-w-4xl mx-auto px-4 md:px-8">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 text-center mb-12">
            Sammenligning
          </h2>

          <Card className="overflow-hidden">
            <table className="w-full text-sm">
              <thead className="bg-slate-100">
                <tr>
                  <th className="text-left p-4 font-semibold text-slate-900">Egenskap</th>
                  <th className="text-left p-4 font-semibold text-blue-600">Brodering</th>
                  <th className="text-left p-4 font-semibold text-slate-700">Trykk</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {comparisonData.map((row, i) => (
                  <tr key={i} className="hover:bg-slate-50">
                    <td className="p-4 font-medium text-slate-900">{row.feature}</td>
                    <td className="p-4 text-slate-600">{row.embroidery}</td>
                    <td className="p-4 text-slate-600">{row.print}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </Card>
        </div>
      </section>

      {/* Recommendations */}
      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4 md:px-8">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 text-center mb-4">
            Våre anbefalinger
          </h2>
          <p className="text-center text-slate-600 mb-12">
            Basert på produkttype og bruksområde
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {recommendations.map((rec, i) => (
              <Card key={i} className="p-6 hover:shadow-md transition-shadow">
                <div className="flex items-center gap-3 mb-4">
                  <span className="text-3xl">{rec.icon}</span>
                  <div>
                    <h3 className="font-semibold text-slate-900">{rec.product}</h3>
                    <span className={`text-sm font-medium ${
                      rec.recommendation === 'Brodering' ? 'text-blue-600' :
                      rec.recommendation === 'Trykk' ? 'text-slate-600' :
                      'text-purple-600'
                    }`}>
                      Anbefalt: {rec.recommendation}
                    </span>
                  </div>
                </div>
                <p className="text-sm text-slate-600">{rec.reason}</p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-slate-900">
        <div className="max-w-4xl mx-auto px-4 md:px-8 text-center">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-white">
            Usikker på hva som passer?
          </h2>
          <p className="mt-4 text-slate-400">
            Kontakt oss for gratis veiledning. Vi hjelper deg med å finne den beste løsningen.
          </p>
          <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" className="bg-white text-slate-900 hover:bg-slate-100" asChild>
              <Link to="/kontakt">Kontakt oss <ArrowRight className="ml-2 w-4 h-4" /></Link>
            </Button>
            <Button size="lg" variant="outline" className="border-slate-600 text-white hover:bg-slate-800" asChild>
              <Link to="/produkter">Se produkter</Link>
            </Button>
          </div>
        </div>
      </section>
    </Layout>
  );
};

export default PrintVsEmbroideryPage;
