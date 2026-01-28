import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Trash2, Minus, Plus, ShoppingBag, ArrowRight } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card } from '../components/ui/card';
import { Layout } from '../components/Layout';
import { useCart } from '../context/AppContext';
import { toast } from 'sonner';

export const CartPage = () => {
  const { cart, removeFromCart, loading } = useCart();
  const navigate = useNavigate();

  const handleRemove = async (index) => {
    try {
      await removeFromCart(index);
      toast.success('Vare fjernet fra handlekurven');
    } catch {
      toast.error('Kunne ikke fjerne varen');
    }
  };

  if (loading) {
    return (
      <Layout>
        <div className="max-w-4xl mx-auto px-4 md:px-8 py-8">
          <div className="animate-pulse space-y-4">
            <div className="h-8 bg-slate-100 rounded w-48" />
            <div className="h-32 bg-slate-100 rounded" />
            <div className="h-32 bg-slate-100 rounded" />
          </div>
        </div>
      </Layout>
    );
  }

  if (!cart.items || cart.items.length === 0) {
    return (
      <Layout>
        <div className="max-w-4xl mx-auto px-4 md:px-8 py-16 text-center">
          <div className="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mx-auto mb-6">
            <ShoppingBag className="w-10 h-10 text-slate-400" />
          </div>
          <h1 className="font-manrope text-2xl font-bold text-slate-900">Handlekurven er tom</h1>
          <p className="mt-2 text-slate-600">Legg til noen produkter for å komme i gang</p>
          <Button className="mt-6" asChild data-testid="empty-cart-browse-btn">
            <Link to="/produkter">Se produkter</Link>
          </Button>
        </div>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="bg-slate-50 min-h-screen">
        <div className="max-w-4xl mx-auto px-4 md:px-8 py-8">
          <h1 className="font-manrope text-2xl md:text-3xl font-bold text-slate-900 mb-8" data-testid="cart-title">
            Handlekurv ({cart.items.length} {cart.items.length === 1 ? 'vare' : 'varer'})
          </h1>

          <div className="grid lg:grid-cols-3 gap-8">
            {/* Cart items */}
            <div className="lg:col-span-2 space-y-4">
              {cart.items.map((item, index) => (
                <Card key={index} className="p-4" data-testid={`cart-item-${index}`}>
                  <div className="flex gap-4">
                    {/* Product image or design preview */}
                    <div className="w-24 h-24 bg-slate-100 rounded-lg overflow-hidden flex-shrink-0">
                      {item.design?.logo_preview ? (
                        <div className="w-full h-full relative">
                          <img src={item.design.logo_preview} alt="Design" className="w-full h-full object-contain p-2" />
                        </div>
                      ) : (
                        <div className="w-full h-full bg-slate-200" />
                      )}
                    </div>

                    {/* Item details */}
                    <div className="flex-1 min-w-0">
                      <h3 className="font-semibold text-slate-900 truncate">{item.product_name}</h3>
                      <p className="text-sm text-slate-500">
                        {item.variant_color} · {item.size}
                      </p>
                      {item.design && (
                        <p className="text-sm text-blue-600">
                          {item.design.print_method === 'embroidery' ? 'Brodering' : 'Trykk'} på {item.design.print_area}
                        </p>
                      )}
                      <div className="flex items-center justify-between mt-3">
                        <div className="flex items-center gap-2">
                          <span className="text-sm text-slate-500">Antall: {item.quantity}</span>
                        </div>
                        <div className="text-right">
                          <p className="font-semibold text-slate-900">{item.total_price.toFixed(2)} kr</p>
                          {item.design_price > 0 && (
                            <p className="text-xs text-slate-500">
                              inkl. {(item.design_price * item.quantity).toFixed(2)} kr for dekor
                            </p>
                          )}
                        </div>
                      </div>
                    </div>

                    {/* Remove button */}
                    <Button
                      variant="ghost"
                      size="icon"
                      className="text-slate-400 hover:text-red-600 flex-shrink-0"
                      onClick={() => handleRemove(index)}
                      data-testid={`remove-item-${index}`}
                    >
                      <Trash2 className="w-4 h-4" />
                    </Button>
                  </div>
                </Card>
              ))}
            </div>

            {/* Order summary */}
            <div>
              <Card className="p-6 sticky top-24">
                <h2 className="font-semibold text-lg text-slate-900 mb-4">Ordresammendrag</h2>
                
                <div className="space-y-3 text-sm">
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
                    <span className="text-slate-500">Beregnes ved checkout</span>
                  </div>
                  <hr />
                  <div className="flex justify-between font-bold text-lg">
                    <span>Totalt</span>
                    <span data-testid="cart-total">{cart.total?.toFixed(2)} kr</span>
                  </div>
                  <p className="text-xs text-slate-500">eks. mva</p>
                </div>

                <Button
                  size="lg"
                  className="w-full mt-6 bg-slate-900 hover:bg-slate-800"
                  onClick={() => navigate('/checkout')}
                  data-testid="checkout-btn"
                >
                  Gå til kassen <ArrowRight className="ml-2 w-4 h-4" />
                </Button>

                <Button
                  variant="outline"
                  className="w-full mt-3"
                  asChild
                >
                  <Link to="/produkter">Fortsett å handle</Link>
                </Button>
              </Card>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default CartPage;
