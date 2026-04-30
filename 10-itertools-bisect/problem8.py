# Using itertools.accumulate():

# Take a list of daily sales
# Calculate running total
# Calculate running average
# Find day with highest cumulative sales

daily_sales = [100, 150, 200, 120, 180, 220, 190]

import itertools

def sales_analyzer(daily_sales):
    running_totals = list(itertools.accumulate(daily_sales))
    print("Output")
    print("Day-wise running total")

    for i, (sale, total) in enumerate(zip(daily_sales, running_totals), 1):
        print(f"Day {i}: {sale} (Total: {total})")
    
    print("\nRunning Average: ")
    for i, running_total in enumerate(running_totals, 1):
        print(f"Day {i}: {round(running_total/i, 2)}")

    highest = max(running_totals)
    highest_day = running_totals.index(highest) + 1

    print(f"\nHighest Cumulative Sales: Day {highest_day} -> {highest}")

sales_analyzer(daily_sales)