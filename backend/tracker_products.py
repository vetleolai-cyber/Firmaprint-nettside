"""
Seed script for Tracker products
Based on https://www.tracker.no/ catalog with 10%+ margin pricing
Using local product images from tracker.no
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
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/1010_tshirt_white.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/1010_original_tshirt_black.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/1010_original_tshirt_black.jpg"], "stock": {}},
            {"color": "Rød", "color_hex": "#DC2626", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["/images/products/1010_original_tshirt_black.jpg"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["/images/products/1010_original_tshirt_black.jpg"], "stock": {}},
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
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["/images/products/1012_slim_t_navy.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["/images/products/1012_slim_t_navy.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["/images/products/1012_slim_t_navy.jpg"], "stock": {}},
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
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["/images/products/1200_cool_dry_white.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["/images/products/1200_cool_dry_white.jpg"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["/images/products/1200_cool_dry_blue.jpg"], "stock": {}},
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
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/2010_pique_white.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/2010_pique_black.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/2010_pique_black.jpg"], "stock": {}},
            {"color": "Lysblå", "color_hex": "#93C5FD", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["/images/products/2010_pique_white.jpg"], "stock": {}},
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3010_sweat_navy.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3010_sweat_navy.jpg"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3010_sweat_navy.jpg"], "stock": {}},
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3065_hood_navy.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3065_hood_navy.jpg"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3065_hood_navy.jpg"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["/images/products/3065_hood_navy.jpg"], "stock": {}},
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3066_hood_jacket.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3066_hood_jacket.jpg"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3066_hood_jacket.jpg"], "stock": {}},
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/4020_ultrafleece.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/4020_ultrafleece.jpg"], "stock": {}},
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
            {"color": "Mørk Grå Melert", "color_hex": "#6B7280", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/4040_knitted_fleece.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/4040_knitted_fleece.jpg"], "stock": {}},
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
        "name": "Tracker 7085 Active Softshell",
        "slug": "tracker-7085-active-softshell",
        "description": "3-lags softshell jakke med vannavstøtende overflate og fleece-innside. Vindtett og pustende.",
        "category": "jackets",
        "brand": "Tracker",
        "base_price": 749.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/7085_softshell.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/7085_softshell.jpg"], "stock": {}},
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
        "name": "Tracker 7077 Superlight Down Jacket",
        "slug": "tracker-7077-superlight-down-jacket",
        "description": "Ultralett dunjakke som kan pakkes i egen lomme. Perfekt som ekstra lag.",
        "category": "jackets",
        "brand": "Tracker",
        "base_price": 1199.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/7077_superlight_down.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/7077_superlight_down.jpg"], "stock": {}},
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
    {
        "name": "Tracker 7075 Original Down Jacket",
        "slug": "tracker-7075-original-down-jacket",
        "description": "Klassisk dunjakke med god varme og lett vekt. Ideell for kalde dager.",
        "category": "jackets",
        "brand": "Tracker",
        "base_price": 1099.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/7075_down_jacket.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/7075_down_jacket.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 55, "y": 25, "width": 14, "height": 10, "max_width_cm": 7, "max_height_cm": 5},
        ],
        "materials": ["100% nylon, dun-/fjærfyll 80/20"],
        "fit": "Regular",
        "delivery_days": 10,
        "best_for": ["outdoor", "travel", "casual"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    
    # ==================== CAPS ====================
    {
        "name": "Tracker 6010 Original Baseball Cap",
        "slug": "tracker-6010-original-cap",
        "description": "Klassisk 6-panels caps i bomull med børstet innside. Justerbar stropp bak.",
        "category": "caps",
        "brand": "Tracker",
        "base_price": 149.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["/images/products/6010_cap.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["One Size"], "images": ["/images/products/6010_cap.jpg"], "stock": {}},
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["One Size"], "images": ["/images/products/6010_cap.jpg"], "stock": {}},
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
        "name": "Tracker 6150 Original Beanie",
        "slug": "tracker-6150-original-beanie",
        "description": "Klassisk strikket lue i akryl med dobbel lag for ekstra varme.",
        "category": "caps",
        "brand": "Tracker",
        "base_price": 119.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["/images/products/6150_beanie.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["One Size"], "images": ["/images/products/6150_beanie.jpg"], "stock": {}},
            {"color": "Grå", "color_hex": "#6B7280", "sizes": ["One Size"], "images": ["/images/products/6150_beanie.jpg"], "stock": {}},
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
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/1213_hivis_tshirt.jpg"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/1213_hivis_tshirt.jpg"], "stock": {}},
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
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/4013_hivis_fleece.jpg"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/4013_hivis_fleece.jpg"], "stock": {}},
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
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3013_hivis_crewneck.jpg"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["/images/products/3013_hivis_crewneck.jpg"], "stock": {}},
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
        "name": "Tracker Original Duffel Bag",
        "slug": "tracker-duffel-bag",
        "description": "Slitesterk duffel bag med stor hovedlomme. Ideell for trening og reise.",
        "category": "accessories",
        "brand": "Tracker",
        "base_price": 599.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["/images/products/9167_duffel_bag.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["One Size"], "images": ["/images/products/9167_duffel_bag.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 18, "y": 22, "width": 64, "height": 50, "max_width_cm": 28, "max_height_cm": 30}
        ],
        "materials": ["100% polyester"],
        "fit": "One Size",
        "delivery_days": 5,
        "best_for": ["event", "promo", "sport"],
        "min_quantity": 10,
        "featured": False,
        "active": True
    },
]
