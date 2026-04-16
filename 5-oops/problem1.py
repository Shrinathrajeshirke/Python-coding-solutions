# Create a class named Laptop.

# In __init__, take brand and ram (in GB).

# Add a method called upgrade_ram that takes extra_ram as an argument and adds it to the existing RAM.

# Add a method called display that prints: "This [brand] laptop has [ram]GB RAM."

# Execute: Create a "Dell" laptop with 8GB, upgrade it by 8GB, and call display.

class Laptop():
    def __init__(self, brand, ram):
        self.brand = brand
        self.ram = ram

    def upgrade_ram(self, add_ram):
        self.ram += add_ram

    def display(self):
        return f"This {self.brand} laptop has {self.ram} GB RAM."
    
dell = Laptop("Dell", 8)

dell.upgrade_ram(8)

print(dell.display())