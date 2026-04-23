# Using ALL concepts together:

# Take a list of orders
# Each order: (customer, product, quantity, price)
# Filter valid orders (quantity > 0 and price > 0)
# Map to calculate:

# Total per order
# Apply tax (18%)
# Apply loyalty discount:

# 15% if total > 1000
# 5% if total > 500




# Sort by final amount descending
# Reduce to find grand total
# Print complete order summary

orders = [
    ("Alice", "Laptop", 2, 800),
    ("Bob",   "Phone",  0, 600),
    ("Charlie","Book",  3, 200),
    ("David", "Pen",    5, -10),
    ("Eve",   "Tablet", 1, 900)
]

from functools import reduce

def cart(ord):
    valid_orders = list(filter(lambda x: x[2]>0 and x[3]>0, ord))

    tax = 0.18

    total_per_order = list(map(lambda x: (x[0], x[1], x[2], x[3], x[2]*x[3]), valid_orders))

    total_per_order = list(map(lambda x: (x[0], x[1], x[2], x[3], x[4]*(1-0.15)*(1+tax) if x[4]>1000 
                                          else x[4]*(1-0.05)*(1+tax) if x[4]>500
                                          else x[4]), total_per_order))
    
    sorted_total = sorted(total_per_order, key = lambda x: -x[4])

    grand_total = reduce(lambda x, y: x+y[4], sorted_total, 0)

    print("Output: ")
    print("Valid Orders: ")
    for name, product, qty, price in valid_orders:
        print(f"{name:8} | {product:8} | {qty} X {price} = {qty*price}")

    print("Sorted by Final amount")
    for name, product, qty, price, total in sorted_total:
        print(f"{name} -> {round(total,2)}")

    print(f"Grand total: {round(grand_total,2)}")    

cart(orders)