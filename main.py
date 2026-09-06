from datetime import date
import json

def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)

def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


transactions = load_transactions()

def add_transaction():
    transaction = {}
    current_id = 1

    for old_transaction in transactions:
        if old_transaction['id'] >= current_id:
            current_id = old_transaction['id'] + 1

    transaction['id'] = current_id

    while True:

        transaction_type = input("Enter type (income/expense): ").lower()

        if transaction_type in ['income', 'expense']:
            transaction['type'] = transaction_type
            break

        else:
            print("Invalid type. Please enter 'income' or 'expense'.")

    while True:

        try:
            transaction['amount'] = float(input("Enter amount: "))
            if transaction['amount'] <= 0:
                print("Amount must be greater than zero.")
                continue
            break

        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    transaction['category'] = input("Enter category: ")
    transaction['description'] = input("Enter description: ")
    transaction['date'] = str(date.today())

    print("Transaction added successfully!")

    transactions.append(transaction)
    save_transactions()

def view_transactions():

    if not transactions:
        print("No transactions found.")
        return
    
    print("\n======== TRANSACTIONS ========")

    for transaction in transactions:
        print(f"ID: {transaction['id']}")
        print(f"Type: {transaction['type']}")
        print(f"Amount: ₹{transaction['amount']}")
        print(f"Category: {transaction['category']}")
        print(f"Description: {transaction['description']}")
        print(f"Date: {transaction['date']}")
        print("-------------------------------")

def search_transactions():

    keyword = input("Search category or description: ").lower()

    found = False

    for transaction in transactions:
        if keyword in transaction['category'].lower() or keyword in transaction['description'].lower():
            print(f"ID: {transaction['id']}")
            print(f"Type: {transaction['type']}")
            print(f"Amount: ₹{transaction['amount']}")
            print(f"Category: {transaction['category']}")
            print(f"Description: {transaction['description']}")
            print(f"Date: {transaction['date']}")
            print("-------------------------------")
            found = True

    if not found:
        print("No matching transactions found.")

def delete_transaction():

    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            save_transactions()
            print("Transaction deleted successfully!")
            return

    print("Transaction not found.")

def view_balance():

    income = 0
    expenses = 0

    for transaction in transactions:
        if transaction['type'] == 'income':
            income += transaction['amount']
        elif transaction['type'] == 'expense':
            expenses += transaction['amount']

    balance = income - expenses

    print("\n========== BALANCE ==========")
    print(f"Total Income:  ₹{income}")
    print(f"Total Expense: ₹{expenses}")
    print(f"Balance:       ₹{balance}")

def spending_summary():

    spending = {}

    for transaction in transactions:
        if transaction['type'] == 'expense':
            category = transaction['category']

            if category not in spending:
                spending[category] = 0

            spending[category] += transaction['amount']

    if not spending:
        print("No expenses found.")
        return

    print("\n========== SPENDING SUMMARY ==========")
    for category, amount in spending.items():
        print(f"{category}: ₹{amount}")

def main():

    while True:
        print("\n========== FINANCE MANAGER ==========")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Search Transactions")
        print("4. Delete Transaction")
        print("5. View Balance")
        print("6. Spending Summary")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            search_transactions()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            view_balance()
        elif choice == '6':
            spending_summary()
        elif choice == '7':
            print("Exiting Finance Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

main()