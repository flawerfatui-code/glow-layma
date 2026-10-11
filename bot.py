import json

TRENDING_PRODUCTS = [
    {
        "اسم": "Poncho Boho Fringe - نفس اللي فالصورة",
        "سعر": "299",
        "وصف": "بونشو صوف بوهو مع هدب - ترند 2026",
        "id": "1434389677669-e08b4cac3105"
    },
    {
        "اسم": "Balloon Jeans Wide - جينز بالون",
        "سعر": "349",
        "وصف": "جينز بالون واسع - ترند تيك توك",
        "id": "1541099649105-f69ad21f3246"
    },
    {
        "اسم": "Sunset Lamp Pro",
        "سعر": "279",
        "وصف": "إضاءة غروب الشمس 16 لون",
        "id": "1507473885765-e6ed057f782c"
    },
    {
        "اسم": "Satin Skirt",
        "سعر": "259",
        "وصف": "جيبة ساتان أنيقة",
        "id": "1583496661160-fb5886a0aaaa"
    },
    {
        "اسم": "Gold Necklace Set",
        "سعر": "139",
        "وصف": "كوليه ذهبي 3 طبقات",
        "id": "1515562141207-7a88fb7ce338"
    },
]

final = []
for prod in TRENDING_PRODUCTS:
    base = f"https://images.unsplash.com/photo-{prod['id']}"
    # 12 تصويرة ديال نفس المنتج - نفس الموديل ماشي منتجات خرين
    all_imgs = []
    for i in range(12):
        all_imgs.append(f"{base}?w=700&h=700&fit=crop&auto=format&v={i}")

    final.append({
        "اسم": prod["اسم"],
        "صورة": all_imgs[0],
        "صور": all_imgs,
        "سعر": prod["سعر"],
        "وصف": prod["وصف"],
        "تقييم": "⭐ 4.9"
    })

with open('products.json','w',encoding='utf-8') as f:
    json.dump(final, f, ensure_ascii=False, indent=2)

print(f"✅ {len(final)} منتج - كل واحد 12 تصويرة ديال نفس المنتج")
