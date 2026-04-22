# Using map(), filter(), reduce():

# Take a list of products with
# name, price, quantity
# Filter products worth buying
# (total value > 500)
# Map to calculate discount:

# 20% if total > 1000
# 10% if total > 500


# Use reduce to find
# grand total after discount

products = [
    ("Apple",  50,  5),
    ("Laptop", 800, 2),
    ("Pen",    10, 10),
    ("Phone",  600, 1),
    ("Book",   200, 4)
]
from functools import reduce

def worth_products(prod):
    worth_buy_products = list(filter(lambda x: x[1]*x[2]>500, prod))

    buy_prod_prices = list(map(lambda x: (x[0], x[1], x[2], x[1]*x[2]),worth_buy_products))

    discounted_prices = list(map(lambda x: (x[0], x[1], x[2], x[3]*0.80 if x[3]> 1000 
                                            else x[3]*0.90 if x[3]>500
                                            else x[3]), buy_prod_prices))
    
    total_price = reduce(lambda x,y: x+y[3], discounted_prices,0)

    print("Output: ")
    print("Filtered Products: ")
    
    for product, price, qty, amt in buy_prod_prices:
        print(f"{product} -> {price} X {qty} = {amt}")

    print("After discount: ")
    for product, price, qty, price_after_discount in discounted_prices:
        print(f"{product} -> {price} X {qty} = {price_after_discount}")

    print(f"Grand Total: {total_price}")

worth_products(products)