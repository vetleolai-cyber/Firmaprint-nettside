import "@/App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "sonner";
import { AuthProvider, CartProvider } from "./context/AppContext";
import HomePage from "./pages/HomePage";
import ProductsPage from "./pages/ProductsPage";
import ProductPage from "./pages/ProductPage";
import CartPage from "./pages/CartPage";
import CheckoutPage, { CheckoutSuccessPage, CheckoutCancelPage } from "./pages/CheckoutPage";
import BusinessPage from "./pages/BusinessPage";
import PrintVsEmbroideryPage from "./pages/PrintVsEmbroideryPage";
import ContactPage, { LoginPage, RegisterPage } from "./pages/ContactPage";
import FAQPage from "./pages/FAQPage";
import AboutPage, { PrivacyPage, TermsPage } from "./pages/StaticPages";

function App() {
  return (
    <AuthProvider>
      <CartProvider>
        <div className="App font-inter">
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/produkter" element={<ProductsPage />} />
              <Route path="/kategori/:category" element={<ProductsPage />} />
              <Route path="/produkt/:slug" element={<ProductPage />} />
              <Route path="/handlekurv" element={<CartPage />} />
              <Route path="/checkout" element={<CheckoutPage />} />
              <Route path="/checkout/success" element={<CheckoutSuccessPage />} />
              <Route path="/checkout/cancel" element={<CheckoutCancelPage />} />
              <Route path="/bedrift" element={<BusinessPage />} />
              <Route path="/brodyr-vs-trykk" element={<PrintVsEmbroideryPage />} />
              <Route path="/kontakt" element={<ContactPage />} />
              <Route path="/faq" element={<FAQPage />} />
              <Route path="/om-oss" element={<AboutPage />} />
              <Route path="/personvern" element={<PrivacyPage />} />
              <Route path="/vilkar" element={<TermsPage />} />
              <Route path="/logg-inn" element={<LoginPage />} />
              <Route path="/registrer" element={<RegisterPage />} />
            </Routes>
          </BrowserRouter>
          <Toaster position="top-center" richColors />
        </div>
      </CartProvider>
    </AuthProvider>
  );
}

export default App;
