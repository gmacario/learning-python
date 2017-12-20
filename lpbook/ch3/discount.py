# discount.py
# Reference: w_pacb43.pdf, page 88

from datetime import date, timedelta

today = date.today()
tomorrow = today + timedelta(days=1)
products = [
    {'sku': '1', 'expiration_date': today, 'price': 100.0},
    {'sku': '2', 'expiration_date': tomorrow, 'price': 50},
    {'sku': '3', 'expiration_date': today, 'price': 20},
]

# print("DEBUG: products=", products)
for product in products:
    # print("DEBUG: product=", product)
    if product['expiration_date'] != today:
        continue
    product['price'] *= 0.8     # Apply a 20% discount
    print(
        'Price for sku', product['sku'],
        'is now', product['price']
    )

# EOF
