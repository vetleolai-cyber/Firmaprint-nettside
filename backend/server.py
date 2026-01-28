from fastapi import FastAPI, APIRouter, HTTPException, UploadFile, File, Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field, ConfigDict, EmailStr
from typing import List, Optional, Dict, Any
import uuid
from datetime import datetime, timezone, timedelta
import jwt
import bcrypt
import base64

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# JWT Configuration
JWT_SECRET = os.environ.get('JWT_SECRET', 'firmaprint-secret-key-2024')
JWT_ALGORITHM = 'HS256'
JWT_EXPIRATION_HOURS = 24

# Create the main app
app = FastAPI(title="Firmaprint.no API", version="1.0.0")

# Create routers
api_router = APIRouter(prefix="/api")
security = HTTPBearer(auto_error=False)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# ==================== MODELS ====================

# Auth Models
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    company_name: Optional[str] = None
    org_number: Optional[str] = None
    is_business: bool = False

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str
    company_name: Optional[str] = None
    org_number: Optional[str] = None
    is_business: bool = False
    discount_tier: int = 0
    created_at: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse

# Product Models
class ProductVariant(BaseModel):
    color: str
    color_hex: str
    sizes: List[str]
    images: List[str]
    stock: Dict[str, int] = {}

class PrintArea(BaseModel):
    name: str
    name_no: str
    x: float
    y: float
    width: float
    height: float
    max_width_cm: float
    max_height_cm: float

class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    slug: str
    description: str
    category: str
    brand: Optional[str] = None
    base_price: float
    variants: List[ProductVariant]
    print_methods: List[str]  # ["embroidery", "print", "both"]
    print_areas: List[PrintArea]
    materials: List[str]
    fit: str
    delivery_days: int = 5
    best_for: List[str] = []
    min_quantity: int = 1
    featured: bool = False
    active: bool = True
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class ProductCreate(BaseModel):
    name: str
    slug: str
    description: str
    category: str
    brand: Optional[str] = None
    base_price: float
    variants: List[ProductVariant]
    print_methods: List[str]
    print_areas: List[PrintArea]
    materials: List[str]
    fit: str
    delivery_days: int = 5
    best_for: List[str] = []
    min_quantity: int = 1
    featured: bool = False

# Cart Models
class DesignObject(BaseModel):
    logo_url: str
    logo_preview: str
    position_x: float
    position_y: float
    scale: float
    rotation: float
    view: str  # front, back, side
    print_area: str
    print_method: str  # embroidery or print
    width_cm: float
    height_cm: float
    colors: List[str] = []
    complexity: str = "normal"  # simple, normal, detailed
    warnings: List[str] = []

class CartItem(BaseModel):
    product_id: str
    product_name: str
    variant_color: str
    size: str
    quantity: int
    base_price: float
    design: Optional[DesignObject] = None
    design_price: float = 0
    total_price: float

class Cart(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: Optional[str] = None
    session_id: str
    items: List[CartItem] = []
    subtotal: float = 0
    design_total: float = 0
    shipping: float = 0
    total: float = 0
    updated_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class AddToCartRequest(BaseModel):
    product_id: str
    variant_color: str
    size: str
    quantity: int
    design: Optional[DesignObject] = None

# Order Models
class ShippingAddress(BaseModel):
    name: str
    company: Optional[str] = None
    street: str
    city: str
    postal_code: str
    country: str = "Norge"
    phone: str
    email: EmailStr

class Order(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    order_number: str
    user_id: Optional[str] = None
    items: List[CartItem]
    shipping_address: ShippingAddress
    payment_method: str  # stripe, vipps, invoice
    payment_status: str = "pending"
    stripe_session_id: Optional[str] = None
    vipps_reference: Optional[str] = None
    subtotal: float
    design_total: float
    shipping_cost: float = 0
    discount: float = 0
    total: float
    status: str = "pending"
    notes: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class CreateOrderRequest(BaseModel):
    cart_session_id: str
    shipping_address: ShippingAddress
    payment_method: str
    notes: Optional[str] = None

# Quote Request Model
class QuoteRequest(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    company_name: str
    contact_name: str
    email: EmailStr
    phone: str
    product_types: List[str]
    estimated_quantity: str
    message: str
    logo_url: Optional[str] = None
    status: str = "new"
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class QuoteRequestCreate(BaseModel):
    company_name: str
    contact_name: str
    email: EmailStr
    phone: str
    product_types: List[str]
    estimated_quantity: str
    message: str
    logo_url: Optional[str] = None

# Contact Message Model
class ContactMessage(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    email: EmailStr
    phone: Optional[str] = None
    subject: str
    message: str
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    subject: str
    message: str

# ==================== AUTH HELPERS ====================

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def create_token(user_id: str) -> str:
    payload = {
        'user_id': user_id,
        'exp': datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRATION_HOURS),
        'iat': datetime.now(timezone.utc)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials:
        return None
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user = await db.users.find_one({'id': payload['user_id']}, {'_id': 0})
        return user
    except:
        return None

async def require_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = await get_current_user(credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Ikke autorisert")
    return user

# ==================== PRICING CONSTANTS ====================
# Alle priser eks. mva
PRINT_PRICE_SMALL = 59.0  # Små trykk (bryst, erme)
PRINT_PRICE_LARGE = 79.0  # Store trykk (rygg)
EMBROIDERY_PRICE = 89.0   # Brodering
SHIPPING_COST = 99.0      # Frakt
FREE_SHIPPING_THRESHOLD = 2000.0  # Gratis frakt over dette beløpet

# Print areas som regnes som "store"
LARGE_PRINT_AREAS = ["full_back", "back", "center_chest"]

# ==================== PRICING LOGIC ====================

def calculate_design_price(design: DesignObject, quantity: int) -> float:
    """Calculate price for design/print based on method and placement"""
    
    if design.print_method == "embroidery":
        # Brodering: 89 kr per stk
        return EMBROIDERY_PRICE
    else:
        # Trykk: 59 kr for små, 79 kr for store
        if design.print_area in LARGE_PRINT_AREAS:
            return PRINT_PRICE_LARGE
        else:
            return PRINT_PRICE_SMALL

def calculate_shipping(subtotal: float) -> float:
    """Calculate shipping cost - free over 2000 kr"""
    if subtotal >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    return SHIPPING_COST

# ==================== AUTH ENDPOINTS ====================

@api_router.post("/auth/register", response_model=TokenResponse)
async def register(user_data: UserCreate):
    # Check if email exists
    existing = await db.users.find_one({'email': user_data.email})
    if existing:
        raise HTTPException(status_code=400, detail="E-postadressen er allerede registrert")
    
    user_id = str(uuid.uuid4())
    user = {
        'id': user_id,
        'email': user_data.email,
        'password_hash': hash_password(user_data.password),
        'name': user_data.name,
        'company_name': user_data.company_name,
        'org_number': user_data.org_number,
        'is_business': user_data.is_business,
        'discount_tier': 0,
        'created_at': datetime.now(timezone.utc).isoformat()
    }
    
    await db.users.insert_one(user)
    
    token = create_token(user_id)
    user_response = UserResponse(
        id=user_id,
        email=user['email'],
        name=user['name'],
        company_name=user['company_name'],
        org_number=user['org_number'],
        is_business=user['is_business'],
        discount_tier=user['discount_tier'],
        created_at=user['created_at']
    )
    
    return TokenResponse(access_token=token, user=user_response)

@api_router.post("/auth/login", response_model=TokenResponse)
async def login(credentials: UserLogin):
    user = await db.users.find_one({'email': credentials.email}, {'_id': 0})
    if not user or not verify_password(credentials.password, user['password_hash']):
        raise HTTPException(status_code=401, detail="Ugyldig e-post eller passord")
    
    token = create_token(user['id'])
    user_response = UserResponse(
        id=user['id'],
        email=user['email'],
        name=user['name'],
        company_name=user.get('company_name'),
        org_number=user.get('org_number'),
        is_business=user.get('is_business', False),
        discount_tier=user.get('discount_tier', 0),
        created_at=user['created_at']
    )
    
    return TokenResponse(access_token=token, user=user_response)

@api_router.get("/auth/me", response_model=UserResponse)
async def get_me(user = Depends(require_user)):
    return UserResponse(
        id=user['id'],
        email=user['email'],
        name=user['name'],
        company_name=user.get('company_name'),
        org_number=user.get('org_number'),
        is_business=user.get('is_business', False),
        discount_tier=user.get('discount_tier', 0),
        created_at=user['created_at']
    )

# ==================== PRODUCT ENDPOINTS ====================

@api_router.get("/products", response_model=List[Product])
async def get_products(
    category: Optional[str] = None,
    brand: Optional[str] = None,
    print_method: Optional[str] = None,
    featured: Optional[bool] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    search: Optional[str] = None,
    limit: int = 50,
    skip: int = 0
):
    query = {'active': True}
    
    if category:
        query['category'] = category
    if brand:
        query['brand'] = brand
    if print_method:
        query['print_methods'] = {'$in': [print_method]}
    if featured is not None:
        query['featured'] = featured
    if min_price is not None:
        query['base_price'] = {'$gte': min_price}
    if max_price is not None:
        query.setdefault('base_price', {})['$lte'] = max_price
    if search:
        query['$or'] = [
            {'name': {'$regex': search, '$options': 'i'}},
            {'description': {'$regex': search, '$options': 'i'}}
        ]
    
    products = await db.products.find(query, {'_id': 0}).skip(skip).limit(limit).to_list(limit)
    return products

@api_router.get("/products/{slug}", response_model=Product)
async def get_product(slug: str):
    product = await db.products.find_one({'slug': slug, 'active': True}, {'_id': 0})
    if not product:
        raise HTTPException(status_code=404, detail="Produkt ikke funnet")
    return product

@api_router.get("/categories")
async def get_categories():
    categories = [
        {"id": "caps", "name": "Capser", "slug": "caps", "icon": "cap"},
        {"id": "tshirts", "name": "T-skjorter", "slug": "t-skjorter", "icon": "shirt"},
        {"id": "hoodies", "name": "Gensere & Hoodies", "slug": "gensere-hoodies", "icon": "hoodie"},
        {"id": "jackets", "name": "Jakker", "slug": "jakker", "icon": "jacket"},
        {"id": "workwear", "name": "Arbeidsklær", "slug": "arbeidsklaer", "icon": "hardhat"},
        {"id": "accessories", "name": "Tilbehør", "slug": "tilbehor", "icon": "bag"}
    ]
    return categories

@api_router.get("/products/category/{category}", response_model=List[Product])
async def get_products_by_category(category: str, limit: int = 50, skip: int = 0):
    products = await db.products.find(
        {'category': category, 'active': True}, 
        {'_id': 0}
    ).skip(skip).limit(limit).to_list(limit)
    return products

# ==================== CART ENDPOINTS ====================

@api_router.get("/cart/{session_id}", response_model=Cart)
async def get_cart(session_id: str):
    cart = await db.carts.find_one({'session_id': session_id}, {'_id': 0})
    if not cart:
        cart = Cart(session_id=session_id).model_dump()
        await db.carts.insert_one(cart)
    return cart

@api_router.post("/cart/{session_id}/add", response_model=Cart)
async def add_to_cart(session_id: str, item: AddToCartRequest):
    # Get or create cart
    cart = await db.carts.find_one({'session_id': session_id}, {'_id': 0})
    if not cart:
        cart = Cart(session_id=session_id).model_dump()
    
    # Get product
    product = await db.products.find_one({'id': item.product_id}, {'_id': 0})
    if not product:
        raise HTTPException(status_code=404, detail="Produkt ikke funnet")
    
    # Calculate design price if design exists
    design_price = 0
    if item.design:
        design_price = calculate_design_price(item.design, item.quantity)
    
    # Create cart item
    cart_item = CartItem(
        product_id=item.product_id,
        product_name=product['name'],
        variant_color=item.variant_color,
        size=item.size,
        quantity=item.quantity,
        base_price=product['base_price'],
        design=item.design,
        design_price=design_price,
        total_price=(product['base_price'] * item.quantity) + (design_price * item.quantity)
    )
    
    # Add or update item
    items = cart.get('items', [])
    existing_idx = None
    for i, existing in enumerate(items):
        if (existing['product_id'] == item.product_id and 
            existing['variant_color'] == item.variant_color and 
            existing['size'] == item.size):
            existing_idx = i
            break
    
    if existing_idx is not None:
        items[existing_idx] = cart_item.model_dump()
    else:
        items.append(cart_item.model_dump())
    
    # Recalculate totals
    subtotal = sum(i['base_price'] * i['quantity'] for i in items)
    design_total = sum(i['design_price'] * i['quantity'] for i in items)
    shipping = calculate_shipping(subtotal + design_total)
    total = subtotal + design_total + shipping
    
    # Update cart
    updated_cart = {
        'id': cart.get('id', str(uuid.uuid4())),
        'user_id': cart.get('user_id'),
        'session_id': session_id,
        'items': items,
        'subtotal': round(subtotal, 2),
        'design_total': round(design_total, 2),
        'shipping': round(shipping, 2),
        'total': round(total, 2),
        'updated_at': datetime.now(timezone.utc).isoformat()
    }
    
    await db.carts.update_one(
        {'session_id': session_id},
        {'$set': updated_cart},
        upsert=True
    )
    
    return updated_cart

@api_router.delete("/cart/{session_id}/item/{item_index}")
async def remove_from_cart(session_id: str, item_index: int):
    cart = await db.carts.find_one({'session_id': session_id}, {'_id': 0})
    if not cart:
        raise HTTPException(status_code=404, detail="Handlekurv ikke funnet")
    
    items = cart.get('items', [])
    if item_index < 0 or item_index >= len(items):
        raise HTTPException(status_code=400, detail="Ugyldig vareindeks")
    
    items.pop(item_index)
    
    # Recalculate
    subtotal = sum(i['base_price'] * i['quantity'] for i in items)
    design_total = sum(i['design_price'] * i['quantity'] for i in items)
    shipping = calculate_shipping(subtotal + design_total)
    total = subtotal + design_total + shipping
    
    cart['items'] = items
    cart['subtotal'] = round(subtotal, 2)
    cart['design_total'] = round(design_total, 2)
    cart['shipping'] = round(shipping, 2)
    cart['total'] = round(total, 2)
    cart['updated_at'] = datetime.now(timezone.utc).isoformat()
    
    await db.carts.update_one({'session_id': session_id}, {'$set': cart})
    
    return cart

@api_router.delete("/cart/{session_id}")
async def clear_cart(session_id: str):
    await db.carts.delete_one({'session_id': session_id})
    return {"message": "Handlekurv tømt"}

# ==================== ORDER ENDPOINTS ====================

@api_router.post("/orders/create")
async def create_order(request: CreateOrderRequest, http_request: Request):
    # Get cart
    cart = await db.carts.find_one({'session_id': request.cart_session_id}, {'_id': 0})
    if not cart or not cart.get('items'):
        raise HTTPException(status_code=400, detail="Handlekurven er tom")
    
    # Generate order number
    order_count = await db.orders.count_documents({})
    order_number = f"FP{datetime.now().strftime('%Y%m')}{order_count + 1:04d}"
    
    order = Order(
        order_number=order_number,
        user_id=cart.get('user_id'),
        items=[CartItem(**item) for item in cart['items']],
        shipping_address=request.shipping_address,
        payment_method=request.payment_method,
        subtotal=cart['subtotal'],
        design_total=cart['design_total'],
        total=cart['total'],
        notes=request.notes
    )
    
    if request.payment_method == "stripe":
        # Create Stripe checkout session
        from emergentintegrations.payments.stripe.checkout import StripeCheckout, CheckoutSessionRequest
        
        api_key = os.environ.get('STRIPE_API_KEY')
        host_url = str(http_request.base_url).rstrip('/')
        webhook_url = f"{host_url}/api/webhook/stripe"
        
        stripe_checkout = StripeCheckout(api_key=api_key, webhook_url=webhook_url)
        
        # Get origin from request headers
        origin = http_request.headers.get('origin', host_url)
        success_url = f"{origin}/checkout/success?session_id={{CHECKOUT_SESSION_ID}}"
        cancel_url = f"{origin}/checkout/cancel"
        
        checkout_request = CheckoutSessionRequest(
            amount=float(order.total),
            currency="nok",
            success_url=success_url,
            cancel_url=cancel_url,
            metadata={
                "order_id": order.id,
                "order_number": order_number
            }
        )
        
        session = await stripe_checkout.create_checkout_session(checkout_request)
        order.stripe_session_id = session.session_id
        
        # Save payment transaction
        await db.payment_transactions.insert_one({
            'id': str(uuid.uuid4()),
            'order_id': order.id,
            'session_id': session.session_id,
            'amount': float(order.total),
            'currency': 'nok',
            'payment_status': 'pending',
            'metadata': checkout_request.metadata,
            'created_at': datetime.now(timezone.utc).isoformat()
        })
        
        # Save order
        order_dict = order.model_dump()
        await db.orders.insert_one(order_dict)
        
        # Clear cart
        await db.carts.delete_one({'session_id': request.cart_session_id})
        
        return {"order": order_dict, "checkout_url": session.url}
    
    else:  # Invoice
        order.payment_status = "awaiting_invoice"
        order.status = "awaiting_payment"
        
        order_dict = order.model_dump()
        await db.orders.insert_one(order_dict)
        
        # Clear cart
        await db.carts.delete_one({'session_id': request.cart_session_id})
        
        return {"order": order_dict}

@api_router.get("/orders/{order_id}")
async def get_order(order_id: str):
    order = await db.orders.find_one({'id': order_id}, {'_id': 0})
    if not order:
        raise HTTPException(status_code=404, detail="Ordre ikke funnet")
    return order

@api_router.get("/orders/number/{order_number}")
async def get_order_by_number(order_number: str):
    order = await db.orders.find_one({'order_number': order_number}, {'_id': 0})
    if not order:
        raise HTTPException(status_code=404, detail="Ordre ikke funnet")
    return order

@api_router.get("/checkout/status/{session_id}")
async def get_checkout_status(session_id: str):
    from emergentintegrations.payments.stripe.checkout import StripeCheckout
    
    api_key = os.environ.get('STRIPE_API_KEY')
    stripe_checkout = StripeCheckout(api_key=api_key, webhook_url="")
    
    status = await stripe_checkout.get_checkout_status(session_id)
    
    # Update order and transaction if paid
    if status.payment_status == "paid":
        await db.payment_transactions.update_one(
            {'session_id': session_id},
            {'$set': {'payment_status': 'paid', 'updated_at': datetime.now(timezone.utc).isoformat()}}
        )
        await db.orders.update_one(
            {'stripe_session_id': session_id},
            {'$set': {'payment_status': 'paid', 'status': 'processing'}}
        )
    
    return status

@api_router.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    from emergentintegrations.payments.stripe.checkout import StripeCheckout
    
    body = await request.body()
    signature = request.headers.get("Stripe-Signature")
    
    api_key = os.environ.get('STRIPE_API_KEY')
    stripe_checkout = StripeCheckout(api_key=api_key, webhook_url="")
    
    try:
        webhook_response = await stripe_checkout.handle_webhook(body, signature)
        
        if webhook_response.payment_status == "paid":
            await db.payment_transactions.update_one(
                {'session_id': webhook_response.session_id},
                {'$set': {'payment_status': 'paid', 'updated_at': datetime.now(timezone.utc).isoformat()}}
            )
            await db.orders.update_one(
                {'stripe_session_id': webhook_response.session_id},
                {'$set': {'payment_status': 'paid', 'status': 'processing'}}
            )
        
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return {"status": "error"}

# ==================== QUOTE ENDPOINTS ====================

@api_router.post("/quotes", response_model=QuoteRequest)
async def create_quote(quote: QuoteRequestCreate):
    quote_obj = QuoteRequest(**quote.model_dump())
    await db.quotes.insert_one(quote_obj.model_dump())
    return quote_obj

@api_router.get("/quotes", response_model=List[QuoteRequest])
async def get_quotes(user = Depends(require_user)):
    if not user.get('is_admin'):
        raise HTTPException(status_code=403, detail="Ikke tilgang")
    quotes = await db.quotes.find({}, {'_id': 0}).to_list(100)
    return quotes

# ==================== CONTACT ENDPOINTS ====================

@api_router.post("/contact", response_model=ContactMessage)
async def send_contact_message(message: ContactMessageCreate):
    msg_obj = ContactMessage(**message.model_dump())
    await db.contact_messages.insert_one(msg_obj.model_dump())
    return msg_obj

# ==================== FILE UPLOAD ENDPOINT ====================

@api_router.post("/upload/logo")
async def upload_logo(file: UploadFile = File(...)):
    """Upload logo file and return base64 encoded data"""
    allowed_types = ['image/png', 'image/jpeg', 'image/svg+xml', 'application/pdf']
    
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Ugyldig filtype. Bruk PNG, JPG, SVG eller PDF.")
    
    # Read file content
    content = await file.read()
    
    # Check file size (max 10MB)
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="Filen er for stor. Maks 10MB.")
    
    # Encode to base64
    encoded = base64.b64encode(content).decode('utf-8')
    
    # Save to database
    logo_id = str(uuid.uuid4())
    logo_doc = {
        'id': logo_id,
        'filename': file.filename,
        'content_type': file.content_type,
        'size': len(content),
        'data': encoded,
        'created_at': datetime.now(timezone.utc).isoformat()
    }
    
    await db.logos.insert_one(logo_doc)
    
    return {
        'id': logo_id,
        'filename': file.filename,
        'content_type': file.content_type,
        'size': len(content),
        'data_url': f"data:{file.content_type};base64,{encoded[:50]}..."  # Preview only
    }

@api_router.get("/logos/{logo_id}")
async def get_logo(logo_id: str):
    logo = await db.logos.find_one({'id': logo_id}, {'_id': 0})
    if not logo:
        raise HTTPException(status_code=404, detail="Logo ikke funnet")
    
    return {
        'id': logo['id'],
        'filename': logo['filename'],
        'content_type': logo['content_type'],
        'data_url': f"data:{logo['content_type']};base64,{logo['data']}"
    }

# ==================== PRICING ENDPOINT ====================

@api_router.get("/pricing/info")
async def get_pricing_info():
    """Get current pricing information"""
    return {
        "print_small": PRINT_PRICE_SMALL,
        "print_large": PRINT_PRICE_LARGE,
        "embroidery": EMBROIDERY_PRICE,
        "shipping": SHIPPING_COST,
        "free_shipping_threshold": FREE_SHIPPING_THRESHOLD,
        "large_print_areas": LARGE_PRINT_AREAS,
        "currency": "NOK",
        "vat_rate": 0.25,
        "prices_exclude_vat": True
    }

@api_router.post("/pricing/calculate")
async def calculate_pricing(
    print_method: str,
    print_area: str = "left_chest",
    quantity: int = 1
):
    """Calculate price for design/print"""
    if print_method == "embroidery":
        price_per_item = EMBROIDERY_PRICE
    else:
        price_per_item = PRINT_PRICE_LARGE if print_area in LARGE_PRINT_AREAS else PRINT_PRICE_SMALL
    
    total_price = price_per_item * quantity
    
    return {
        "price_per_item": round(price_per_item, 2),
        "total_price": round(total_price, 2),
        "quantity": quantity,
        "breakdown": {
            "method": print_method,
            "print_area": print_area,
            "is_large_area": print_area in LARGE_PRINT_AREAS
        }
    }

# ==================== VIPPS PAYMENT ENDPOINTS ====================

import httpx
import time

# Vipps Token Manager
class VippsTokenManager:
    def __init__(self):
        self.access_token: Optional[str] = None
        self.token_expires_at: float = 0
    
    async def get_access_token(self) -> str:
        """Get a valid access token, requesting a new one if expired."""
        current_time = time.time()
        
        # Return cached token if still valid (with 60-second buffer)
        if self.access_token and current_time < (self.token_expires_at - 60):
            return self.access_token
        
        vipps_client_id = os.environ.get('VIPPS_CLIENT_ID')
        vipps_client_secret = os.environ.get('VIPPS_CLIENT_SECRET')
        vipps_subscription_key = os.environ.get('VIPPS_SUBSCRIPTION_KEY')
        vipps_msn = os.environ.get('VIPPS_MSN')
        vipps_api_url = os.environ.get('VIPPS_API_URL', 'https://apitest.vipps.no')
        
        if not all([vipps_client_id, vipps_client_secret, vipps_subscription_key, vipps_msn]):
            raise HTTPException(status_code=500, detail="Vipps er ikke konfigurert")
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{vipps_api_url}/accesstoken/get",
                headers={
                    "Content-Type": "application/json",
                    "client_id": vipps_client_id,
                    "client_secret": vipps_client_secret,
                    "Ocp-Apim-Subscription-Key": vipps_subscription_key,
                    "Merchant-Serial-Number": vipps_msn,
                    "Vipps-System-Name": "Firmaprint",
                    "Vipps-System-Version": "1.0.0",
                },
            )
            
            if response.status_code != 200:
                logger.error(f"Vipps token error: {response.text}")
                raise HTTPException(status_code=500, detail="Kunne ikke koble til Vipps")
            
            token_data = response.json()
            self.access_token = token_data["access_token"]
            self.token_expires_at = current_time + token_data["expires_in"]
            
            return self.access_token

vipps_token_manager = VippsTokenManager()

class VippsPaymentRequest(BaseModel):
    order_id: str
    amount: int  # In øre (NOK * 100)
    description: str
    return_url: str

@api_router.post("/payments/vipps/initiate")
async def initiate_vipps_payment(request: VippsPaymentRequest):
    """Initiate a Vipps payment"""
    try:
        access_token = await vipps_token_manager.get_access_token()
        vipps_api_url = os.environ.get('VIPPS_API_URL', 'https://apitest.vipps.no')
        vipps_subscription_key = os.environ.get('VIPPS_SUBSCRIPTION_KEY')
        vipps_msn = os.environ.get('VIPPS_MSN')
        
        # Generate unique reference
        reference = f"fp-{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}"
        
        payment_payload = {
            "amount": {
                "currency": "NOK",
                "value": request.amount
            },
            "paymentMethod": {
                "type": "WALLET"
            },
            "reference": reference,
            "returnUrl": request.return_url,
            "userFlow": "WEB_REDIRECT",
            "paymentDescription": request.description
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{vipps_api_url}/epayment/v1/payments",
                json=payment_payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {access_token}",
                    "Ocp-Apim-Subscription-Key": vipps_subscription_key,
                    "Merchant-Serial-Number": vipps_msn,
                    "Idempotency-Key": str(uuid.uuid4()),
                    "Vipps-System-Name": "Firmaprint",
                    "Vipps-System-Version": "1.0.0",
                },
            )
            
            if response.status_code != 201:
                logger.error(f"Vipps payment error: {response.text}")
                raise HTTPException(status_code=400, detail="Kunne ikke opprette Vipps-betaling")
            
            payment_data = response.json()
            
            # Store payment info
            await db.payment_transactions.insert_one({
                'id': str(uuid.uuid4()),
                'order_id': request.order_id,
                'reference': reference,
                'amount': request.amount,
                'currency': 'NOK',
                'payment_method': 'vipps',
                'payment_status': 'CREATED',
                'created_at': datetime.now(timezone.utc).isoformat()
            })
            
            return {
                "redirect_url": payment_data["redirectUrl"],
                "payment_reference": reference
            }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Vipps initiation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@api_router.get("/payments/vipps/{reference}/status")
async def get_vipps_payment_status(reference: str):
    """Check the status of a Vipps payment"""
    try:
        access_token = await vipps_token_manager.get_access_token()
        vipps_api_url = os.environ.get('VIPPS_API_URL', 'https://apitest.vipps.no')
        vipps_subscription_key = os.environ.get('VIPPS_SUBSCRIPTION_KEY')
        vipps_msn = os.environ.get('VIPPS_MSN')
        
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{vipps_api_url}/epayment/v1/payments/{reference}",
                headers={
                    "Authorization": f"Bearer {access_token}",
                    "Ocp-Apim-Subscription-Key": vipps_subscription_key,
                    "Merchant-Serial-Number": vipps_msn,
                    "Vipps-System-Name": "Firmaprint",
                    "Vipps-System-Version": "1.0.0",
                },
            )
            
            if response.status_code != 200:
                raise HTTPException(status_code=404, detail="Betaling ikke funnet")
            
            payment_data = response.json()
            
            # Update payment status in DB
            await db.payment_transactions.update_one(
                {'reference': reference},
                {'$set': {
                    'payment_status': payment_data["state"],
                    'updated_at': datetime.now(timezone.utc).isoformat()
                }}
            )
            
            return {
                "status": payment_data["state"],
                "authorized_amount": payment_data.get("aggregate", {}).get("authorizedAmount"),
                "captured_amount": payment_data.get("aggregate", {}).get("capturedAmount"),
            }
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Vipps status error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@api_router.post("/payments/vipps/{reference}/capture")
async def capture_vipps_payment(reference: str):
    """Capture an authorized Vipps payment"""
    try:
        # Get payment info
        payment = await db.payment_transactions.find_one({'reference': reference}, {'_id': 0})
        if not payment:
            raise HTTPException(status_code=404, detail="Betaling ikke funnet")
        
        access_token = await vipps_token_manager.get_access_token()
        vipps_api_url = os.environ.get('VIPPS_API_URL', 'https://apitest.vipps.no')
        vipps_subscription_key = os.environ.get('VIPPS_SUBSCRIPTION_KEY')
        vipps_msn = os.environ.get('VIPPS_MSN')
        
        capture_payload = {
            "modificationAmount": {
                "currency": "NOK",
                "value": payment['amount']
            }
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{vipps_api_url}/epayment/v1/payments/{reference}/capture",
                json=capture_payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {access_token}",
                    "Ocp-Apim-Subscription-Key": vipps_subscription_key,
                    "Merchant-Serial-Number": vipps_msn,
                    "Idempotency-Key": str(uuid.uuid4()),
                    "Vipps-System-Name": "Firmaprint",
                    "Vipps-System-Version": "1.0.0",
                },
            )
            
            if response.status_code != 200:
                logger.error(f"Vipps capture error: {response.text}")
                raise HTTPException(status_code=400, detail="Kunne ikke fullføre betaling")
            
            capture_data = response.json()
            
            # Update payment status
            await db.payment_transactions.update_one(
                {'reference': reference},
                {'$set': {
                    'payment_status': 'CAPTURED',
                    'captured_amount': capture_data["aggregate"]["capturedAmount"]["value"],
                    'updated_at': datetime.now(timezone.utc).isoformat()
                }}
            )
            
            # Update order status
            await db.orders.update_one(
                {'vipps_reference': reference},
                {'$set': {'payment_status': 'paid', 'status': 'processing'}}
            )
            
            return {"success": True, "captured_amount": capture_data["aggregate"]["capturedAmount"]}
    
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Vipps capture error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# ==================== SEED DATA ====================

@api_router.post("/seed")
async def seed_database():
    """Seed database with Tracker products"""
    from tracker_products import tracker_products
    
    # Clear existing products
    await db.products.delete_many({})
    
    # Add ID and timestamp to each product
    products_with_ids = []
    for product in tracker_products:
        product_copy = product.copy()
        product_copy["id"] = str(uuid.uuid4())
        product_copy["created_at"] = datetime.now(timezone.utc).isoformat()
        products_with_ids.append(product_copy)
    
    await db.products.insert_many(products_with_ids)
    
    return {"message": f"Lagt til {len(products_with_ids)} Tracker-produkter", "count": len(products_with_ids)}

# Root endpoint
@api_router.get("/")
async def root():
    return {"message": "Firmaprint.no API", "version": "1.0.0"}

# Include router
app.include_router(api_router)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=os.environ.get('CORS_ORIGINS', '*').split(','),
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
