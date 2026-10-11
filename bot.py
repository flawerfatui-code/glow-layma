import json

products = [
  {
    "اسم":"Chunky Cardigan - كارديجان صوف",
    "id":"1434389677669-e08b4cac3105",
    "سعر":"289",
    "وصف":"كارديجان صوف oversize دافئ - موضة شتاء 2026 🧶 مقاس واحد"
  },
  {
    "اسم":"Glow Sunset Lamp - إضاءة غروب",
    "id":"1507473885765-e6ed057f782c",
    "سعر":"249",
    "وصف":"إضاءة غروب الشمس الأصلية 16 لون مع ريموت - ترند تيك توك 🔥"
  },
  {
    "اسم":"Wide Leg Jeans - جينز واسع",
    "id":"1541099649105-f69ad21f3246",
    "سعر":"299",
    "وصف":"جينز واسع Wide Leg - ترند 2026"
  },
  {
    "اسم":"Gold Necklace Set",
    "id":"1515562141207-7a88fb7ce338",
    "سعر":"139",
    "وصف":"كوليه ذهبي 3 طبقات - موضة 2026"
  },
  {
    "اسم":"Sunglasses Retro",
    "id":"1511499767150-a48a237f0083",
    "سعر":"169",
    "وصف":"نظارات شمس ريترو - حماية UV"
  },
  {
    "اسم":"Satin Skirt",
    "id":"1583496661160-fb5886a0aaaa",
    "سعر":"259",
    "وصف":"جيبة ساتان أنيقة - للمناسبات"
  },
]

final=[]
for p in products:
    # نفس المنتج - 4 صور ديال نفس المنتج غير زوايا مختلفة (نفس الصورة ب crop مختلف باش ما يبانش منتج آخر)
    base = f"https://images.unsplash.com/photo-{p['id']}"
    imgs = [
        f"{base}?w=600&h=600&fit=crop",
        f"{base}?w=600&h=600&fit=crop&crop=top",
        f"{base}?w=600&h=600&fit=crop&crop=bottom",
        f"{base}?w=600&h=600&fit=crop&crop=center&zoom=1.2"
    ]
    final.append({
        "اسم": p["اسم"],
        "صورة": imgs[0],
        "صور": imgs,
        "سعر": p["سعر"],
        "وصف": p["وصف"],
        "تقييم": "⭐ 4.8"
    })

with open('products.json','w',encoding='utf-8') as f:
    json.dump(final,f,ensure_ascii=False,indent=2)

print(f"✅ {len(final)} منتج - كل واحد 4 تصاور ديال نفس المنتج") 
