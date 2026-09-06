import json

def save_transactions(transactions):
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file)

def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

