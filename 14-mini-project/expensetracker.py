import re
from collections import defaultdict

class Expense:
    def __init__(self ,category, amount, date):
        if not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
            raise ValueError(f"Invalid date format: {date}")
        self.category = category
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"{self.category} - ${self.amount} - {self.date}"
    
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = defaultdict(list)

    def add_expense(self, category, amount, date):
        try:
            expense = Expense(category, amount, date)
            self.expenses.append(expense)
            self.categories[category].append(expense)
            print(f"Expense added: {expense}")
        except ValueError as e:
            print(e)

    def view_all(self):
        print("All expenses")
        if self.expenses == []:
            print("No expenses found.")
        else:
            sorted_expenses = sorted(self.expenses, key = lambda x: x.date)
            for i, expense in enumerate(sorted_expenses, start=1):
                print(f"{i}. {expense}")

    def view_by_category(self, category):
        print(f"{category} Expenses:")
        if category not in self.categories:
            print("category not found")
        else:
            expenses = self.categories[category]
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense}")
            total = sum(expense.amount for expense in expenses)
            print(f"Total: ${total}")

    def total_spending(self):
        total = sum(expense.amount for expense in self.expenses)
        total_expenses = len(self.expenses)
        print(f"Total spending: ${total}")
        print(f"Total Expenses: {total_expenses}")
    
    def most_expensive_category(self):
        category_totals = {cg: sum(expense.amount for expense in expenses) for cg, expenses in self.categories.items()}
        max_category = max(category_totals, key=lambda x: category_totals[x])
        print(f"Most Expensive Category: {max_category} - ${category_totals[max_category]}")
    
    def search_by_range(self, min_amount, max_amount):
        if not self.expenses:
            print("No expenses found.")
        sorted_expenses = sorted(self.expenses, key= lambda x: x.amount)
        print(f"Expenses between ${min_amount} and ${max_amount}: ")
        filtered_expenses = [e for e in sorted_expenses if min_amount <= e.amount <= max_amount]
        if not filtered_expenses:
            print("No expenses found in this range")
        for i, expense in enumerate(filtered_expenses, start=1):
            print(f"{i}. {expense}")
        
    def save_to_file(self, file_name):
        with open(file_name, "w") as f:
            for expense in self.expenses:
                f.write(f"{expense.category},{expense.amount},{expense.date}\n")
        print(f"Expenses saved to {file_name}")
    
    def load_from_file(self, file_name):
        self.expenses = []
        self.categories = defaultdict(list)
        try:
            print("Expenses: ")
            with open(file_name, "r") as f:
                for line in f:
                    line = line.strip()
                    category, amount, date = line.split(",")
                    self.add_expense(category, int(amount), date)
                    print(line)
        except FileNotFoundError:
            print(f"File does not exist")
        
    def generate_report(self):
        for expense in self.expenses:
            yield f"Category: {expense.category} | Amount: ${expense.amount} | Date: {expense.date}"
    
tracker = ExpenseTracker()
tracker.add_expense("Food", 250, "01-01-2025")
tracker.add_expense("Transport", 100, "02-01-2025")
tracker.add_expense("Food", 180, "03-01-2025")
tracker.add_expense("Shopping", 500, "04-01-2025")

tracker.view_all()
tracker.view_by_category("Food")
tracker.total_spending()
tracker.most_expensive_category()
tracker.search_by_range(100, 300)
tracker.save_to_file("expenses.txt")
tracker.load_from_file("expenses.txt")

for report in tracker.generate_report():
    print(report)

