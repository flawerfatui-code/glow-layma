import json

# بوت بسيط ما كيخسرش الموقع
products = [
  {"اسم": "Glow Light", "صورة": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400", "صور": ["https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600"], "سعر": "24.99", "ربح": "11.00", "وصف": "إضاءة ترند", "تقييم": "⭐ 4.9"},
  {"اسم": "Cardigan", "صورة": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=400", "صور": ["https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=600"], "سعر": "28.99", "ربح": "13.00", "وصف": "كارديجان", "تقييم": "⭐ 4.8"},
  {"اسم": "Dress Puff", "صورة": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=400", "صور": ["https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?w=600"], "سعر": "32.99", "ربح": "15.00", "وصف": "فستان", "تقييم": "⭐ 4.7"},
  {"اسم": "Jeans Wide", "صورة": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", "صور": ["https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400"], "سعر": "29.99", "ربح": "14.00", "وصف": "جينز", "تقييم": "⭐ 4.6"},
  {"اسم": "LED Mirror", "صورة": "https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=400", "صور": ["https://images.unsplash.com/photo-1522338140262-f46f5913618a?w=400"], "سعر": "35.99", "ربح": "16.00", "وصف": "مرايا", "تقييم": "⭐ 4.9"}
]

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print("✅ تم")
