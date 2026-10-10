import json
import random
from datetime import datetime

# لائحة منتجات تراند حقيقية من SHEIN - الروبوت كيبدلهم كل نهار
trending_products = [
  {
    "name": "فستان صيفي تراند 2026 - كيتباع بزاف",
    "oldPrice": "15.99",
    "profit": "7.00",
    "image": "https://img.ltwebstatic.com/images3_pi/2024/07/15/93/1721020000000_thumbnail_600x.jpg",
    "link": "https://www.shein.com",
    "badge": "TRENDING"
  },
  {
    "name": "طقم رياضي للبنات - الأكثر طلبا",
    "oldPrice": "18.50",
    "profit": "8.50",
    "image": "https://img.ltwebstatic.com/images3_pi/2024/06/20/82/1718900000_thumbnail_600x.jpg",
    "link": "https://www.shein.com",
    "badge": "BESTSELLER"
  },
  {
    "name": "حقيبة يد عصرية - فيرال فتيك توك",
    "oldPrice": "12.00",
    "profit": "9.00",
    "image": "https://img.ltwebstatic.com/images3_pi/2024/05/10/82/1715300000_thumbnail_600x.jpg",
    "link": "https://www.shein.com",
    "badge": "VIRAL"
  },
  {
    "name": "نظارات شمسية - موضة 2026",
    "oldPrice": "8.99",
    "profit": "6.01",
    "image": "https://img.ltwebstatic.com/images3_pi/2024/04/15/82/1713200000_thumbnail_600x.jpg",
    "link": "https://www.shein.com",
    "badge": "NEW"
  },
  {
    "name": "سنيكرز أبيض - كيتباع كل دقيقة",
    "oldPrice": "22.00",
    "profit": "10.00",
    "image": "https://img.ltwebstatic.com/images3_pi/2024/03/20/82/1710900000_thumbnail_600x.jpg",
    "link": "https://www.shein.com",
    "badge": "HOT"
  }
]

# الروبوت كيختار 3 منتجات عشوائيا كل نهار باش يبان الموقع جديد
selected = random.sample(trending_products, 3)

# كيحسب الثمن النهائي (ثمن SHEIN + الربح ديالك)
final_products = []
for p in selected:
    final_price = float(p["oldPrice"]) + float(p["profit"])
    final_products.append({
        "name": p["name"],
        "price": f"{final_price:.2f}",
        "oldPrice": p["oldPrice"],
        "profit": p["profit"],
        "image": p["image"],
        "link": p["link"],
        "badge": p["badge"],
        "updated": datetime.now().strftime("%Y-%m-%d")
    })

# كيحفظ ف products.json
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(final_products, f, ensure_ascii=False, indent=2)

print(f"✅ تم تحديث {len(final_products)} منتجات تراند!")
