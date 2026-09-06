from datetime import date
from storage import save_transactions

def add_transaction(transactions):
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
    save_transactions(transactions)

def view_transactions(transactions):

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

def search_transactions(transactions):

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

def delete_transaction(transactions):

    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a numeric value.")
        return

    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            save_transactions(transactions)
            print("Transaction deleted successfully!")
            return

    print("Transaction not found.")

def view_balance(transactions):

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

def spending_summary(transactions):

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
