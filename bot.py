import json

products = [
  {
    "اسم": "Glow Light - إضاءة ترند تيك توك",
    "صورة": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400",
    "صور": [
      "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600",
      "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?w=600",
      "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600",
      "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600"
    ],
    "سعر": "24.99", "ربح": "11.00",
    "وصف": "إضاءة غروب الشمس الشهيرة - 16 لون",
    "تقييم": "⭐ 4.9"
  },
  {
    "اسم": "Chunky Cardigan - كارديجان شتوي",
    "صورة": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=400",
    "صور": [
      "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=600",
      "https://images.unsplash.com/photo-1516762689617-e1cffcef479d?w=600",
      "https://images.unsplash.com/photo-1578587018452-892bacefd3f2?w=600",
      "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=600"
    ],
    "سعر": "28.99", "ربح": "13.00",
    "وصف": "كارديجان صوف دافئ موضة 2026",
    "تقييم": "⭐ 4.8"
  },
  {
    "اسم": "LED Mirror - مرايا مكياج",
    "صورة": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=400",
    "صور": [
      "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=600",
      "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=600",
      "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=600",
      "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=600"
    ],
    "سعر": "35.99", "ربح": "16.00",
    "وصف": "مرايا بإضاءة LED للمكياج",
    "تقييم": "⭐ 4.9"
  },
  {
    "اسم": "Puff Dress - فستان",
    "صورة": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=400",
    "صور": [
      "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=600",
      "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=600",
      "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=600",
      "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=600"
    ],
    "سعر": "32.99", "ربح": "15.00",
    "وصف": "فستان رومانسي",
    "تقييم": "⭐ 4.7"
  },
  {
    "اسم": "Wide Jeans - جينز واسع",
    "صورة": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400",
    "صور": [
      "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600",
      "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600",
      "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600",
      "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=600"
    ],
    "سعر": "29.99", "ربح": "14.00",
    "وصف": "جينز واسع موضة 2026",
    "تقييم": "⭐ 4.6"
  }
]

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"✅ تم {len(products)} منتجات - كل واحد تصاورو بوحدو")
