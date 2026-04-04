# Write a program that:

# Takes a list of transactions
# (deposits and withdrawals)
# Maintains a running balance
# Stores transaction history
# Prints complete bank statement

def bank_statement():
    transactions = [
    ("deposit", 10000),
    ("deposit", 5000),
    ("withdrawal", 3000),
    ("deposit", 2000),
    ("withdrawal", 8000),
    ("withdrawal", 1000)
    ]

    balance = 0
    total_deposit = 0
    total_withdrawl = 0
    print("============ Bank Statement ============")

    for trans_type, amount in transactions:
        if trans_type == "deposit":
            balance += amount
            total_deposit += amount
            print(f"deposit -> +{amount} | Balance: {balance}")
        else:
            balance -= amount
            total_withdrawl += amount
            print(f"withdrawl -> -{amount} | Balance: {balance}")

    print("==========================================")
    print(f"Total Deposit: {total_deposit}")
    print(f"Total Withdrawl: {total_withdrawl}")
    print(f"Final Balance: {balance}")
    
    
bank_statement()
        

    
    
         