# Write a program that:

# Creates a dictionary of 5 countries and their capitals
# Prints all countries
# Prints all capitals
# Prints each country with its capital

countries = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "UK": "London",
    "Japan": "Tokyo",
    "France": "Paris"
}

print(f"Countries: {list(countries.keys())}")

print(f"Capitals: {list(countries.values())}")

for country, capital in countries.items():
    print(f"{country} -> {capital}")

