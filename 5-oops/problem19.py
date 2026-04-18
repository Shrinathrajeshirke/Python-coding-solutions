# Create a class with Magic/Dunder methods:

# Class Cart for shopping cart
# __init__ → empty items dict
# __str__ → print cart nicely
# __len__ → number of items
# __add__ → merge two carts
# Regular methods:

# add_item(name, price, qty)
# get_total()

class Cart:
    def __init__(self):
        self.items = {}

    def __str__(self):
        if not self.items:
            return "Cart is empty"
        result = "=== Cart ===\n"
        for name, details in self.items.items():
            result += f"{name}: {details['qty']} X {details['price']}\n"
        result += f"Total: {self.get_total()}"
        return result

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_cart = Cart()
        new_cart.items = self.items.copy()
        for name, details in other.items.items():
            if name in new_cart.items:
                new_cart.items[name]['qty'] += details['qty']
            else:
                new_cart.items[name] = details
        return new_cart

    def add_item(self, name, price, qty):
        self.items[name] = {
            "price": price,
            "qty": qty
        }

    def get_total(self):
        total = 0
        for name, details in self.items.items():
            total += details['price']*details['qty']
        return total

cart1 = Cart()
cart1.add_item("Apple", 10, 3)
cart1.add_item("Bread", 25, 2)

cart2 = Cart()
cart2.add_item("Milk", 20, 1)

cart3 = cart1 + cart2  

print(cart1)           
print(len(cart1))     
print(cart3)  