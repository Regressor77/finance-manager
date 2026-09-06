from transactions import add_transaction, view_transactions, search_transactions, delete_transaction, view_balance, spending_summary
from storage import load_transactions

transactions = load_transactions()

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
            add_transaction(transactions)
        elif choice == '2':
            view_transactions(transactions)
        elif choice == '3':
            search_transactions(transactions)
        elif choice == '4':
            delete_transaction(transactions)
        elif choice == '5':
            view_balance(transactions)
        elif choice == '6':
            spending_summary(transactions)
        elif choice == '7':
            print("Exiting Finance Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

main()