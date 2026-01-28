import { Link } from 'react-router-dom';
import { Target, Users, Award, Heart, ArrowRight } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Layout } from '../components/Layout';

const values = [
  {
    icon: Target,
    title: 'Kvalitet først',
    description: 'Vi velger kun materialer og leverandører som møter våre strenge krav til holdbarhet og finish.'
  },
  {
    icon: Users,
    title: 'Kundefokus',
    description: 'Din suksess er vår suksess. Vi går den ekstra milen for å levere profilklær du blir stolt av.'
  },
  {
    icon: Award,
    title: 'Ekspertise',
    description: 'Over 10 års erfaring med trykk og brodyr. Vi vet hva som fungerer og gir deg ærlige råd.'
  },
  {
    icon: Heart,
    title: 'Bærekraft',
    description: 'Vi tilbyr økologiske alternativer og jobber kontinuerlig med å redusere vårt miljøavtrykk.'
  }
];

const milestones = [
  { year: '2014', event: 'Firmaprint grunnlagt i Oslo' },
  { year: '2016', event: 'Utvidet produksjonskapasitet med brodyrmaskin' },
  { year: '2019', event: 'Lanserte online designverktøy' },
  { year: '2021', event: 'Passerte 500 bedriftskunder' },
  { year: '2023', event: 'Sertifisert økologisk produksjon' },
  { year: '2024', event: 'Ny plattform og utvidet sortiment' }
];

export const AboutPage = () => {
  return (
    <Layout>
      {/* Hero */}
      <section className="bg-gradient-to-br from-slate-50 to-slate-100 py-16 md:py-24">
        <div className="max-w-4xl mx-auto px-4 md:px-8 text-center">
          <h1 className="font-manrope text-3xl md:text-5xl font-bold text-slate-900" data-testid="about-title">
            Om Firmaprint
          </h1>
          <p className="mt-6 text-lg text-slate-600 max-w-2xl mx-auto">
            Vi er Norges ledende leverandør av profilklær med logo. Med over 10 års erfaring hjelper vi bedrifter med å skape et sterkt visuelt uttrykk.
          </p>
        </div>
      </section>

      {/* Story */}
      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4 md:px-8">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 mb-6">
                Vår historie
              </h2>
              <div className="space-y-4 text-slate-600">
                <p>
                  Firmaprint ble startet i 2014 med en enkel visjon: gjøre det enkelt for norske bedrifter å få høykvalitets profilklær med logo.
                </p>
                <p>
                  Vi så at markedet manglet en leverandør som kombinerte profesjonell kvalitet med enkel bestilling og rask levering. Det ønsket vi å endre.
                </p>
                <p>
                  I dag betjener vi over 500 bedrifter årlig – fra små startups til store konsern. Uansett størrelse på bestillingen får du samme høye kvalitet og personlige service.
                </p>
              </div>
            </div>
            <div className="relative">
              <img
                src="https://images.unsplash.com/photo-1657470036063-c7e49da31393?w=600"
                alt="Broderingmaskin i arbeid"
                className="rounded-2xl shadow-lg"
              />
              <div className="absolute -bottom-6 -right-6 bg-blue-600 text-white p-4 rounded-xl shadow-lg">
                <p className="text-3xl font-bold">10+</p>
                <p className="text-sm text-blue-100">års erfaring</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Values */}
      <section className="py-16 bg-slate-50">
        <div className="max-w-6xl mx-auto px-4 md:px-8">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 text-center mb-12">
            Våre verdier
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {values.map((value, i) => (
              <Card key={i} className="p-6">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                  <value.icon className="w-6 h-6 text-blue-600" />
                </div>
                <h3 className="font-semibold text-slate-900 mb-2">{value.title}</h3>
                <p className="text-sm text-slate-600">{value.description}</p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Timeline */}
      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 md:px-8">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 text-center mb-12">
            Vår reise
          </h2>
          <div className="space-y-6">
            {milestones.map((milestone, i) => (
              <div key={i} className="flex items-center gap-6">
                <div className="w-20 text-right">
                  <span className="font-manrope font-bold text-blue-600">{milestone.year}</span>
                </div>
                <div className="w-3 h-3 bg-blue-600 rounded-full flex-shrink-0" />
                <p className="text-slate-700">{milestone.event}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="py-16 bg-slate-900 text-white">
        <div className="max-w-6xl mx-auto px-4 md:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
            <div>
              <p className="text-4xl font-bold text-blue-400">500+</p>
              <p className="text-sm text-slate-400 mt-1">Bedriftskunder</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-blue-400">50K+</p>
              <p className="text-sm text-slate-400 mt-1">Produserte plagg</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-blue-400">98%</p>
              <p className="text-sm text-slate-400 mt-1">Fornøyde kunder</p>
            </div>
            <div>
              <p className="text-4xl font-bold text-blue-400">5-10</p>
              <p className="text-sm text-slate-400 mt-1">Virkedager levering</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 md:px-8 text-center">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900">
            Klar til å komme i gang?
          </h2>
          <p className="mt-4 text-slate-600">
            Vi ser frem til å hjelpe din bedrift med profilklær av høy kvalitet.
          </p>
          <div className="mt-8 flex flex-col sm:flex-row gap-4 justify-center">
            <Button size="lg" asChild>
              <Link to="/produkter">Se produkter <ArrowRight className="ml-2 w-4 h-4" /></Link>
            </Button>
            <Button size="lg" variant="outline" asChild>
              <Link to="/kontakt">Kontakt oss</Link>
            </Button>
          </div>
        </div>
      </section>
    </Layout>
  );
};

// Privacy Policy Page
export const PrivacyPage = () => {
  return (
    <Layout>
      <div className="max-w-4xl mx-auto px-4 md:px-8 py-16">
        <h1 className="font-manrope text-3xl font-bold text-slate-900 mb-8" data-testid="privacy-title">
          Personvernerklæring
        </h1>
        
        <div className="prose prose-slate max-w-none">
          <p className="text-slate-600 mb-6">
            Sist oppdatert: Januar 2024
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">1. Innledning</h2>
          <p className="text-slate-600 mb-4">
            Firmaprint AS ("vi", "oss", "vår") respekterer ditt personvern og forplikter seg til å beskytte dine personopplysninger. Denne personvernerklæringen forklarer hvordan vi samler inn, bruker og beskytter informasjonen din.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">2. Informasjon vi samler inn</h2>
          <p className="text-slate-600 mb-4">Vi samler inn følgende informasjon:</p>
          <ul className="list-disc pl-6 text-slate-600 mb-4 space-y-2">
            <li>Kontaktinformasjon (navn, e-post, telefon, adresse)</li>
            <li>Betalingsinformasjon (behandles sikkert av vår betalingsleverandør)</li>
            <li>Bestillingshistorikk og kommunikasjon</li>
            <li>Opplastede logoer og designfiler</li>
          </ul>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">3. Hvordan vi bruker informasjonen</h2>
          <p className="text-slate-600 mb-4">Vi bruker informasjonen til å:</p>
          <ul className="list-disc pl-6 text-slate-600 mb-4 space-y-2">
            <li>Behandle og levere bestillinger</li>
            <li>Kommunisere om ordrestatus og kundeservice</li>
            <li>Forbedre våre produkter og tjenester</li>
            <li>Sende relevant markedsføring (med ditt samtykke)</li>
          </ul>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">4. Dine rettigheter</h2>
          <p className="text-slate-600 mb-4">
            Du har rett til innsyn, retting, sletting og dataportabilitet. Kontakt oss på personvern@firmaprint.no for spørsmål.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">5. Kontakt</h2>
          <p className="text-slate-600">
            Firmaprint AS<br />
            Storgata 1, 0155 Oslo<br />
            E-post: personvern@firmaprint.no
          </p>
        </div>
      </div>
    </Layout>
  );
};

// Terms Page
export const TermsPage = () => {
  return (
    <Layout>
      <div className="max-w-4xl mx-auto px-4 md:px-8 py-16">
        <h1 className="font-manrope text-3xl font-bold text-slate-900 mb-8" data-testid="terms-title">
          Kjøpsvilkår
        </h1>
        
        <div className="prose prose-slate max-w-none">
          <p className="text-slate-600 mb-6">
            Sist oppdatert: Januar 2024
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">1. Generelt</h2>
          <p className="text-slate-600 mb-4">
            Disse vilkårene gjelder for alle kjøp hos Firmaprint AS. Ved å bestille fra oss aksepterer du disse vilkårene.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">2. Priser</h2>
          <p className="text-slate-600 mb-4">
            Alle priser er oppgitt i NOK eksklusiv merverdiavgift (MVA). Prisen du ser ved checkout er totalprisen inkludert frakt.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">3. Betaling</h2>
          <p className="text-slate-600 mb-4">
            Vi aksepterer betaling med kort (Visa, Mastercard) og faktura for bedriftskunder. Faktura har 14 dagers betalingsfrist.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">4. Levering</h2>
          <p className="text-slate-600 mb-4">
            Standard leveringstid er 5-10 virkedager fra godkjent design. Frakt er gratis for bestillinger over 2000 kr.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">5. Angrerett</h2>
          <p className="text-slate-600 mb-4">
            Plagg uten trykk/brodyr kan returneres innen 14 dager. Plagg med dekor er spesialtilpasset og kan ikke returneres med mindre de er defekte.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">6. Reklamasjon</h2>
          <p className="text-slate-600 mb-4">
            Ved feil på produktet eller avvik fra bestillingen, kontakt oss innen 14 dager etter mottak. Vi erstatter eller refunderer defekte produkter.
          </p>

          <h2 className="font-manrope text-xl font-semibold text-slate-900 mt-8 mb-4">7. Kontakt</h2>
          <p className="text-slate-600">
            Firmaprint AS<br />
            Storgata 1, 0155 Oslo<br />
            E-post: ordre@firmaprint.no<br />
            Telefon: +47 123 45 678
          </p>
        </div>
      </div>
    </Layout>
  );
};

export default AboutPage;
