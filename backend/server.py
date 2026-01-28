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
    payment_method: str  # stripe, invoice
    payment_status: str = "pending"
    stripe_session_id: Optional[str] = None
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

# ==================== PRICING LOGIC ====================

def calculate_design_price(design: DesignObject, quantity: int) -> float:
    """Calculate price for design/print based on method, size, and quantity"""
    base_price = 0
    area_cm2 = design.width_cm * design.height_cm
    
    if design.print_method == "embroidery":
        # Embroidery pricing based on complexity and size
        complexity_multiplier = {"simple": 0.8, "normal": 1.0, "detailed": 1.5}
        multiplier = complexity_multiplier.get(design.complexity, 1.0)
        base_price = (area_cm2 * 2.5) * multiplier  # NOK per cm² for embroidery
        
        # Setup cost (divided by quantity)
        setup_cost = 200 / quantity if quantity > 0 else 200
        base_price += setup_cost
        
    else:  # print
        # Print pricing based on colors and size
        color_count = len(design.colors) if design.colors else 1
        base_price = area_cm2 * 1.2 * color_count  # NOK per cm² per color
        
        # Setup cost (divided by quantity)
        setup_cost = 150 / quantity if quantity > 0 else 150
        base_price += setup_cost
    
    # Quantity discount
    if quantity >= 100:
        base_price *= 0.6
    elif quantity >= 50:
        base_price *= 0.7
    elif quantity >= 25:
        base_price *= 0.8
    elif quantity >= 10:
        base_price *= 0.9
    
    return round(base_price, 2)

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
    total = subtotal + design_total
    
    # Update cart
    updated_cart = {
        'id': cart.get('id', str(uuid.uuid4())),
        'user_id': cart.get('user_id'),
        'session_id': session_id,
        'items': items,
        'subtotal': round(subtotal, 2),
        'design_total': round(design_total, 2),
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
    total = subtotal + design_total
    
    cart['items'] = items
    cart['subtotal'] = round(subtotal, 2)
    cart['design_total'] = round(design_total, 2)
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

@api_router.post("/pricing/calculate")
async def calculate_pricing(
    print_method: str,
    width_cm: float,
    height_cm: float,
    quantity: int,
    colors: List[str] = [],
    complexity: str = "normal"
):
    """Calculate price for design/print"""
    design = DesignObject(
        logo_url="",
        logo_preview="",
        position_x=0,
        position_y=0,
        scale=1,
        rotation=0,
        view="front",
        print_area="chest",
        print_method=print_method,
        width_cm=width_cm,
        height_cm=height_cm,
        colors=colors,
        complexity=complexity
    )
    
    price_per_item = calculate_design_price(design, quantity)
    total_price = price_per_item * quantity
    
    return {
        "price_per_item": round(price_per_item, 2),
        "total_price": round(total_price, 2),
        "quantity": quantity,
        "breakdown": {
            "method": print_method,
            "area_cm2": round(width_cm * height_cm, 2),
            "colors": len(colors) if colors else 1,
            "complexity": complexity
        }
    }

# ==================== SEED DATA ====================

@api_router.post("/seed")
async def seed_database():
    """Seed database with sample products"""
    # Clear existing products
    await db.products.delete_many({})
    
    sample_products = [
        {
            "id": str(uuid.uuid4()),
            "name": "Premium T-skjorte",
            "slug": "premium-t-skjorte",
            "description": "Høykvalitets bomullst-skjorte, perfekt for trykk og brodering. 100% ringspunnet bomull for en myk følelse.",
            "category": "tshirts",
            "brand": "Firmaprint Basics",
            "base_price": 149.0,
            "variants": [
                {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1581655353564-df123a1eb820?w=600"], "stock": {}},
                {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1503341504253-dff4815485f1?w=600"], "stock": {}},
                {"color": "Navy", "color_hex": "#0F172A", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600"], "stock": {}}
            ],
            "print_methods": ["print", "embroidery"],
            "print_areas": [
                {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 20, "width": 25, "height": 25, "max_width_cm": 8, "max_height_cm": 8},
                {"name": "center_chest", "name_no": "Midt bryst", "x": 30, "y": 20, "width": 40, "height": 30, "max_width_cm": 25, "max_height_cm": 20},
                {"name": "full_back", "name_no": "Rygg", "x": 20, "y": 15, "width": 60, "height": 50, "max_width_cm": 35, "max_height_cm": 40}
            ],
            "materials": ["100% bomull"],
            "fit": "Regular",
            "delivery_days": 5,
            "best_for": ["event", "team", "casual"],
            "min_quantity": 1,
            "featured": True,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Klassisk Hoodie",
            "slug": "klassisk-hoodie",
            "description": "Varm og komfortabel hoodie med hette og lomme foran. Perfekt for brodert logo.",
            "category": "hoodies",
            "brand": "Firmaprint Premium",
            "base_price": 399.0,
            "variants": [
                {"color": "Sort", "color_hex": "#000000", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://images.pexels.com/photos/7688469/pexels-photo-7688469.jpeg?w=600"], "stock": {}},
                {"color": "Grå", "color_hex": "#6B7280", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600"], "stock": {}},
                {"color": "Navy", "color_hex": "#0F172A", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1578681994506-b8f463449011?w=600"], "stock": {}}
            ],
            "print_methods": ["print", "embroidery"],
            "print_areas": [
                {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 25, "width": 20, "height": 20, "max_width_cm": 8, "max_height_cm": 8},
                {"name": "center_chest", "name_no": "Midt bryst", "x": 25, "y": 20, "width": 50, "height": 35, "max_width_cm": 30, "max_height_cm": 25},
                {"name": "full_back", "name_no": "Rygg", "x": 15, "y": 10, "width": 70, "height": 55, "max_width_cm": 40, "max_height_cm": 45}
            ],
            "materials": ["80% bomull", "20% polyester"],
            "fit": "Regular",
            "delivery_days": 7,
            "best_for": ["team", "workwear", "casual"],
            "min_quantity": 1,
            "featured": True,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Snapback Caps",
            "slug": "snapback-caps",
            "description": "Klassisk snapback caps med flat skjerm. Ideell for brodert logo.",
            "category": "caps",
            "brand": "Firmaprint Headwear",
            "base_price": 179.0,
            "variants": [
                {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://images.pexels.com/photos/12025472/pexels-photo-12025472.jpeg?w=600"], "stock": {}},
                {"color": "Navy", "color_hex": "#0F172A", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=600"], "stock": {}},
                {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1534215754734-18e55d13e346?w=600"], "stock": {}}
            ],
            "print_methods": ["embroidery"],
            "print_areas": [
                {"name": "front", "name_no": "Front", "x": 25, "y": 30, "width": 50, "height": 30, "max_width_cm": 10, "max_height_cm": 6},
                {"name": "side", "name_no": "Side", "x": 75, "y": 40, "width": 20, "height": 20, "max_width_cm": 4, "max_height_cm": 4}
            ],
            "materials": ["100% akryl"],
            "fit": "Adjustable",
            "delivery_days": 5,
            "best_for": ["team", "event", "promo"],
            "min_quantity": 10,
            "featured": True,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Softshell Jakke",
            "slug": "softshell-jakke",
            "description": "Vannavstøtende softshell jakke med fleece-fôr. Perfekt for utendørs arbeid og aktiviteter.",
            "category": "jackets",
            "brand": "Firmaprint Pro",
            "base_price": 699.0,
            "variants": [
                {"color": "Sort", "color_hex": "#000000", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.pexels.com/photos/3763234/pexels-photo-3763234.jpeg?w=600"], "stock": {}},
                {"color": "Navy", "color_hex": "#0F172A", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1544923246-77307dd628b5?w=600"], "stock": {}}
            ],
            "print_methods": ["embroidery", "print"],
            "print_areas": [
                {"name": "left_chest", "name_no": "Venstre bryst", "x": 10, "y": 20, "width": 20, "height": 15, "max_width_cm": 8, "max_height_cm": 6},
                {"name": "back_top", "name_no": "Rygg øvre", "x": 25, "y": 10, "width": 50, "height": 20, "max_width_cm": 25, "max_height_cm": 10},
                {"name": "sleeve", "name_no": "Erme", "x": 85, "y": 35, "width": 12, "height": 15, "max_width_cm": 5, "max_height_cm": 6}
            ],
            "materials": ["94% polyester", "6% elastan"],
            "fit": "Regular",
            "delivery_days": 10,
            "best_for": ["workwear", "outdoor", "team"],
            "min_quantity": 5,
            "featured": True,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Arbeidsjakke Hi-Vis",
            "slug": "arbeidsjakke-hi-vis",
            "description": "EN ISO 20471 godkjent arbeidsjakke med høy synlighet. For profesjonelle.",
            "category": "workwear",
            "brand": "Firmaprint Safety",
            "base_price": 899.0,
            "variants": [
                {"color": "Gul/Navy", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=600"], "stock": {}},
                {"color": "Oransje/Navy", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1581092162384-8987c1d64926?w=600"], "stock": {}}
            ],
            "print_methods": ["embroidery", "print"],
            "print_areas": [
                {"name": "left_chest", "name_no": "Venstre bryst", "x": 10, "y": 25, "width": 18, "height": 12, "max_width_cm": 7, "max_height_cm": 5},
                {"name": "back", "name_no": "Rygg", "x": 20, "y": 15, "width": 60, "height": 40, "max_width_cm": 30, "max_height_cm": 20}
            ],
            "materials": ["100% polyester"],
            "fit": "Regular",
            "delivery_days": 14,
            "best_for": ["workwear", "safety", "construction"],
            "min_quantity": 5,
            "featured": False,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Polo Skjorte",
            "slug": "polo-skjorte",
            "description": "Klassisk polo i pique-kvalitet. Elegant og profesjonell for kontor og events.",
            "category": "tshirts",
            "brand": "Firmaprint Classic",
            "base_price": 249.0,
            "variants": [
                {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1625910513413-5fc51d87c6c3?w=600"], "stock": {}},
                {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=600"], "stock": {}},
                {"color": "Navy", "color_hex": "#0F172A", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1598032895397-b9472444bf93?w=600"], "stock": {}}
            ],
            "print_methods": ["embroidery"],
            "print_areas": [
                {"name": "left_chest", "name_no": "Venstre bryst", "x": 12, "y": 22, "width": 22, "height": 18, "max_width_cm": 8, "max_height_cm": 6},
                {"name": "sleeve", "name_no": "Erme", "x": 80, "y": 25, "width": 15, "height": 12, "max_width_cm": 5, "max_height_cm": 4}
            ],
            "materials": ["100% bomull pique"],
            "fit": "Classic",
            "delivery_days": 7,
            "best_for": ["corporate", "event", "hospitality"],
            "min_quantity": 1,
            "featured": True,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Totebag",
            "slug": "totebag",
            "description": "Miljøvennlig bomullsbag med lange håndtak. Ideell for messe og event.",
            "category": "accessories",
            "brand": "Firmaprint Eco",
            "base_price": 79.0,
            "variants": [
                {"color": "Natur", "color_hex": "#F5F5DC", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1597633544424-4da83d50be55?w=600"], "stock": {}},
                {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1605518215813-6e3c7debd1fc?w=600"], "stock": {}}
            ],
            "print_methods": ["print"],
            "print_areas": [
                {"name": "front", "name_no": "Front", "x": 15, "y": 20, "width": 70, "height": 60, "max_width_cm": 28, "max_height_cm": 30}
            ],
            "materials": ["100% økologisk bomull"],
            "fit": "One Size",
            "delivery_days": 5,
            "best_for": ["event", "promo", "eco"],
            "min_quantity": 25,
            "featured": False,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        },
        {
            "id": str(uuid.uuid4()),
            "name": "Fleece Genser",
            "slug": "fleece-genser",
            "description": "Varm fleece genser med glidelås i halsen. Perfekt som mellomlag.",
            "category": "hoodies",
            "brand": "Firmaprint Outdoor",
            "base_price": 349.0,
            "variants": [
                {"color": "Sort", "color_hex": "#000000", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1614975059251-992f11792f9a?w=600"], "stock": {}},
                {"color": "Navy", "color_hex": "#0F172A", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600"], "stock": {}},
                {"color": "Grå", "color_hex": "#6B7280", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1578681041175-9717c16b0d7c?w=600"], "stock": {}}
            ],
            "print_methods": ["embroidery"],
            "print_areas": [
                {"name": "left_chest", "name_no": "Venstre bryst", "x": 12, "y": 20, "width": 20, "height": 18, "max_width_cm": 8, "max_height_cm": 7}
            ],
            "materials": ["100% polyester fleece"],
            "fit": "Regular",
            "delivery_days": 7,
            "best_for": ["outdoor", "workwear", "team"],
            "min_quantity": 1,
            "featured": False,
            "active": True,
            "created_at": datetime.now(timezone.utc).isoformat()
        }
    ]
    
    await db.products.insert_many(sample_products)
    
    return {"message": f"Lagt til {len(sample_products)} produkter", "count": len(sample_products)}

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
