"""
Seed script for Tracker products
Based on https://www.tracker.no/ catalog with 10%+ margin pricing
Using reliable image sources
"""

tracker_products = [
    # ==================== T-SHIRTS ====================
    {
        "name": "Tracker 1010 Original T-Shirt",
        "slug": "tracker-1010-original-t-shirt",
        "description": "Klassisk t-skjorte i 100% bomull. Behagelig og slitesterk med god passform. Ideell for trykk og brodering.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 119.0,
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=600"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1503341504253-dff4815485f1?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1618354691373-d851c5c3a990?w=600"], "stock": {}},
            {"color": "Rød", "color_hex": "#DC2626", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1562157873-818bc0726f68?w=600"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=600"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 25, "width": 18, "height": 15, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 30, "y": 22, "width": 40, "height": 28, "max_width_cm": 25, "max_height_cm": 20},
            {"name": "full_back", "name_no": "Rygg", "x": 25, "y": 20, "width": 50, "height": 45, "max_width_cm": 35, "max_height_cm": 40}
        ],
        "materials": ["100% bomull, 150g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["event", "team", "promo"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    {
        "name": "Tracker 1012 Original Slim-T Dame",
        "slug": "tracker-1012-original-slim-t",
        "description": "Slim-fit t-skjorte for damer i myk bomull. Feminin passform med smale ermer.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 129.0,
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["https://images.unsplash.com/photo-1554568218-0f1715e72254?w=600"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["https://images.unsplash.com/photo-1576566588028-4147f3842f27?w=600"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 28, "width": 16, "height": 14, "max_width_cm": 7, "max_height_cm": 7},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 30, "y": 25, "width": 40, "height": 26, "max_width_cm": 22, "max_height_cm": 18},
        ],
        "materials": ["100% bomull, 150g/m²"],
        "fit": "Slim fit",
        "delivery_days": 5,
        "best_for": ["event", "team", "corporate"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    {
        "name": "Tracker 1200 Cool Dry T-Shirt",
        "slug": "tracker-1200-cool-dry-t-shirt",
        "description": "Teknisk trenings t-skjorte med fukttransporterende egenskaper. Perfekt for aktiv bruk og sport.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 149.0,
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1571945153237-4929e783af4a?w=600"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1618517351616-38fb9c5210c6?w=600"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1581655353564-df123a1eb820?w=600"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 25, "width": 18, "height": 15, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 28, "y": 22, "width": 44, "height": 28, "max_width_cm": 25, "max_height_cm": 20},
        ],
        "materials": ["100% polyester, 135g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["sport", "team", "trening"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    
    # ==================== PIQUE / POLO ====================
    {
        "name": "Tracker 2010 Original Pique",
        "slug": "tracker-2010-original-pique",
        "description": "Klassisk pique polo i 100% bomull. Profesjonell og komfortabel med ribbestrikket krage.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 229.0,
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1625910513413-5fc51d87c6c3?w=600"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1594938298603-c8148c4dae35?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1598032895397-b9472444bf93?w=600"], "stock": {}},
            {"color": "Lysblå", "color_hex": "#93C5FD", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1589310243389-96a5483213a8?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 30, "width": 16, "height": 14, "max_width_cm": 8, "max_height_cm": 7},
            {"name": "sleeve", "name_no": "Erme", "x": 8, "y": 32, "width": 14, "height": 12, "max_width_cm": 5, "max_height_cm": 4}
        ],
        "materials": ["100% bomull pique, 210g/m²"],
        "fit": "Classic",
        "delivery_days": 5,
        "best_for": ["corporate", "event", "hospitality"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    
    # ==================== SWEATSHIRTS & HOODIES ====================
    {
        "name": "Tracker 3010 Original Sweat",
        "slug": "tracker-3010-original-sweat",
        "description": "Klassisk sweatshirt i børstet bomullsmix. Mykt innside og god varme.",
        "category": "hoodies",
        "brand": "Tracker",
        "base_price": 329.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1572495532056-8583af1cbae0?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1578681994506-b8f463449011?w=600"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 25, "width": 16, "height": 14, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 26, "y": 22, "width": 48, "height": 30, "max_width_cm": 30, "max_height_cm": 25},
            {"name": "full_back", "name_no": "Rygg", "x": 20, "y": 18, "width": 60, "height": 50, "max_width_cm": 40, "max_height_cm": 40}
        ],
        "materials": ["80% bomull, 20% polyester, 280g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["team", "casual", "workwear"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    {
        "name": "Tracker 3065 Original Hood",
        "slug": "tracker-3065-original-hood",
        "description": "Klassisk hoodie med kengurulomme og justerbar hette. Myk innside og god passform.",
        "category": "hoodies",
        "brand": "Tracker",
        "base_price": 449.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.pexels.com/photos/7688469/pexels-photo-7688469.jpeg?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=600"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1509942774463-acf339cf87d5?w=600"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=600"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 32, "width": 16, "height": 12, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 26, "y": 28, "width": 48, "height": 28, "max_width_cm": 30, "max_height_cm": 25},
            {"name": "full_back", "name_no": "Rygg", "x": 20, "y": 22, "width": 60, "height": 48, "max_width_cm": 40, "max_height_cm": 40}
        ],
        "materials": ["80% bomull, 20% polyester, 280g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["team", "casual", "russ"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    {
        "name": "Tracker 3066 Original Hood Jacket",
        "slug": "tracker-3066-original-hood-jacket",
        "description": "Hoodie jakke med full glidelås og to sidelommer. Allsidig og behagelig.",
        "category": "hoodies",
        "brand": "Tracker",
        "base_price": 499.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1578681994506-b8f463449011?w=600"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 55, "y": 30, "width": 16, "height": 12, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "full_back", "name_no": "Rygg", "x": 20, "y": 20, "width": 60, "height": 50, "max_width_cm": 40, "max_height_cm": 40}
        ],
        "materials": ["80% bomull, 20% polyester, 280g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["team", "casual", "russ"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    
    # ==================== FLEECE ====================
    {
        "name": "Tracker 4020 Ultrafleece Jacket",
        "slug": "tracker-4020-ultrafleece-jacket",
        "description": "Lett og myk fleece jakke med full glidelås. Perfekt som mellomlag eller alene på milde dager.",
        "category": "hoodies",
        "brand": "Tracker",
        "base_price": 399.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1614975059251-992f11792f9a?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1578681041175-9717c16b0d7c?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 55, "y": 25, "width": 16, "height": 12, "max_width_cm": 8, "max_height_cm": 7},
        ],
        "materials": ["100% polyester fleece, 200g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["outdoor", "workwear", "team"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    {
        "name": "Tracker 4040 Knitted Fleece Jacket",
        "slug": "tracker-4040-knitted-fleece-jacket",
        "description": "Moderne strikket fleece jakke med kontrast glidelås. Stilfull og varm.",
        "category": "hoodies",
        "brand": "Tracker",
        "base_price": 549.0,
        "variants": [
            {"color": "Mørk Grå Melert", "color_hex": "#6B7280", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=600"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1517940310602-26535839e6d8?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 55, "y": 28, "width": 16, "height": 12, "max_width_cm": 8, "max_height_cm": 7},
        ],
        "materials": ["100% polyester strikket fleece, 280g/m²"],
        "fit": "Regular",
        "delivery_days": 7,
        "best_for": ["outdoor", "corporate", "casual"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    
    # ==================== JAKKER ====================
    {
        "name": "Tracker 5040 Softshell Jacket",
        "slug": "tracker-5040-softshell-jacket",
        "description": "3-lags softshell jakke med vannavstøtende overflate og fleece-innside. Vindtett og pustende.",
        "category": "jackets",
        "brand": "Tracker",
        "base_price": 749.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.pexels.com/photos/3763234/pexels-photo-3763234.jpeg?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1544923246-77307dd628b5?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 55, "y": 25, "width": 14, "height": 12, "max_width_cm": 8, "max_height_cm": 6},
            {"name": "back", "name_no": "Rygg", "x": 22, "y": 20, "width": 56, "height": 45, "max_width_cm": 30, "max_height_cm": 25},
            {"name": "sleeve", "name_no": "Erme", "x": 5, "y": 35, "width": 12, "height": 14, "max_width_cm": 5, "max_height_cm": 6}
        ],
        "materials": ["94% polyester, 6% elastan"],
        "fit": "Regular",
        "delivery_days": 7,
        "best_for": ["outdoor", "workwear", "team"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    {
        "name": "Tracker 7050 Lightweight Down Jacket",
        "slug": "tracker-7050-lightweight-down-jacket",
        "description": "Ultralett dunjakke som kan pakkes i egen lomme. Perfekt som ekstra lag.",
        "category": "jackets",
        "brand": "Tracker",
        "base_price": 1199.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1551028719-00167b16eac5?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1548883354-94bcfe321cbb?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 55, "y": 25, "width": 14, "height": 10, "max_width_cm": 7, "max_height_cm": 5},
        ],
        "materials": ["100% nylon, dun-/fjærfyll 90/10"],
        "fit": "Regular",
        "delivery_days": 10,
        "best_for": ["outdoor", "travel", "casual"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    
    # ==================== CAPS ====================
    {
        "name": "Tracker 6000 Original Cap",
        "slug": "tracker-6000-original-cap",
        "description": "Klassisk 6-panels caps i bomull med børstet innside. Justerbar stropp bak.",
        "category": "caps",
        "brand": "Tracker",
        "base_price": 149.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1534215754734-18e55d13e346?w=600"], "stock": {}},
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["One Size"], "images": ["https://images.pexels.com/photos/12025472/pexels-photo-12025472.jpeg?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 25, "y": 30, "width": 50, "height": 28, "max_width_cm": 10, "max_height_cm": 6},
        ],
        "materials": ["100% bomull"],
        "fit": "Adjustable",
        "delivery_days": 5,
        "best_for": ["team", "event", "promo"],
        "min_quantity": 10,
        "featured": True,
        "active": True
    },
    {
        "name": "Tracker 6820 Original Beanie",
        "slug": "tracker-6820-original-beanie",
        "description": "Klassisk strikket lue i akryl med dobbel lag for ekstra varme.",
        "category": "caps",
        "brand": "Tracker",
        "base_price": 119.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?w=600"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1510598969022-c4c6c5d05769?w=600"], "stock": {}},
            {"color": "Grå", "color_hex": "#6B7280", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1607672632458-9eb56696346b?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 30, "y": 35, "width": 40, "height": 25, "max_width_cm": 8, "max_height_cm": 5},
        ],
        "materials": ["100% akryl"],
        "fit": "One Size",
        "delivery_days": 5,
        "best_for": ["outdoor", "team", "winter"],
        "min_quantity": 10,
        "featured": False,
        "active": True
    },
    
    # ==================== ARBEIDSKLÆR ====================
    {
        "name": "Tracker 1213 Hi-Vis T-Shirt",
        "slug": "tracker-1213-hi-vis-t-shirt",
        "description": "Fluoriserende t-skjorte i synlighetsklasse 2 etter EN ISO20471. Teknisk materiale med god fuktavledning.",
        "category": "workwear",
        "brand": "Tracker",
        "base_price": 199.0,
        "variants": [
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=600"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1581092162384-8987c1d64926?w=600"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 22, "width": 16, "height": 12, "max_width_cm": 7, "max_height_cm": 6},
            {"name": "back", "name_no": "Rygg", "x": 25, "y": 25, "width": 50, "height": 35, "max_width_cm": 25, "max_height_cm": 18},
        ],
        "materials": ["100% polyester, 135g/m²"],
        "fit": "Regular",
        "delivery_days": 7,
        "best_for": ["workwear", "safety", "construction"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    {
        "name": "Tracker 4013 Hi-Vis Fleece Jacket",
        "slug": "tracker-4013-hi-vis-fleece-jacket",
        "description": "Synlig fleece jakke i klasse 3 etter EN ISO20471. Varm og funksjonell arbeidsjakke.",
        "category": "workwear",
        "brand": "Tracker",
        "base_price": 649.0,
        "variants": [
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=600"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1581092162384-8987c1d64926?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 55, "y": 22, "width": 14, "height": 12, "max_width_cm": 7, "max_height_cm": 5},
            {"name": "back", "name_no": "Rygg", "x": 22, "y": 25, "width": 56, "height": 38, "max_width_cm": 30, "max_height_cm": 20}
        ],
        "materials": ["100% polyester fleece"],
        "fit": "Regular",
        "delivery_days": 10,
        "best_for": ["workwear", "safety", "construction"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    {
        "name": "Tracker 3013 Hi-Vis Crewneck",
        "slug": "tracker-3013-hi-vis-crewneck",
        "description": "Synlig sweatshirt i klasse 3 etter EN ISO20471. Behagelig arbeidsgenser.",
        "category": "workwear",
        "brand": "Tracker",
        "base_price": 449.0,
        "variants": [
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=600"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://images.unsplash.com/photo-1581092162384-8987c1d64926?w=600"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 52, "y": 18, "width": 16, "height": 14, "max_width_cm": 7, "max_height_cm": 6},
            {"name": "back", "name_no": "Rygg", "x": 22, "y": 22, "width": 56, "height": 40, "max_width_cm": 30, "max_height_cm": 20}
        ],
        "materials": ["80% bomull, 20% polyester, 280g/m²"],
        "fit": "Regular",
        "delivery_days": 7,
        "best_for": ["workwear", "safety", "construction"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    
    # ==================== TILBEHØR ====================
    {
        "name": "Tracker Tote Bag",
        "slug": "tracker-tote-bag",
        "description": "Miljøvennlig bomullsbag med lange håndtak. Ideell for messe og event.",
        "category": "accessories",
        "brand": "Tracker",
        "base_price": 79.0,
        "variants": [
            {"color": "Natur", "color_hex": "#F5F5DC", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1597633544424-4da83d50be55?w=600"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://images.unsplash.com/photo-1605518215813-6e3c7debd1fc?w=600"], "stock": {}},
        ],
        "print_methods": ["print"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 18, "y": 22, "width": 64, "height": 50, "max_width_cm": 28, "max_height_cm": 30}
        ],
        "materials": ["100% økologisk bomull"],
        "fit": "One Size",
        "delivery_days": 5,
        "best_for": ["event", "promo", "eco"],
        "min_quantity": 25,
        "featured": False,
        "active": True
    },
]
