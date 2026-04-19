# Write a complete program that:

# Custom exception InsufficientFunds
# Class BankAccount with file storage
# Saves transactions to "bank.txt"
# Operations:

# deposit(amount)
# withdraw(amount) — raises InsufficientFunds
# get_balance()
# show_history()

class InsufficientFunds(Exception):
    pass

class BankAccount:
    def __init__(self, filename, balance):
        self.filename = filename
        self.__balance = balance

    def write_transactions(self, transaction, amount):
        with open(self.filename, "a") as f:
            f.write(f"{transaction},{amount},{self.__balance}\n")

    def deposit(self, amount):
        self.__balance += amount
        self.write_transactions("deposit", amount)
        print(f"Deposited {amount} Balance: {self.__balance}")
    
    def withdraw(self, amount):
        try:
            if amount > self.__balance:
                raise InsufficientFunds(f"Balance {self.__balance} < {amount}!")
            
        
            self.__balance -= amount
            self.write_transactions("Withdrawl", amount)
            print(f"Withdrawn {amount} Balance: {self.__balance}")
        except InsufficientFunds as e:
            print(f"Insufficient funds: {e}")
        
        
    def get_balance(self):
        return self.__balance
    
    def show_history(self):
        try:
            with open(self.filename, "r") as f:
                transactions = f.readlines()
                
            if not transactions:
                print("No transactions yet")
                return
            
            print("=== Transaction History ===")
            for transaction in transactions:
                type, amount, balance = transaction.strip().split(",")
                print(f"{type:^8} | {amount:^8} | Balance: {balance:^8}")
        except FileNotFoundError:
            print("File does not exists")

acc = BankAccount("bank.txt", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  # raises exception!
acc.show_history()