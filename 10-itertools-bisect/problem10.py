# Product recommendation system
# Products with ratings and prices
# Use bisect for price range filtering
# Use combinations to suggest product bundles
# Use accumulate for total bundle prices

products = [
    ("Laptop", 4.5, 800),
    ("Mouse", 4.2, 20),
    ("Keyboard", 4.3, 50),
    ("Monitor", 4.6, 300),
    ("Headphones", 4.4, 100),
    ("Webcam", 4.1, 80)
]

import itertools, bisect

def product_recommender(products, min_price, max_price):
    in_budget = [p for p in products if min_price <= p[2] <= max_price]

    print("Products in budget: ")

    for name, rating, price in in_budget:
        print(f"{name} -> {rating} -> ${price}")

    bundles = list(itertools.combinations(products, 2))

    print(f"\nRecommended Bundles (2 items)")
    for i, (p1,p2) in enumerate(bundles, 1):
        total = p1[2] + p2[2]
        print(f"Bundle {i}: {p1[0]} + {p2[0]} -> ${total}")

    first_three = bundles[:3]
    bundle_prices = [p1[2]+p2[2] for p1,p2 in first_three]
    running_totals = list(itertools.accumulate(bundle_prices))

    print("\nBundle Price Breakdown (first 3):")
    for (p1, p2), total in zip(first_three, running_totals):
        print(f"{p1[0]} + {p2[0]} -> Running total: ${total}")

product_recommender(products, 200,400)
