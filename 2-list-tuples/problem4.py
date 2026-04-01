# > **Write a program using Tuples that:**
# > - Creates a tuple of 5 cities
# > - Prints total number of cities
# > - Checks if a city entered by user exists in tuple
# > - Prints index of that city if found
# > - Prints how many times a city appears

def tuple_ops():
    cities = ("Mumbai","Delhi","Pune","Mumbai","Nashik")

    print(f"Total cities: {len(cities)}")

    city_to_search = input("Enter a city to search: (select from Mumbai, Pune, Delhi, Nashik): ").capitalize()

    print(f"Enter a city to search: {city_to_search}")

    if city_to_search in cities:
     
        print(f"{city_to_search} found at {cities.index(city_to_search)}")

        print(f"{city_to_search} appears {cities.count(city_to_search)} times")
    
    else:
        print(f"{city_to_search} not found")

tuple_ops()
          
