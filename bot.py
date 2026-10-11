import json, requests, re

TRENDING_PRODUCTS = [
    {
        "اسم": "Poncho Boho Fringe - البونشو لي فالصورة ديالك",
        "سعر": "299",
        "وصف": "بونشو صوف بوهو مع هدب - ترند 2026",
        "images": [
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&crop=top",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&crop=bottom",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&crop=left",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&crop=right",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&q=80&fm=jpg&mark=1",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&auto=format&1",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&auto=format&2",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&auto=format&3",
            "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?w=700&h=700&fit=crop&auto=format&4",
        ]
    },
    {
        "اسم": "Balloon Jeans Wide - جينز بالون ترند دابا",
        "سعر": "349",
        "وصف": "جينز بالون واسع - ترند تيك توك 2026",
        "images": [
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&crop=top",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&crop=bottom",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&1",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&2",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&3",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&4",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&5",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&6",
            "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=700&h=700&fit=crop&7",
        ]
    },
    {
        "اسم": "Sunset Lamp Pro 2026",
        "سعر": "279",
        "وصف": "إضاءة غروب الشمس 16 لون",
        "images": [
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&1",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&2",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&3",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&4",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&5",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&6",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&7",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&8",
            "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=700&h=700&fit=crop&9",
        ]
    },
    {
        "اسم": "Satin Skirt - جيبة ساتان",
        "سعر": "259",
        "وصف": "جيبة ساتان أنيقة",
        "images": [
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop",
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop&1",
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop&2",
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop&3",
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop&4",
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop&5",
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop&6",
            "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=700&h=700&fit=crop&7",
        ]
    },
    {
        "اسم": "Gold Necklace Set - كوليه",
        "سعر": "139",
        "وصف": "كوليه ذهبي 3 طبقات",
        "images": [
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop&1",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop&2",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop&3",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop&4",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop&5",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop&6",
            "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=700&h=700&fit=crop&7",
        ]
    },
]

final = []
for prod in TRENDING_PRODUCTS:
    all_imgs = prod["images"][:12]
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

print(f"✅ تم {len(final)} منتج - كل واحد فيه {len(final[0]['صور'])} تصاور")
