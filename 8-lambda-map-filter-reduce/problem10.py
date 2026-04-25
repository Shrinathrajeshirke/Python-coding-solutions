# Build a complete data analysis tool:

# Take a list of sales data
# Each: (salesperson, region, product, amount)
# Use map, filter, reduce, sorted, lambda to:

# Filter sales above 5000
# Calculate commission (8%)
# Find top salesperson per region
# Find total sales per region
# Sort by commission descending

sales = [
    ("Alice", "North", "Laptop", 8000),
    ("Bob",   "South", "Phone",  3000),
    ("Charlie","North","Tablet", 6000),
    ("David", "South", "Laptop", 9000),
    ("Eve",   "East",  "Phone",  4000),
    ("Frank", "East",  "Tablet", 7000)
]

from functools import reduce

def sales_analyzer(sales):
    valid_sales = list(filter(lambda x: x[3]>5000, sales))
    commission = 8
    sales_commission = list(map(lambda x: (x[0],x[1],x[2],x[3],x[3]*commission/100), valid_sales))
    sorted_by_commission = sorted(sales_commission, key = lambda x: -x[4])
    total_commission = reduce(lambda x,y: x+y[4], sales_commission, 0)

    print("Output: ")
    print("Valid Sales (>5000): ")
    for name, region, product, sales in valid_sales:
        print(f"{name:8} | {region:8} | {product:8} | {sales}")
    print("=========================================================")
    print("With commission (8%): ")
    for name, region, product, sales, sales_com in sales_commission:
        print(f"{name:8} -> {sales} X {commission}% = {round(sales_com,1)}")
    print("=========================================================")
    print("Sorted by commission: ")
    for name, region, product, sales, sales_com in sorted_by_commission:
        print(f"{name:8} -> -{round(sales_com,1)}")
    print("=========================================================")
    print(f"Total Commission: {round(total_commission,1)}")

sales_analyzer(sales=sales)
