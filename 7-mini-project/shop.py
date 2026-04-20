class OutOfStock(Exception):
    pass

class ProductNotFound(Exception):
    pass

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Shop:
    def __init__(self):
        self.products = {}
        self.receipt_list = []
    
    def add_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products[name] = product
        print(f"{name} added!")

    def view_product(self):
        if not self.products:
            print("No products found")
        else:
            print("=== Products ===")
            for name, product in self.products.items():
                print(f"{name: <10} | Price: {product.price: ^4} | Stock: {product.stock: ^4}")

    def buy_product(self, name, quantity):
        try: 
            if name not in self.products:
                raise ProductNotFound(f'{name} is not available.')
            elif self.products[name].stock < quantity:
                raise OutOfStock(f"{name} is out of stock")
            else:
                self.products[name].stock -= quantity
                total = self.products[name].price*quantity
                self.receipt_list.append({
                    "name": name,
                    "qty": quantity,
                    "price": total
                })
                print(f"{name} X {quantity} = {total}")
        except ProductNotFound as e:
            print(f"Error: {e}")
        except OutOfStock as e:
            print(f"Error: {e}")
    
    def view_receipt(self):
        if not self.receipt_list:
            print("Nothing bought yet")
            return 
        total_amount = 0
        print("=== receipt ===")
        for item in self.receipt_list:
            print(f"{item['name']} X {item['qty']} = {item['price']}")
            total_amount += item['price']
        print("------------------")
        print(f"Total: {total_amount}")

    def save_to_file(self, filename="shop.txt"):
        with open(filename, "w") as f:
            for name, product in self.products.items():
                product_details = f"{name},{product.price},{product.stock}\n"
                f.write(product_details)
        print("Data Saved!")
    
    def load_from_file(self, filename="shop.txt"):
        try:
            with open(filename, "r") as f:
                lines = f.readlines()
                for line in lines:
                    name, price, stock = line.strip().split(",")
                    product = Product(name, float(price), float(stock))
                    self.products[name] = product
        except FileNotFoundError:
            print("Store is empty")
    
    def run(self):
        self.load_from_file()
        while True:
            print("1. Add product\n")
            print("2. View all products\n")
            print("3. Buy product\n")
            print("4. View receipt\n")
            print("5. Save data to file\n")
            print("6. Load data from file\n")
            print("7. Exit")

            choice = input("Choose: ")

            if choice == "1":
                name = input("Enter a product name: ")
                try:
                    price = float(input("Enter price of product: "))
                    stock = int(input("Enter number of products: "))
                except ValueError:
                    print("Enter correct number")
                    continue
                self.add_product(name, price, stock)
                print("Product added successfully")
            
            elif choice == "2":
                self.view_product()

            elif choice == "3":
                name = input("Enter a product name: ")
                try:
                    qty = int(input("Enter quantity required: "))
                except ValueError:
                    print("Enter correct quantity")
                    continue
                self.buy_product(name, quantity=qty)
            
            elif choice == "4":
                self.view_receipt()
            
            elif choice == "5":
                self.save_to_file()

            elif choice == "6":
                self.load_from_file()
            
            elif choice =="7":
                self.save_to_file()
                print("Bye!")
                break
                
            else:
                print("Invalid choice: 1-7")
        
s = Shop()
s.run()