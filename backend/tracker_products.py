"""
Seed script for Tracker products
Based on https://www.tracker.no/ catalog with 10%+ margin pricing
"""

tracker_products = [
    # ==================== T-SHIRTS ====================
    {
        "name": "Tracker 1010 Original T-Shirt",
        "slug": "tracker-1010-original-t-shirt",
        "description": "Klassisk t-skjorte i 100% bomull. Behagelig og slitesterk med god passform. Ideell for trykk og brodering.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 119.0,  # Zeproc ~98-105kr, margin ~15%
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/1010_00-2.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/1010_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/1010_05.jpg"], "stock": {}},
            {"color": "Rød", "color_hex": "#DC2626", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/1010_06.jpg"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/1010_08.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 20, "width": 20, "height": 20, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 30, "y": 18, "width": 40, "height": 30, "max_width_cm": 25, "max_height_cm": 20},
            {"name": "full_back", "name_no": "Rygg", "x": 20, "y": 15, "width": 60, "height": 50, "max_width_cm": 35, "max_height_cm": 40}
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
        "name": "Tracker 1012 Original Slim-T",
        "slug": "tracker-1012-original-slim-t",
        "description": "Slim-fit t-skjorte for damer i myk bomull. Feminin passform med smale ermer.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 129.0,
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1012_00.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1012_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1012_05.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 20, "width": 18, "height": 18, "max_width_cm": 7, "max_height_cm": 7},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 30, "y": 18, "width": 40, "height": 28, "max_width_cm": 22, "max_height_cm": 18},
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
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1200_00.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1200_04.jpg"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1200_08.jpg"], "stock": {}},
            {"color": "Rød", "color_hex": "#DC2626", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1200_06.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 20, "width": 20, "height": 20, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 30, "y": 18, "width": 40, "height": 30, "max_width_cm": 25, "max_height_cm": 20},
        ],
        "materials": ["100% polyester, 135g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["sport", "team", "trening"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    {
        "name": "Tracker 1213 Hi-Vis CoolDry T-Shirt",
        "slug": "tracker-1213-hi-vis-cooldry-t-shirt",
        "description": "Fluoriserende t-skjorte i synlighetsklasse 2 etter EN ISO20471. Teknisk materiale med god fuktavledning.",
        "category": "workwear",
        "brand": "Tracker",
        "base_price": 199.0,
        "variants": [
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1213.jpg"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/1213_37.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 22, "width": 18, "height": 15, "max_width_cm": 7, "max_height_cm": 6},
            {"name": "back", "name_no": "Rygg", "x": 25, "y": 20, "width": 50, "height": 35, "max_width_cm": 25, "max_height_cm": 18},
        ],
        "materials": ["100% polyester, 135g/m²"],
        "fit": "Regular",
        "delivery_days": 7,
        "best_for": ["workwear", "safety", "construction"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    
    # ==================== PIQUE ====================
    {
        "name": "Tracker 2010 Original Pique",
        "slug": "tracker-2010-original-pique",
        "description": "Klassisk pique polo i 100% bomull. Profesjonell og komfortabel med ribbestrikket krage.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 229.0,
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/03/2010_00.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/03/2010_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/03/2010_05.jpg"], "stock": {}},
            {"color": "Lysblå", "color_hex": "#93C5FD", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/03/2010_09.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 12, "y": 22, "width": 20, "height": 18, "max_width_cm": 8, "max_height_cm": 7},
            {"name": "sleeve", "name_no": "Erme", "x": 80, "y": 25, "width": 15, "height": 12, "max_width_cm": 5, "max_height_cm": 4}
        ],
        "materials": ["100% bomull pique, 210g/m²"],
        "fit": "Classic",
        "delivery_days": 5,
        "best_for": ["corporate", "event", "hospitality"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    {
        "name": "Tracker 2110 Cool Dry Sport Pique",
        "slug": "tracker-2110-cool-dry-sport-pique",
        "description": "Sporty pique polo med fukttransporterende egenskaper. Ideell for aktiv bruk og golf.",
        "category": "tshirts",
        "brand": "Tracker",
        "base_price": 259.0,
        "variants": [
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/2110_00.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/2110_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/2110_05.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 12, "y": 22, "width": 20, "height": 18, "max_width_cm": 8, "max_height_cm": 7},
        ],
        "materials": ["100% polyester, 150g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["sport", "golf", "corporate"],
        "min_quantity": 1,
        "featured": False,
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/3010_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/3010_05.jpg"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/3010_25.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 22, "width": 18, "height": 18, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 25, "y": 20, "width": 50, "height": 35, "max_width_cm": 30, "max_height_cm": 25},
            {"name": "full_back", "name_no": "Rygg", "x": 15, "y": 12, "width": 70, "height": 55, "max_width_cm": 40, "max_height_cm": 40}
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
        "name": "Tracker 3060 Original Sweat m/Zip",
        "slug": "tracker-3060-original-sweat-zip",
        "description": "Sweatshirt med glidelås i halsen. Praktisk og behagelig for hverdagsbruk.", 
        "category": "hoodies",
        "brand": "Tracker",
        "base_price": 429.0,  # Zeproc ~374-396kr, margin ~12%
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/3060_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/3060_05.jpg"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/3060_22.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 25, "width": 18, "height": 18, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "full_back", "name_no": "Rygg", "x": 15, "y": 12, "width": 70, "height": 55, "max_width_cm": 40, "max_height_cm": 40}
        ],
        "materials": ["80% bomull, 20% polyester, 280g/m²"],
        "fit": "Regular",
        "delivery_days": 5,
        "best_for": ["team", "casual", "workwear"],
        "min_quantity": 1,
        "featured": True,
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/3065_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/3065_05.jpg"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/3065_25.jpg"], "stock": {}},
            {"color": "Kongeblå", "color_hex": "#1D4ED8", "sizes": ["XS", "S", "M", "L", "XL", "XXL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/3065_08.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 28, "width": 18, "height": 18, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "center_chest", "name_no": "Midt bryst", "x": 25, "y": 25, "width": 50, "height": 35, "max_width_cm": 30, "max_height_cm": 25},
            {"name": "full_back", "name_no": "Rygg", "x": 15, "y": 15, "width": 70, "height": 55, "max_width_cm": 40, "max_height_cm": 40}
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/3066_04_f.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/3066_05_f.jpg"], "stock": {}},
            {"color": "Grå Melert", "color_hex": "#9CA3AF", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/02/3066_25_f.jpg"], "stock": {}},
        ],
        "print_methods": ["print", "embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 15, "y": 28, "width": 18, "height": 18, "max_width_cm": 8, "max_height_cm": 8},
            {"name": "full_back", "name_no": "Rygg", "x": 15, "y": 15, "width": 70, "height": 55, "max_width_cm": 40, "max_height_cm": 40}
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
        "name": "Tracker 4020 Original Ultrafleece Jacket",
        "slug": "tracker-4020-ultrafleece-jacket",
        "description": "Lett og myk fleece jakke med full glidelås. Perfekt som mellomlag eller alene på milde dager.",
        "category": "hoodies",
        "brand": "Tracker",
        "base_price": 399.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/4020_04_f.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/4020_05_f.jpg"], "stock": {}},
            {"color": "Mørk Grå", "color_hex": "#4B5563", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/4020_08_f.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 12, "y": 22, "width": 20, "height": 18, "max_width_cm": 8, "max_height_cm": 7},
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
            {"color": "Mørk Grå Melert", "color_hex": "#6B7280", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/4040_10.jpg"], "stock": {}},
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/12/4040_04.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 12, "y": 22, "width": 20, "height": 18, "max_width_cm": 8, "max_height_cm": 7},
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
        "name": "Tracker 5040 Original Softshell Jacket",
        "slug": "tracker-5040-softshell-jacket",
        "description": "3-lags softshell jakke med vannavstøtende overflate og fleece-innside. Vindtett og pustende.",
        "category": "jackets",
        "brand": "Tracker",
        "base_price": 749.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/5040_04_f.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/5040_05_f.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 10, "y": 22, "width": 18, "height": 15, "max_width_cm": 8, "max_height_cm": 6},
            {"name": "back", "name_no": "Rygg", "x": 20, "y": 12, "width": 60, "height": 45, "max_width_cm": 30, "max_height_cm": 25},
            {"name": "sleeve", "name_no": "Erme", "x": 82, "y": 30, "width": 12, "height": 15, "max_width_cm": 5, "max_height_cm": 6}
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
        "name": "Tracker 7073 Hybrid Down Stretch Jacket",
        "slug": "tracker-7073-hybrid-down-jacket",
        "description": "Lett og varm hybrid dunjakke med stretch-sider. Perfekt for aktiv bruk i kaldt vær.",
        "category": "jackets",
        "brand": "Tracker",
        "base_price": 1549.0,  # Zeproc ~1353-1497kr, margin ~10%
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2023/01/7073_04_f.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2023/01/7073_05_f.jpg"], "stock": {}},
            {"color": "Mørk Grå", "color_hex": "#4B5563", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2023/01/7073_10_f.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 10, "y": 22, "width": 18, "height": 12, "max_width_cm": 7, "max_height_cm": 5},
        ],
        "materials": ["100% nylon, dun-/fjærfyll"],
        "fit": "Regular",
        "delivery_days": 10,
        "best_for": ["outdoor", "ski", "premium"],
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/7050_04_f.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["XS", "S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/7050_05_f.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 10, "y": 22, "width": 18, "height": 12, "max_width_cm": 7, "max_height_cm": 5},
        ],
        "materials": ["100% nylon, dun-/fjærfyll 90/10"],
        "fit": "Regular",
        "delivery_days": 10,
        "best_for": ["outdoor", "travel", "casual"],
        "min_quantity": 1,
        "featured": False,
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
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6000_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["One Size"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6000_05.jpg"], "stock": {}},
            {"color": "Hvit", "color_hex": "#FFFFFF", "sizes": ["One Size"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6000_00.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 25, "y": 30, "width": 50, "height": 30, "max_width_cm": 10, "max_height_cm": 6},
            {"name": "side", "name_no": "Side", "x": 75, "y": 40, "width": 20, "height": 20, "max_width_cm": 4, "max_height_cm": 4}
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
        "name": "Tracker 6070 Winter Cap Fleece",
        "slug": "tracker-6070-winter-cap-fleece",
        "description": "Varm vintercaps med fleece-fôr og nedfellbare øreklaffer. Perfekt for kalde dager.",
        "category": "caps",
        "brand": "Tracker",
        "base_price": 229.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["S/M", "L/XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6070_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["S/M", "L/XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6070_05.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 25, "y": 25, "width": 50, "height": 25, "max_width_cm": 9, "max_height_cm": 5},
        ],
        "materials": ["100% polyester med fleece-fôr"],
        "fit": "S/M, L/XL",
        "delivery_days": 7,
        "best_for": ["outdoor", "workwear", "winter"],
        "min_quantity": 10,
        "featured": False,
        "active": True
    },
    
    # ==================== LUER ====================
    {
        "name": "Tracker 6820 Original Beanie",
        "slug": "tracker-6820-original-beanie",
        "description": "Klassisk strikket lue i akryl med dobbel lag for ekstra varme.",
        "category": "caps",
        "brand": "Tracker",
        "base_price": 119.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6820_04.jpg"], "stock": {}},
            {"color": "Marine", "color_hex": "#1E3A5F", "sizes": ["One Size"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6820_05.jpg"], "stock": {}},
            {"color": "Grå", "color_hex": "#6B7280", "sizes": ["One Size"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/6820_10.jpg"], "stock": {}},
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
        "name": "Tracker 4013 Hi-Vis Microfleece Jacket",
        "slug": "tracker-4013-hi-vis-microfleece-jacket",
        "description": "Synlig fleece jakke i klasse 3 etter EN ISO20471. Varm og funksjonell arbeidsjakke.",
        "category": "workwear",
        "brand": "Tracker",
        "base_price": 649.0,
        "variants": [
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/4013_37.jpg"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2020/07/4013_38.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 10, "y": 25, "width": 18, "height": 12, "max_width_cm": 7, "max_height_cm": 5},
            {"name": "back", "name_no": "Rygg", "x": 20, "y": 15, "width": 60, "height": 40, "max_width_cm": 30, "max_height_cm": 20}
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
            {"color": "Hi-Vis Gul", "color_hex": "#FACC15", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/04/3013_37_f.jpg"], "stock": {}},
            {"color": "Hi-Vis Oransje", "color_hex": "#F97316", "sizes": ["S", "M", "L", "XL", "XXL", "3XL"], "images": ["https://www.tracker.no/wp-content/uploads/2021/04/3013_38_f.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "left_chest", "name_no": "Venstre bryst", "x": 10, "y": 25, "width": 18, "height": 15, "max_width_cm": 7, "max_height_cm": 6},
            {"name": "back", "name_no": "Rygg", "x": 20, "y": 15, "width": 60, "height": 40, "max_width_cm": 30, "max_height_cm": 20}
        ],
        "materials": ["80% bomull, 20% polyester, 280g/m²"],
        "fit": "Regular",
        "delivery_days": 7,
        "best_for": ["workwear", "safety", "construction"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
    
    # ==================== SEKKER ====================
    {
        "name": "Tracker 9023 Hard Shell PC-Sekk",
        "slug": "tracker-9023-hard-shell-pc-sekk",
        "description": "Stilig PC-sekk med hardt ytterskall og to romslige rom. Laptop-lomme for opptil 15.6 tommer.",
        "category": "accessories",
        "brand": "Tracker",
        "base_price": 899.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["One Size"], "images": ["https://www.tracker.no/wp-content/uploads/2025/01/9023_04_l.jpg"], "stock": {}},
        ],
        "print_methods": ["embroidery", "print"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 30, "y": 30, "width": 40, "height": 20, "max_width_cm": 10, "max_height_cm": 5},
        ],
        "materials": ["100% polyester med hardt skall"],
        "fit": "One Size",
        "delivery_days": 10,
        "best_for": ["business", "travel", "promo"],
        "min_quantity": 1,
        "featured": True,
        "active": True
    },
    {
        "name": "Tracker 9004 Waterproof Roller Bag 100L",
        "slug": "tracker-9004-waterproof-roller-bag",
        "description": "Vanntett trillebag på 100 liter. Sporty, robust og værbestandig for lange reiser.",
        "category": "accessories",
        "brand": "Tracker",
        "base_price": 1899.0,
        "variants": [
            {"color": "Sort", "color_hex": "#000000", "sizes": ["100L"], "images": ["https://www.tracker.no/wp-content/uploads/2025/02/9004_04_2-1.jpg"], "stock": {}},
        ],
        "print_methods": ["print"],
        "print_areas": [
            {"name": "front", "name_no": "Front", "x": 25, "y": 25, "width": 50, "height": 30, "max_width_cm": 20, "max_height_cm": 12},
        ],
        "materials": ["Vanntett tarpaulin"],
        "fit": "100L",
        "delivery_days": 14,
        "best_for": ["travel", "outdoor", "premium"],
        "min_quantity": 1,
        "featured": False,
        "active": True
    },
]
