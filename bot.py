import json
import random
from datetime import datetime

# لائحة منتجات تراند - زدناها 15 منتج باش يبان الموقع عامر
trending_products = [
  {"name": "فستان صيفي تراند 2026 - كيتباع بزاف", "oldPrice": "15.99", "profit": "7.00", "image": "https://img.ltwebstatic.com/images3_pi/2024/07/15/93/1721020000000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "TRENDING"},
  {"name": "طقم رياضي للبنات - الأكثر طلبا", "oldPrice": "18.50", "profit": "8.50", "image": "https://img.ltwebstatic.com/images3_pi/2024/06/20/82/1718900000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "BESTSELLER"},
  {"name": "حقيبة يد عصرية - فيرال فتيك توك", "oldPrice": "12.00", "profit": "9.00", "image": "https://img.ltwebstatic.com/images3_pi/2024/05/10/82/1715300000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "VIRAL"},
  {"name": "نظارات شمسية - موضة 2026", "oldPrice": "8.99", "profit": "6.01", "image": "https://img.ltwebstatic.com/images3_pi/2024/04/15/82/1713200000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "NEW"},
  {"name": "سنيكرز أبيض - كيتباع كل دقيقة", "oldPrice": "22.00", "profit": "10.00", "image": "https://img.ltwebstatic.com/images3_pi/2024/03/20/82/1710900000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "HOT"},
  {"name": "بلوزة كروب توب ترند", "oldPrice": "9.99", "profit": "6.00", "image": "https://img.ltwebstatic.com/images3_pi/2024/08/10/15/1723300000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "TRENDING"},
  {"name": "جيب جينز قصير - صيف 2026", "oldPrice": "14.50", "profit": "7.50", "image": "https://img.ltwebstatic.com/images3_pi/2024/08/05/22/1722900000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "HOT"},
  {"name": "بيجاما حرير فاخرة", "oldPrice": "16.99", "profit": "8.00", "image": "https://img.ltwebstatic.com/images3_pi/2024/07/20/10/1721400000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "BESTSELLER"},
  {"name": "إكسسوارات شعر لامعة", "oldPrice": "5.99", "profit": "5.00", "image": "https://img.ltwebstatic.com/images3_pi/2024/06/25/11/1719300000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "VIRAL"},
  {"name": "تنورة ميدي أنيقة", "oldPrice": "13.99", "profit": "7.00", "image": "https://img.ltwebstatic.com/images3_pi/2024/05/25/30/1716600000_thumbnail_600x.jpg", "link": "https://www.shein.com", "badge": "NEW"}
]

# دابا كيجيب كاع المنتجات ماشي غير 3
selected = trending_products  # كاع المنتجات

# كيحسب ثمن واحد فقط
final_products = []
for p in selected:
    final_price = float(p["oldPrice"]) + float(p["profit"])
    final_products.append({
        "اسم": p["name"],
        "سعر": f"{final_price:.2f}",
        "ربح": p["profit"],
        "صورة": p["image"],
        "وصلة": p["link"],
        "badge": p["badge"]
    })

# كيحفظ
with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(final_products, f, ensure_ascii=False, indent=2)

print(f"✅ تم تحديث {len(final_products)} منتج بثمن واحد فقط!")
