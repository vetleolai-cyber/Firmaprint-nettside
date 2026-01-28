import { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import { Building2, Users, BadgePercent, FileText, Truck, HeadphonesIcon, Check, ArrowRight, Loader2 } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Checkbox } from '../components/ui/checkbox';
import { Layout } from '../components/Layout';
import { toast } from 'sonner';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

const discountTiers = [
  { quantity: '10-24', discount: '5%', color: 'bg-slate-100' },
  { quantity: '25-49', discount: '10%', color: 'bg-blue-50' },
  { quantity: '50-99', discount: '15%', color: 'bg-blue-100' },
  { quantity: '100+', discount: '20%', color: 'bg-blue-200' },
];

const benefits = [
  { icon: BadgePercent, title: 'Rabatterte priser', description: 'Opptil 20% rabatt ved større bestillinger' },
  { icon: FileText, title: 'Fakturabetaling', description: 'Betal fakturaen innen 14 dager' },
  { icon: Truck, title: 'Prioritert levering', description: 'Raskere produksjon og levering' },
  { icon: HeadphonesIcon, title: 'Dedikert kontakt', description: 'Egen kundekontakt for din bedrift' },
];

const productTypes = [
  'T-skjorter', 'Gensere/Hoodies', 'Jakker', 'Capser', 'Arbeidsklær', 'Tilbehør'
];

export const BusinessPage = () => {
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [selectedProducts, setSelectedProducts] = useState([]);
  const [formData, setFormData] = useState({
    company_name: '',
    contact_name: '',
    email: '',
    phone: '',
    estimated_quantity: '',
    message: ''
  });

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleProductToggle = (product) => {
    setSelectedProducts(prev =>
      prev.includes(product) ? prev.filter(p => p !== product) : [...prev, product]
    );
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.company_name || !formData.contact_name || !formData.email || !formData.phone) {
      toast.error('Vennligst fyll ut alle obligatoriske felt');
      return;
    }

    setLoading(true);
    try {
      await axios.post(`${API}/quotes`, {
        ...formData,
        product_types: selectedProducts
      });
      setSubmitted(true);
      toast.success('Forespørselen ble sendt!');
    } catch (err) {
      toast.error('Kunne ikke sende forespørselen. Prøv igjen.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      {/* Hero */}
      <section className="bg-gradient-to-br from-slate-900 to-slate-800 text-white py-16 md:py-24">
        <div className="max-w-7xl mx-auto px-4 md:px-8">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 bg-blue-600/20 text-blue-300 px-3 py-1 rounded-full text-sm font-medium mb-6">
              <Building2 className="w-4 h-4" />
              For bedrifter og storkunder
            </div>
            <h1 className="font-manrope text-4xl md:text-5xl font-bold leading-tight" data-testid="business-title">
              Profilklær for hele teamet
            </h1>
            <p className="mt-6 text-xl text-slate-300">
              Få rabatterte priser, fakturabetaling og dedikert kundeservice. Vi hjelper bedrifter med alt fra enkeltbestillinger til store avtaler.
            </p>
          </div>
        </div>
      </section>

      {/* Discount tiers */}
      <section className="py-16 bg-white">
        <div className="max-w-7xl mx-auto px-4 md:px-8">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 text-center mb-4">
            Rabatterte priser ved volum
          </h2>
          <p className="text-center text-slate-600 mb-12">
            Jo mer du bestiller, jo mer sparer du
          </p>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 max-w-3xl mx-auto">
            {discountTiers.map((tier, i) => (
              <Card key={i} className={`p-6 text-center ${tier.color} border-0`}>
                <p className="text-3xl font-bold text-slate-900">{tier.discount}</p>
                <p className="text-sm text-slate-600 mt-1">{tier.quantity} stk</p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Benefits */}
      <section className="py-16 bg-slate-50">
        <div className="max-w-7xl mx-auto px-4 md:px-8">
          <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 text-center mb-12">
            Fordeler for bedriftskunder
          </h2>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {benefits.map((benefit, i) => (
              <Card key={i} className="p-6">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                  <benefit.icon className="w-6 h-6 text-blue-600" />
                </div>
                <h3 className="font-semibold text-slate-900 mb-2">{benefit.title}</h3>
                <p className="text-sm text-slate-600">{benefit.description}</p>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Quote form */}
      <section className="py-16 bg-white" id="tilbud">
        <div className="max-w-3xl mx-auto px-4 md:px-8">
          <div className="text-center mb-12">
            <h2 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900">
              Få et tilbud
            </h2>
            <p className="mt-2 text-slate-600">
              Fyll ut skjemaet under, så kontakter vi deg innen 24 timer
            </p>
          </div>

          {submitted ? (
            <Card className="p-8 text-center">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                <Check className="w-8 h-8 text-green-600" />
              </div>
              <h3 className="font-manrope text-xl font-bold text-slate-900">Takk for din henvendelse!</h3>
              <p className="mt-2 text-slate-600">Vi kontakter deg innen 24 timer med et tilbud.</p>
              <Button className="mt-6" asChild>
                <Link to="/produkter">Se produkter</Link>
              </Button>
            </Card>
          ) : (
            <Card className="p-6 md:p-8">
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid md:grid-cols-2 gap-4">
                  <div>
                    <Label htmlFor="company_name">Firmanavn *</Label>
                    <Input
                      id="company_name"
                      name="company_name"
                      value={formData.company_name}
                      onChange={handleChange}
                      required
                      data-testid="quote-company"
                    />
                  </div>
                  <div>
                    <Label htmlFor="contact_name">Kontaktperson *</Label>
                    <Input
                      id="contact_name"
                      name="contact_name"
                      value={formData.contact_name}
                      onChange={handleChange}
                      required
                      data-testid="quote-contact"
                    />
                  </div>
                  <div>
                    <Label htmlFor="email">E-post *</Label>
                    <Input
                      id="email"
                      name="email"
                      type="email"
                      value={formData.email}
                      onChange={handleChange}
                      required
                      data-testid="quote-email"
                    />
                  </div>
                  <div>
                    <Label htmlFor="phone">Telefon *</Label>
                    <Input
                      id="phone"
                      name="phone"
                      type="tel"
                      value={formData.phone}
                      onChange={handleChange}
                      required
                      data-testid="quote-phone"
                    />
                  </div>
                </div>

                <div>
                  <Label>Hvilke produkter er du interessert i?</Label>
                  <div className="flex flex-wrap gap-3 mt-2">
                    {productTypes.map((type) => (
                      <label key={type} className="flex items-center gap-2 cursor-pointer">
                        <Checkbox
                          checked={selectedProducts.includes(type)}
                          onCheckedChange={() => handleProductToggle(type)}
                        />
                        <span className="text-sm">{type}</span>
                      </label>
                    ))}
                  </div>
                </div>

                <div>
                  <Label htmlFor="estimated_quantity">Estimert antall</Label>
                  <Input
                    id="estimated_quantity"
                    name="estimated_quantity"
                    value={formData.estimated_quantity}
                    onChange={handleChange}
                    placeholder="F.eks. 50-100 stk"
                    data-testid="quote-quantity"
                  />
                </div>

                <div>
                  <Label htmlFor="message">Beskriv ditt behov</Label>
                  <textarea
                    id="message"
                    name="message"
                    value={formData.message}
                    onChange={handleChange}
                    rows={4}
                    className="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
                    placeholder="Fortell oss om prosjektet ditt, f.eks. type arrangement, leveringstidspunkt, ønskede produkter..."
                    data-testid="quote-message"
                  />
                </div>

                <Button type="submit" size="lg" className="w-full" disabled={loading} data-testid="quote-submit">
                  {loading ? (
                    <><Loader2 className="w-4 h-4 mr-2 animate-spin" /> Sender...</>
                  ) : (
                    <>Send forespørsel <ArrowRight className="w-4 h-4 ml-2" /></>
                  )}
                </Button>
              </form>
            </Card>
          )}
        </div>
      </section>
    </Layout>
  );
};

export default BusinessPage;
