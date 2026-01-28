import { useState, useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import axios from 'axios';
import { CreditCard, FileText, Truck, Check, Loader2, Smartphone } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { RadioGroup, RadioGroupItem } from '../components/ui/radio-group';
import { Layout } from '../components/Layout';
import { useCart, useAuth } from '../context/AppContext';
import { toast } from 'sonner';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

// Vipps logo SVG
const VippsLogo = () => (
  <svg viewBox="0 0 80 24" className="h-6 w-auto" fill="currentColor">
    <path d="M13.7 1.5l-6 14.4-5.9-14.4H0l7.5 17h2.5l7.5-17h-3.8zm9.8 0h-3.2v17h3.2v-17zm12.1 0h-6.3v17h3.2v-6.6h3.1c3.6 0 5.9-2.2 5.9-5.2s-2.3-5.2-5.9-5.2zm-.1 7.4h-3v-4.4h3c1.7 0 2.7.9 2.7 2.2s-1 2.2-2.7 2.2zm17.1-7.4h-6.3v17h3.2v-6.6h3.1c3.6 0 5.9-2.2 5.9-5.2s-2.3-5.2-5.9-5.2zm-.1 7.4h-3v-4.4h3c1.7 0 2.7.9 2.7 2.2s-1 2.2-2.7 2.2zm16.3-3.9c-1.7-.5-2.5-.9-2.5-1.7 0-.7.6-1.2 1.7-1.2 1.2 0 2.4.5 3.4 1.3l1.5-2.4c-1.3-1-2.9-1.6-4.8-1.6-3 0-5 1.7-5 4.1 0 2.5 2 3.5 4.2 4.1 1.7.5 2.4.9 2.4 1.7 0 .8-.7 1.3-1.9 1.3-1.4 0-2.9-.6-4-1.6l-1.6 2.4c1.4 1.2 3.4 1.9 5.4 1.9 3.2 0 5.2-1.7 5.2-4.2.1-2.5-1.9-3.5-4-4.1z" fill="#FF5B24"/>
  </svg>
);

export const CheckoutPage = () => {
  const navigate = useNavigate();
  const { cart, sessionId, clearCart } = useCart();
  const { user } = useAuth();
  const [loading, setLoading] = useState(false);
  const [paymentMethod, setPaymentMethod] = useState('vipps');
  
  const [formData, setFormData] = useState({
    name: user?.name || '',
    company: user?.company_name || '',
    street: '',
    city: '',
    postal_code: '',
    phone: '',
    email: user?.email || '',
    notes: ''
  });

  // Calculate shipping
  const subtotalWithDesign = (cart.subtotal || 0) + (cart.design_total || 0);
  const shipping = subtotalWithDesign >= 2000 ? 0 : 99;
  const total = subtotalWithDesign + shipping;

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!formData.name || !formData.street || !formData.city || !formData.postal_code || !formData.phone || !formData.email) {
      toast.error('Vennligst fyll ut alle obligatoriske felt');
      return;
    }

    setLoading(true);
    try {
      const res = await axios.post(`${API}/orders/create`, {
        cart_session_id: sessionId,
        shipping_address: {
          name: formData.name,
          company: formData.company || null,
          street: formData.street,
          city: formData.city,
          postal_code: formData.postal_code,
          country: 'Norge',
          phone: formData.phone,
          email: formData.email
        },
        payment_method: paymentMethod,
        notes: formData.notes || null
      });

      if ((paymentMethod === 'stripe' || paymentMethod === 'vipps') && res.data.checkout_url) {
        window.location.href = res.data.checkout_url;
      } else {
        // Invoice payment
        navigate(`/ordre/${res.data.order.order_number}?payment=invoice`);
      }
    } catch (err) {
      console.error('Checkout error:', err);
      toast.error('Kunne ikke fullføre bestillingen. Prøv igjen.');
    } finally {
      setLoading(false);
    }
  };

  if (!cart.items || cart.items.length === 0) {
    navigate('/handlekurv');
    return null;
  }

  return (
    <Layout>
      <div className="bg-slate-50 min-h-screen">
        <div className="max-w-5xl mx-auto px-4 md:px-8 py-8">
          <h1 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 mb-8" data-testid="checkout-title">
            Kasse
          </h1>

          <form onSubmit={handleSubmit}>
            <div className="grid lg:grid-cols-3 gap-8">
              {/* Left: Forms */}
              <div className="lg:col-span-2 space-y-6">
                {/* Shipping info */}
                <Card className="p-6">
                  <div className="flex items-center gap-3 mb-6">
                    <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                      <Truck className="w-5 h-5 text-blue-600" />
                    </div>
                    <h2 className="font-semibold text-lg">Leveringsadresse</h2>
                  </div>

                  <div className="grid md:grid-cols-2 gap-4">
                    <div className="md:col-span-2">
                      <Label htmlFor="name">Fullt navn *</Label>
                      <Input
                        id="name"
                        name="name"
                        value={formData.name}
                        onChange={handleChange}
                        required
                        data-testid="checkout-name"
                      />
                    </div>
                    <div className="md:col-span-2">
                      <Label htmlFor="company">Firmanavn (valgfritt)</Label>
                      <Input
                        id="company"
                        name="company"
                        value={formData.company}
                        onChange={handleChange}
                        data-testid="checkout-company"
                      />
                    </div>
                    <div className="md:col-span-2">
                      <Label htmlFor="street">Adresse *</Label>
                      <Input
                        id="street"
                        name="street"
                        value={formData.street}
                        onChange={handleChange}
                        required
                        data-testid="checkout-street"
                      />
                    </div>
                    <div>
                      <Label htmlFor="postal_code">Postnummer *</Label>
                      <Input
                        id="postal_code"
                        name="postal_code"
                        value={formData.postal_code}
                        onChange={handleChange}
                        required
                        data-testid="checkout-postal"
                      />
                    </div>
                    <div>
                      <Label htmlFor="city">By *</Label>
                      <Input
                        id="city"
                        name="city"
                        value={formData.city}
                        onChange={handleChange}
                        required
                        data-testid="checkout-city"
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
                        data-testid="checkout-phone"
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
                        data-testid="checkout-email"
                      />
                    </div>
                  </div>
                </Card>

                {/* Payment method */}
                <Card className="p-6">
                  <div className="flex items-center gap-3 mb-6">
                    <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
                      <CreditCard className="w-5 h-5 text-blue-600" />
                    </div>
                    <h2 className="font-semibold text-lg">Betalingsmetode</h2>
                  </div>

                  <RadioGroup value={paymentMethod} onValueChange={setPaymentMethod} className="space-y-3">
                    {/* Vipps - Primary */}
                    <div 
                      className={`flex items-center space-x-3 p-4 border-2 rounded-lg cursor-pointer transition-colors ${paymentMethod === 'vipps' ? 'border-orange-400 bg-orange-50' : 'border-slate-200 hover:border-orange-300'}`} 
                      onClick={() => setPaymentMethod('vipps')}
                    >
                      <RadioGroupItem value="vipps" id="vipps" />
                      <div className="flex-1">
                        <Label htmlFor="vipps" className="font-medium cursor-pointer flex items-center gap-2">
                          <Smartphone className="w-4 h-4" />
                          Vipps
                          <span className="text-xs bg-orange-100 text-orange-700 px-2 py-0.5 rounded-full">Anbefalt</span>
                        </Label>
                        <p className="text-sm text-slate-500">Rask og enkel betaling med Vipps-appen</p>
                      </div>
                      <div className="w-16 h-8 bg-[#FF5B24] rounded-lg flex items-center justify-center">
                        <span className="text-white font-bold text-sm">Vipps</span>
                      </div>
                    </div>

                    {/* Card payment */}
                    <div 
                      className={`flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition-colors ${paymentMethod === 'stripe' ? 'border-blue-400 bg-blue-50' : 'border-slate-200 hover:border-blue-300'}`} 
                      onClick={() => setPaymentMethod('stripe')}
                    >
                      <RadioGroupItem value="stripe" id="stripe" />
                      <div className="flex-1">
                        <Label htmlFor="stripe" className="font-medium cursor-pointer">Kortbetaling</Label>
                        <p className="text-sm text-slate-500">Betal sikkert med Visa, Mastercard eller andre kort</p>
                      </div>
                      <div className="flex gap-1">
                        <div className="w-8 h-5 bg-blue-600 rounded text-white text-xs flex items-center justify-center font-bold">VISA</div>
                        <div className="w-8 h-5 bg-orange-500 rounded text-white text-xs flex items-center justify-center font-bold">MC</div>
                      </div>
                    </div>

                    {/* Invoice */}
                    <div 
                      className={`flex items-center space-x-3 p-4 border rounded-lg cursor-pointer transition-colors ${paymentMethod === 'invoice' ? 'border-slate-400 bg-slate-50' : 'border-slate-200 hover:border-slate-300'}`} 
                      onClick={() => setPaymentMethod('invoice')}
                    >
                      <RadioGroupItem value="invoice" id="invoice" />
                      <div className="flex-1">
                        <Label htmlFor="invoice" className="font-medium cursor-pointer">Faktura (bedrift)</Label>
                        <p className="text-sm text-slate-500">Betal innen 14 dager. Krever organisasjonsnummer.</p>
                      </div>
                      <FileText className="w-6 h-6 text-slate-400" />
                    </div>
                  </RadioGroup>
                </Card>

                {/* Notes */}
                <Card className="p-6">
                  <Label htmlFor="notes">Merknader (valgfritt)</Label>
                  <textarea
                    id="notes"
                    name="notes"
                    value={formData.notes}
                    onChange={handleChange}
                    rows={3}
                    className="mt-2 flex w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
                    placeholder="Spesielle instruksjoner for levering eller produksjon..."
                    data-testid="checkout-notes"
                  />
                </Card>
              </div>

              {/* Right: Order summary */}
              <div>
                <Card className="p-6 sticky top-24">
                  <h2 className="font-semibold text-lg text-slate-900 mb-4">Din bestilling</h2>

                  <div className="space-y-4 mb-6">
                    {cart.items.map((item, index) => (
                      <div key={index} className="flex gap-3">
                        <div className="w-14 h-14 bg-slate-100 rounded-lg flex-shrink-0" />
                        <div className="flex-1 min-w-0">
                          <p className="text-sm font-medium truncate">{item.product_name}</p>
                          <p className="text-xs text-slate-500">{item.variant_color} · {item.size} · x{item.quantity}</p>
                        </div>
                        <p className="text-sm font-medium">{item.total_price.toFixed(2)} kr</p>
                      </div>
                    ))}
                  </div>

                  <div className="space-y-2 text-sm border-t pt-4">
                    <div className="flex justify-between">
                      <span className="text-slate-600">Produkter</span>
                      <span>{cart.subtotal?.toFixed(2)} kr</span>
                    </div>
                    {cart.design_total > 0 && (
                      <div className="flex justify-between">
                        <span className="text-slate-600">Trykk/Brodering</span>
                        <span>{cart.design_total?.toFixed(2)} kr</span>
                      </div>
                    )}
                    <div className="flex justify-between">
                      <span className="text-slate-600">Frakt</span>
                      <span className={shipping === 0 ? "text-green-600 font-medium" : ""}>
                        {shipping === 0 ? 'Gratis' : `${shipping} kr`}
                      </span>
                    </div>
                    {shipping > 0 && subtotalWithDesign < 2000 && (
                      <p className="text-xs text-slate-500">
                        Handl for {(2000 - subtotalWithDesign).toFixed(0)} kr mer for gratis frakt!
                      </p>
                    )}
                    <hr />
                    <div className="flex justify-between font-bold text-lg pt-2">
                      <span>Totalt</span>
                      <span data-testid="checkout-total">{total.toFixed(2)} kr</span>
                    </div>
                    <p className="text-xs text-slate-500">eks. mva</p>
                  </div>

                  <Button
                    type="submit"
                    size="lg"
                    className={`w-full mt-6 ${paymentMethod === 'vipps' ? 'bg-[#FF5B24] hover:bg-[#E5522A]' : 'bg-blue-600 hover:bg-blue-700'}`}
                    disabled={loading}
                    data-testid="place-order-btn"
                  >
                    {loading ? (
                      <>
                        <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                        Behandler...
                      </>
                    ) : (
                      <>
                        {paymentMethod === 'vipps' && 'Betal med Vipps'}
                        {paymentMethod === 'stripe' && 'Betal med kort'}
                        {paymentMethod === 'invoice' && 'Bestill med faktura'}
                      </>
                    )}
                  </Button>

                  <div className="mt-4 flex items-center justify-center gap-2 text-xs text-slate-500">
                    <Check className="w-4 h-4 text-green-600" />
                    Sikker betaling
                  </div>
                </Card>
              </div>
            </div>
          </form>
        </div>
      </div>
    </Layout>
  );
};

export const CheckoutSuccessPage = () => {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();
  const sessionId = searchParams.get('session_id');
  const [status, setStatus] = useState('checking');
  const [order, setOrder] = useState(null);

  useState(() => {
    if (sessionId) {
      pollStatus();
    }
  }, [sessionId]);

  const pollStatus = async (attempts = 0) => {
    if (attempts >= 10) {
      setStatus('timeout');
      return;
    }

    try {
      const res = await axios.get(`${API}/checkout/status/${sessionId}`);
      if (res.data.payment_status === 'paid') {
        setStatus('success');
        // Get order details
        const orderRes = await axios.get(`${API}/orders/number/${res.data.metadata?.order_number}`);
        setOrder(orderRes.data);
      } else if (res.data.status === 'expired') {
        setStatus('expired');
      } else {
        setTimeout(() => pollStatus(attempts + 1), 2000);
      }
    } catch {
      setTimeout(() => pollStatus(attempts + 1), 2000);
    }
  };

  return (
    <Layout>
      <div className="max-w-2xl mx-auto px-4 md:px-8 py-16 text-center">
        {status === 'checking' && (
          <>
            <Loader2 className="w-16 h-16 text-blue-600 animate-spin mx-auto" />
            <h1 className="mt-6 font-manrope text-2xl font-bold text-slate-900">Bekrefter betaling...</h1>
            <p className="mt-2 text-slate-600">Vennligst vent mens vi bekrefter betalingen din.</p>
          </>
        )}

        {status === 'success' && (
          <>
            <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto">
              <Check className="w-10 h-10 text-green-600" />
            </div>
            <h1 className="mt-6 font-manrope text-2xl font-bold text-slate-900" data-testid="success-title">
              Takk for din bestilling!
            </h1>
            <p className="mt-2 text-slate-600">
              Vi har mottatt bestillingen din og starter produksjonen snart.
            </p>
            {order && (
              <p className="mt-4 text-lg font-medium">
                Ordrenummer: <span className="text-blue-600">{order.order_number}</span>
              </p>
            )}
            <Button className="mt-8" onClick={() => navigate('/')}>
              Tilbake til forsiden
            </Button>
          </>
        )}

        {status === 'expired' && (
          <>
            <div className="w-20 h-20 bg-red-100 rounded-full flex items-center justify-center mx-auto">
              <span className="text-3xl">⏰</span>
            </div>
            <h1 className="mt-6 font-manrope text-2xl font-bold text-slate-900">Betalingen utløp</h1>
            <p className="mt-2 text-slate-600">Betalingssesjonen har utløpt. Vennligst prøv igjen.</p>
            <Button className="mt-8" onClick={() => navigate('/handlekurv')}>
              Tilbake til handlekurven
            </Button>
          </>
        )}

        {status === 'timeout' && (
          <>
            <div className="w-20 h-20 bg-yellow-100 rounded-full flex items-center justify-center mx-auto">
              <span className="text-3xl">⚠️</span>
            </div>
            <h1 className="mt-6 font-manrope text-2xl font-bold text-slate-900">Kunne ikke bekrefte</h1>
            <p className="mt-2 text-slate-600">
              Vi kunne ikke bekrefte betalingen. Sjekk e-posten din for bekreftelse.
            </p>
            <Button className="mt-8" onClick={() => navigate('/')}>
              Tilbake til forsiden
            </Button>
          </>
        )}
      </div>
    </Layout>
  );
};

export const CheckoutCancelPage = () => {
  const navigate = useNavigate();

  return (
    <Layout>
      <div className="max-w-2xl mx-auto px-4 md:px-8 py-16 text-center">
        <div className="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mx-auto">
          <span className="text-3xl">😔</span>
        </div>
        <h1 className="mt-6 font-manrope text-2xl font-bold text-slate-900">Bestilling avbrutt</h1>
        <p className="mt-2 text-slate-600">
          Betalingen ble avbrutt. Handlekurven din er fortsatt tilgjengelig.
        </p>
        <div className="mt-8 flex gap-4 justify-center">
          <Button variant="outline" onClick={() => navigate('/handlekurv')}>
            Tilbake til handlekurv
          </Button>
          <Button onClick={() => navigate('/produkter')}>
            Fortsett å handle
          </Button>
        </div>
      </div>
    </Layout>
  );
};

export default CheckoutPage;
