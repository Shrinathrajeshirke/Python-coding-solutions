# Create a class BankAccount with:

# Attributes: owner, balance, transactions list
# Method: deposit(amount)
# Method: withdraw(amount)
# Method: get_balance()
# Method: show_transactions()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
        self.transactions_list = []

    def deposit(self, amount):
        self.__balance += amount
        self.transactions_list.append({"type": "deposit", "amount": amount, "balance": self.__balance})

    def withdraw(self, amount):
        self.__balance -= amount
        self.transactions_list.append({"type": "withdraw", "amount": amount, "balance": self.__balance})

    def get_balance(self):
        return self.__balance
    
    def show_transactions(self):
        print("Output: ")
        print("Transaction History: ")
        for transaction in self.transactions_list:
            if transaction['type'] == "deposit":
                print(f"{transaction['type']} -> +{transaction['amount']} -> {transaction['balance']}")
            else:
                print(f"{transaction['type']} -> -{transaction['amount']} -> {transaction['balance']}")

acc = BankAccount("Shrinath", 10000)
acc.deposit(5000)
acc.withdraw(3000)
acc.deposit(2000)
acc.show_transactions()
print(f"Final balance: {acc.get_balance()}")