import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def display_menu(self):
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Spending Patterns")
        print("4. Exit")

    def add_expense(self):
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")

        expense = {
            'description': description,
            'amount': amount,
            'category': category,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        self.expenses.append(expense)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("\nExpenses:")
            for expense in self.expenses:
                print(f"{expense['date']} - {expense['description']} (${expense['amount']}) - Category: {expense['category']}")

    def view_spending_patterns(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("\nSpending Patterns:")
            categories = set(expense['category'] for expense in self.expenses)
            for category in categories:
                total_spent = sum(expense['amount'] for expense in self.expenses if expense['category'] == category)
                print(f"{category}: ${total_spent}")

    def save_data(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file)

    def load_data(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            pass

def main():
    tracker = ExpenseTracker()
    tracker.load_data()

    while True:
        tracker.display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.view_spending_patterns()
        elif choice == '4':
            tracker.save_data()
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
