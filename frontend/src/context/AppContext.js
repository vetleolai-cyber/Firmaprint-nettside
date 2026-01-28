import { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

const API = `${process.env.REACT_APP_BACKEND_URL}/api`;

// Auth Context
const AuthContext = createContext(null);

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem('fp_token'));
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (token) {
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      fetchUser();
    } else {
      setLoading(false);
    }
  }, [token]);

  const fetchUser = async () => {
    try {
      const res = await axios.get(`${API}/auth/me`);
      setUser(res.data);
    } catch {
      logout();
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    const res = await axios.post(`${API}/auth/login`, { email, password });
    localStorage.setItem('fp_token', res.data.access_token);
    setToken(res.data.access_token);
    setUser(res.data.user);
    axios.defaults.headers.common['Authorization'] = `Bearer ${res.data.access_token}`;
    return res.data;
  };

  const register = async (userData) => {
    const res = await axios.post(`${API}/auth/register`, userData);
    localStorage.setItem('fp_token', res.data.access_token);
    setToken(res.data.access_token);
    setUser(res.data.user);
    axios.defaults.headers.common['Authorization'] = `Bearer ${res.data.access_token}`;
    return res.data;
  };

  const logout = () => {
    localStorage.removeItem('fp_token');
    setToken(null);
    setUser(null);
    delete axios.defaults.headers.common['Authorization'];
  };

  return (
    <AuthContext.Provider value={{ user, token, loading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Cart Context
const CartContext = createContext(null);

export const useCart = () => useContext(CartContext);

export const CartProvider = ({ children }) => {
  const [cart, setCart] = useState({ items: [], total: 0 });
  const [sessionId] = useState(() => {
    let id = localStorage.getItem('fp_session');
    if (!id) {
      id = crypto.randomUUID();
      localStorage.setItem('fp_session', id);
    }
    return id;
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchCart();
  }, [sessionId]);

  const fetchCart = async () => {
    try {
      const res = await axios.get(`${API}/cart/${sessionId}`);
      setCart(res.data);
    } catch (err) {
      console.error('Failed to fetch cart:', err);
    } finally {
      setLoading(false);
    }
  };

  const addToCart = async (item) => {
    const res = await axios.post(`${API}/cart/${sessionId}/add`, item);
    setCart(res.data);
    return res.data;
  };

  const removeFromCart = async (index) => {
    const res = await axios.delete(`${API}/cart/${sessionId}/item/${index}`);
    setCart(res.data);
    return res.data;
  };

  const clearCart = async () => {
    await axios.delete(`${API}/cart/${sessionId}`);
    setCart({ items: [], total: 0 });
  };

  const itemCount = cart.items?.reduce((sum, item) => sum + item.quantity, 0) || 0;

  return (
    <CartContext.Provider value={{ cart, sessionId, loading, addToCart, removeFromCart, clearCart, fetchCart, itemCount }}>
      {children}
    </CartContext.Provider>
  );
};
