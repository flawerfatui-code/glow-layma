import json
import random

trending_products = [
  {"name": "فستان صيفي تراند 2026", "oldPrice": "15.99", "profit": "7.00", "image": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=400", "link": "https://www.shein.com", "badge": "TRENDING"},
  {"name": "طقم رياضي للبنات - الأكثر طلبا", "oldPrice": "18.50", "profit": "8.50", "image": "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?w=400", "link": "https://www.shein.com", "badge": "BESTSELLER"},
  {"name": "حقيبة يد عصرية - فيرال", "oldPrice": "12.00", "profit": "9.00", "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=400", "link": "https://www.shein.com", "badge": "VIRAL"},
  {"name": "نظارات شمسية - موضة 2026", "oldPrice": "8.99", "profit": "6.01", "image": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=400", "link": "https://www.shein.com", "badge": "NEW"},
  {"name": "سنيكرز أبيض - كيتباع كل دقيقة", "oldPrice": "22.00", "profit": "10.00", "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400", "link": "https://www.shein.com", "badge": "HOT"},
  {"name": "بلوزة كروب توب ترند", "oldPrice": "9.99", "profit": "6.00", "image": "https://images.unsplash.com/photo-1554568218-0f1715e72254?w=400", "link": "https://www.shein.com", "badge": "TRENDING"},
  {"name": "جيب جينز قصير - صيف 2026", "oldPrice": "14.50", "profit": "7.50", "image": "https://images.unsplash.com/photo-1541099649105-f69ad21f3246?w=400", "link": "https://www.shein.com", "badge": "HOT"},
  {"name": "بيجاما حرير فاخرة", "oldPrice": "16.99", "profit": "8.00", "image": "https://images.unsplash.com/photo-1618354691792-d1d42acfd860?w=400", "link": "https://www.shein.com", "badge": "BESTSELLER"},
  {"name": "إكسسوارات شعر لامعة", "oldPrice": "5.99", "profit": "5.00", "image": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?w=400", "link": "https://www.shein.com", "badge": "VIRAL"},
  {"name": "تنورة ميدي أنيقة", "oldPrice": "13.99", "profit": "7.00", "image": "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?w=400", "link": "https://www.shein.com", "badge": "NEW"}
]

final_products = []
for p in trending_products:
    final_price = float(p["oldPrice"]) + float(p["profit"])
    final_products.append({
        "اسم": p["name"],
        "سعر": f"{final_price:.2f}",
        "ربح": p["profit"],
        "صورة": p["image"],
        "وصلة": p["link"],
        "badge": p["badge"]
    })

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(final_products, f, ensure_ascii=False, indent=2)

print(f"✅ تم تحديث {len(final_products)} منتج بالتصاور الحقيقية!")
