import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Mail, Phone, MapPin, Clock, Send, Loader2, Check } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Layout } from '../components/Layout';
import { useAuth } from '../context/AppContext';
import { toast } from 'sonner';
import axios from 'axios';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

export const ContactPage = () => {
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  });

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.name || !formData.email || !formData.subject || !formData.message) {
      toast.error('Vennligst fyll ut alle obligatoriske felt');
      return;
    }

    setLoading(true);
    try {
      await axios.post(`${API}/contact`, formData);
      setSubmitted(true);
      toast.success('Meldingen ble sendt!');
    } catch (err) {
      toast.error('Kunne ikke sende meldingen. Prøv igjen.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <div className="bg-slate-50 min-h-screen">
        <div className="max-w-6xl mx-auto px-4 md:px-8 py-16">
          <div className="text-center mb-12">
            <h1 className="font-manrope text-3xl md:text-4xl font-bold text-slate-900" data-testid="contact-title">
              Kontakt oss
            </h1>
            <p className="mt-4 text-lg text-slate-600 max-w-2xl mx-auto">
              Har du spørsmål om produkter, priser eller levering? Ta kontakt så hjelper vi deg.
            </p>
          </div>

          <div className="grid lg:grid-cols-3 gap-8">
            {/* Contact info */}
            <div className="space-y-6">
              <Card className="p-6">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Mail className="w-5 h-5 text-blue-600" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-slate-900">E-post</h3>
                    <a href="mailto:hei@firmaprint.no" className="text-blue-600 hover:underline">hei@firmaprint.no</a>
                    <p className="text-sm text-slate-500 mt-1">Svar innen 24 timer</p>
                  </div>
                </div>
              </Card>

              <Card className="p-6">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Phone className="w-5 h-5 text-blue-600" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-slate-900">Telefon</h3>
                    <a href="tel:+4712345678" className="text-blue-600 hover:underline">+47 123 45 678</a>
                    <p className="text-sm text-slate-500 mt-1">Man-fre 09:00-16:00</p>
                  </div>
                </div>
              </Card>

              <Card className="p-6">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <MapPin className="w-5 h-5 text-blue-600" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-slate-900">Adresse</h3>
                    <p className="text-slate-600">Storgata 1</p>
                    <p className="text-slate-600">0155 Oslo</p>
                  </div>
                </div>
              </Card>

              <Card className="p-6">
                <div className="flex items-start gap-4">
                  <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center flex-shrink-0">
                    <Clock className="w-5 h-5 text-blue-600" />
                  </div>
                  <div>
                    <h3 className="font-semibold text-slate-900">Åpningstider</h3>
                    <p className="text-slate-600">Mandag - Fredag: 09:00 - 16:00</p>
                    <p className="text-slate-600">Lørdag - Søndag: Stengt</p>
                  </div>
                </div>
              </Card>
            </div>

            {/* Contact form */}
            <div className="lg:col-span-2">
              {submitted ? (
                <Card className="p-8 text-center">
                  <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
                    <Check className="w-8 h-8 text-green-600" />
                  </div>
                  <h3 className="font-manrope text-xl font-bold text-slate-900">Takk for din melding!</h3>
                  <p className="mt-2 text-slate-600">Vi svarer deg innen 24 timer.</p>
                  <Button className="mt-6" onClick={() => setSubmitted(false)}>
                    Send ny melding
                  </Button>
                </Card>
              ) : (
                <Card className="p-6 md:p-8">
                  <form onSubmit={handleSubmit} className="space-y-6">
                    <div className="grid md:grid-cols-2 gap-4">
                      <div>
                        <Label htmlFor="name">Navn *</Label>
                        <Input
                          id="name"
                          name="name"
                          value={formData.name}
                          onChange={handleChange}
                          required
                          data-testid="contact-name"
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
                          data-testid="contact-email"
                        />
                      </div>
                      <div>
                        <Label htmlFor="phone">Telefon</Label>
                        <Input
                          id="phone"
                          name="phone"
                          type="tel"
                          value={formData.phone}
                          onChange={handleChange}
                          data-testid="contact-phone"
                        />
                      </div>
                      <div>
                        <Label htmlFor="subject">Emne *</Label>
                        <Input
                          id="subject"
                          name="subject"
                          value={formData.subject}
                          onChange={handleChange}
                          required
                          data-testid="contact-subject"
                        />
                      </div>
                    </div>

                    <div>
                      <Label htmlFor="message">Melding *</Label>
                      <textarea
                        id="message"
                        name="message"
                        value={formData.message}
                        onChange={handleChange}
                        rows={6}
                        className="flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
                        placeholder="Hvordan kan vi hjelpe deg?"
                        required
                        data-testid="contact-message"
                      />
                    </div>

                    <Button type="submit" size="lg" className="w-full" disabled={loading} data-testid="contact-submit">
                      {loading ? (
                        <><Loader2 className="w-4 h-4 mr-2 animate-spin" /> Sender...</>
                      ) : (
                        <>Send melding <Send className="w-4 h-4 ml-2" /></>
                      )}
                    </Button>
                  </form>
                </Card>
              )}
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

// Auth Pages
export const LoginPage = () => {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({ email: '', password: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await login(formData.email, formData.password);
      toast.success('Logget inn!');
      navigate('/');
    } catch (err) {
      toast.error('Ugyldig e-post eller passord');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <div className="min-h-[60vh] flex items-center justify-center px-4 py-16">
        <Card className="w-full max-w-md p-8">
          <h1 className="font-manrope text-2xl font-bold text-slate-900 text-center mb-6" data-testid="login-title">
            Logg inn
          </h1>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <Label htmlFor="email">E-post</Label>
              <Input
                id="email"
                type="email"
                value={formData.email}
                onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
                required
                data-testid="login-email"
              />
            </div>
            <div>
              <Label htmlFor="password">Passord</Label>
              <Input
                id="password"
                type="password"
                value={formData.password}
                onChange={(e) => setFormData(prev => ({ ...prev, password: e.target.value }))}
                required
                data-testid="login-password"
              />
            </div>
            <Button type="submit" className="w-full" disabled={loading} data-testid="login-submit">
              {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : 'Logg inn'}
            </Button>
          </form>
          <p className="mt-6 text-center text-sm text-slate-600">
            Har du ikke konto?{' '}
            <Link to="/registrer" className="text-blue-600 hover:underline">Registrer deg</Link>
          </p>
        </Card>
      </div>
    </Layout>
  );
};

export const RegisterPage = () => {
  const navigate = useNavigate();
  const { register } = useAuth();
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    name: '',
    company_name: '',
    org_number: '',
    is_business: false
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      await register(formData);
      toast.success('Konto opprettet!');
      navigate('/');
    } catch (err) {
      toast.error(err.response?.data?.detail || 'Kunne ikke opprette konto');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <div className="min-h-[60vh] flex items-center justify-center px-4 py-16">
        <Card className="w-full max-w-md p-8">
          <h1 className="font-manrope text-2xl font-bold text-slate-900 text-center mb-6" data-testid="register-title">
            Opprett konto
          </h1>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <Label htmlFor="name">Fullt navn *</Label>
              <Input
                id="name"
                value={formData.name}
                onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
                required
                data-testid="register-name"
              />
            </div>
            <div>
              <Label htmlFor="email">E-post *</Label>
              <Input
                id="email"
                type="email"
                value={formData.email}
                onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
                required
                data-testid="register-email"
              />
            </div>
            <div>
              <Label htmlFor="password">Passord *</Label>
              <Input
                id="password"
                type="password"
                value={formData.password}
                onChange={(e) => setFormData(prev => ({ ...prev, password: e.target.value }))}
                required
                minLength={6}
                data-testid="register-password"
              />
            </div>
            <div>
              <Label htmlFor="company">Firmanavn (valgfritt)</Label>
              <Input
                id="company"
                value={formData.company_name}
                onChange={(e) => setFormData(prev => ({ ...prev, company_name: e.target.value }))}
                data-testid="register-company"
              />
            </div>
            <Button type="submit" className="w-full" disabled={loading} data-testid="register-submit">
              {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : 'Opprett konto'}
            </Button>
          </form>
          <p className="mt-6 text-center text-sm text-slate-600">
            Har du allerede konto?{' '}
            <Link to="/logg-inn" className="text-blue-600 hover:underline">Logg inn</Link>
          </p>
        </Card>
      </div>
    </Layout>
  );
};

export default ContactPage;
