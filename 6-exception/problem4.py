# Create a dictionary of prices. Ask the user for an item name; if it's not there, handle it.

price_dict = {
    'apple': 5,
    'banana': 11,
    'carrot': 12
}

def item_call():
    

    try:
        item = input("Enter item name: ")
        print(price_dict[item])
    except KeyError:
        print("Item not found")

item_call()