# > **Write a program that:**
# > - Creates a dictionary of items and prices
# > - Apply 10% discount on items above 1000
# > - Add 18% GST on all items
# > - Print final price of each item



def price_calc():

    items = {
    "Laptop": 50000,
    "Phone": 15000,
    "Earphones": 800,
    "Keyboard": 1200,
    "Mouse": 500
    }

    for item, price in items.items():
        if price > 1000:
            discount = price*0.10
        else:
            discount = 0
        
        GST = round((price-discount)*0.18,2)

        final = price - discount + GST

        print(f"item: {item} | Original Price: {price} | Discount: {discount} | GST: {GST} | Final Amount: {final}")

price_calc()