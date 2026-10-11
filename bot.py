import json

products = []

base = [
  ("Glow Sunset Lamp - إضاءة غروب", "photo-1507473885765-e6ed057f782c", "إضاءة غروب 16 لون مع ريموت - ترند تيك توك 🔥 تصاور احترافية", "249"),
  ("Cloud LED - سحابة مضيئة", "photo-1513506003901-1e6a229e2d15", "سحابة LED كتضوي فالليل - ديكور غرفة نوم حالم ☁️", "199"),
  ("Moon Lamp - قمر مضيء", "photo-1558618666-fcd25c85cd64", "قمر 3D مضيء - هدية رومانسية 🌙", "229"),
  ("Chunky Knit Cardigan", "photo-1434389677669-e08b4cac3105", "كارديجان صوف دافئ oversize - شتاء 2026 🧶", "289"),
  ("Puff Sleeve Dress", "photo-1515378791036-0648a3ef77b2", "فستان puff رومانسي - ستايل cottagecore 👗", "329"),
  ("Wide Leg Jeans", "photo-1541099649105-f69ad21f3246", "جينز واسع موضة 2026 - كيجي مع كلشي 👖", "299"),
  ("Crop Top Basic", "photo-1521572163474-6864f9cf17ab", "كروب توب قطن - أساسي فكل خزانة", "149"),
  ("Satin Skirt", "photo-1583496661160-fb5886a0aaaa", "جيبة ساتان أنيقة - للمناسبات", "259"),
  ("Oversized Hoodie", "photo-1556821840-3a63f95609a7", "هودي oversize دافئ - ستايل ستريت", "279"),
  ("Teddy Coat", "photo-1544022613-e87ca75a784a", "معطف تيدي ناعم - دفء وأناقة", "399"),
  ("LED Vanity Mirror", "photo-1522338140262-f46f5913618a", "مرايا مكياج بإضاءة LED - 3 ألوان 💡", "359"),
  ("Hair Dryer Mini", "photo-1522338140262-f46f5913618a", "سيشوار صغير قوي - للسفر", "279"),
  ("Makeup Brush Set 12pcs", "photo-1596462502278-27bfdc403348", "فرش مكياج 12 قطعة - شعر ناعم", "189"),
  ("Silk Pillowcase", "photo-1584100936595-c0654b55a2e2", "غطاء مخدة حرير - للشعر والبشرة", "159"),
  ("Scented Candle", "photo-1602874801027-beb0381d39", "شمعة معطرة - رائحة فانيلا", "129"),
  ("Mini Projector", "photo-1513506003901-1e6a229e2d15", "بروجيكتور صغير - سينما فالدار", "599"),
  ("Phone Holder Ring Light", "photo-1507473885765-e6ed057f782c", "حامل هاتف مع إضاءة - لللايف", "179"),
  ("Aesthetic Storage Box", "photo-1558618666-fcd25c85cd64", "صندوق تنظيم شفاف - aesthetic", "99"),
  ("Fuzzy Socks 5 pairs", "photo-1434389677669-e08b4cac3105", "تقاشر فرو 5 أزواج - دافئين", "119"),
  ("Leather Tote Bag", "photo-1584917865442-de89df76afd3", "ساك جلد كبير - للجامعة والخدمة", "349"),
  ("Gold Necklace Set", "photo-1515562141207-7a88fb7ce338", "كوليه ذهبي - 3 طبقات موضة", "139"),
  ("Claw Clips Set", "photo-1522338140262-f46f5913618a", "مقابض شعر ترند - 12 قطعة", "79"),
  ("Yoga Leggings", "photo-1506629082955-511b1aa562c8", "ليغينغز رياضة - خامة عالية", "199"),
  ("Sunglasses Retro", "photo-1511499767150-a48a237f0083", "نظارات شمس ريترو - حماية UV", "169"),
  ("Beanie Hat Wool", "photo-1576871337632-b9aef4c17ab9", "طاقية صوف - دافئة وأنيقة", "89"),
]

for i, (name, img_id, desc, price) in enumerate(base):
    profit = str(int(int(price)*0.4))
    p = {
        "اسم": name,
        "صورة": f"https://images.unsplash.com/{img_id}?w=400&h=400&fit=crop",
        "صور": [
            f"https://images.unsplash.com/{img_id}?w=600&h=600&fit=crop",
            f"https://images.unsplash.com/{img_id}?w=600&h=600&fit=crop&sat=-20",
            f"https://images.unsplash.com/{img_id}?w=600&h=600&fit=crop&sat=20",
            f"https://images.unsplash.com/{img_id}?w=600&h=600&fit=crop&blur=2",
        ],
        "سعر": price,
        "ربح": profit,
        "وصف": f"{desc}\n\n✅ جودة عالية\n🚚 توصيل لجميع المدن\n💵 دفع عند الاستلام\n🎁 هدية مجانية مع كل طلب",
        "تقييم": f"⭐ {round(4.5 + (i%5)*0.1,1)} ({800+i*123} تقييم)"
    }
    products.append(p)

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"✅ تم {len(products)} منتج - الموقع عامر دابا!")
