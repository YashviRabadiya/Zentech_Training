
import random

banks = {
    "B01": {"name": "SBI"},
    "B02": {"name": "HDFC"},
    "B03": {"name": "ICICI"}
}

users = {
    "123456789012": {
        "name": "Yashvi",
        "pin": "1234",
        "bank_id": "B01",
        "balance": 50000
    },
    "234567890123": {
        "name": "Rahul",
        "pin": "5678",
        "bank_id": "B02",
        "balance": 30000
    },
    "345678901234": {
        "name": "Priya",
        "pin": "9876",
        "bank_id": "B03",
        "balance": 40000
    }
}

atms = {
    "ATM01": {"bank_id": "B01", "cash": 100000},
    "ATM02": {"bank_id": "B02", "cash": 80000},
    "ATM03": {"bank_id": "B03", "cash": 60000}
}


# Some limits for transactions

SINGLE_LIMIT = 10000
DAILY_LIMIT = 30000
MAX_TRANSACTIONS = 5
OTHER_BANK_CHARGE = 0.05

transaction_count = {card: 0 for card in users}
withdrawn_today = {card: 0 for card in users}
transaction_history = {card: [] for card in users}


def display_banks():
    print("\nAvailable Banks:")

    for bank_id, bank in banks.items():
        print(bank_id, "-", bank["name"])


def display_atms():
    print("\nAvailable ATMs:")

    for atm_id, atm in atms.items():
        bank = banks[atm["bank_id"]]["name"]
        print(atm_id, "-", bank, "ATM | Cash:", atm["cash"])


def authenticate():
    card = input("\nEnter your card number: ")

    if card not in users:
        print("Card number not found!")
        return None

    for i in range(3):
        pin = input("Enter your PIN: ")

        if pin == users[card]["pin"]:
            print("\nWelcome", users[card]["name"])
            return card

        else:
            print("Wrong PIN!")
            print("Attempts left:", 2 - i)

    print("Too many wrong attempts. Login failed.")
    return None


def account_information(card):
    user = users[card]
    bank = banks[user["bank_id"]]["name"]

    print("\n----- Account Details -----")
    print("Name:", user["name"])
    print("Card Number:", card)
    print("Bank:", bank)
    print("Balance: ₹", user["balance"])
    print("Transactions:", transaction_count[card])
    print("Total Withdrawn: ₹", withdrawn_today[card])

    remaining = DAILY_LIMIT - withdrawn_today[card]
    print("Remaining Daily Limit: ₹", remaining)


def show_transaction_history(card):
    print("\n----- Transaction History -----")

    history = transaction_history[card]

    if len(history) == 0:
        print("No transactions found.")

    else:
        for i, item in enumerate(history, 1):
            print(i, item)


def check_transaction_limit(card):

    if transaction_count[card] >= MAX_TRANSACTIONS:
        print("You have reached the transaction limit.")
        return False

    return True


def withdraw_money(card, atm_id):
    user = users[card]
    atm = atms[atm_id]

    amount = input("Enter amount to withdraw: ")

    if not amount.isdigit():
        print("Enter a valid amount!")
        return

    amount = int(amount)

    if amount <= 0:
        print("Amount should be greater than zero.")
        return

    if amount > SINGLE_LIMIT:
        print("You cannot withdraw more than ₹", SINGLE_LIMIT)
        return

    if not check_transaction_limit(card):
        return

    remaining = DAILY_LIMIT - withdrawn_today[card]

    if amount > remaining:
        print("Daily limit exceeded!")
        print("You can withdraw only ₹", remaining)
        return

    if atm["cash"] < amount:
        print("Sorry, ATM does not have enough cash.")
        return

    # Charges are applied only when using another bank's ATM
    fee = 0

    if user["bank_id"] != atm["bank_id"]:
        fee = amount * OTHER_BANK_CHARGE

    total = amount + fee

    if user["balance"] < total:
        print("Not enough balance in your account.")
        return

    # Updating balances
    user["balance"] = user["balance"] - total
    atm["cash"] = atm["cash"] - amount

    withdrawn_today[card] += amount
    transaction_count[card] += 1

    transaction_history[card].append(
        f"Withdrawn ₹{amount} | Charges ₹{fee}"
    )

    print("\nWithdrawal Successful!")
    print("Cash received: ₹", amount)
    print("Bank charges: ₹", fee)
    print("Total deducted: ₹", total)
    print("Available balance: ₹", user["balance"])


def deposit_money(card, atm_id):
    user = users[card]
    atm = atms[atm_id]

    amount = input("Enter amount to deposit: ")

    if not amount.isdigit():
        print("Please enter a valid number.")
        return

    amount = int(amount)

    if amount <= 0:
        print("Amount should be greater than zero.")
        return

    if not check_transaction_limit(card):
        return

    user["balance"] += amount
    atm["cash"] += amount

    transaction_count[card] += 1

    transaction_history[card].append(
        f"Deposited ₹{amount}"
    )

    print("\nDeposit Successful!")
    print("Amount deposited: ₹", amount)
    print("New balance: ₹", user["balance"])


def atm_menu(card, atm_id):

    while True:
        print("\n========== ATM MENU ==========")
        print("1. Withdraw Money")
        print("2. Deposit Money")
        print("3. Account Information")
        print("4. Transaction History")
        print("5. Change ATM")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            withdraw_money(card, atm_id)

        elif choice == "2":
            deposit_money(card, atm_id)

        elif choice == "3":
            account_information(card)

        elif choice == "4":
            show_transaction_history(card)

        elif choice == "5":
            return "change"

        elif choice == "0":
            print("Thank you for using our ATM!")
            return "exit"

        else:
            print("Invalid choice. Try again.")


def start_atm():

    while True:
        print("\n========== WELCOME TO ATM ==========")

        display_atms()

        print("\n1. Use ATM")
        print("0. Shutdown ATM")

        choice = input("Enter choice: ")

        if choice == "1":

            atm_id = input("Enter ATM ID: ").upper()

            if atm_id not in atms:
                print("ATM not found!")
                continue

            card = authenticate()

            if card is None:
                continue

            while True:

                result = atm_menu(card, atm_id)

                if result == "change":

                    display_atms()
                    new_atm = input("Enter new ATM ID: ").upper()

                    if new_atm in atms:
                        atm_id = new_atm
                    else:
                        print("Invalid ATM ID!")

                else:
                    break

        elif choice == "0":
            print("ATM system shutting down...")
            break

        else:
            print("Please select a valid option.")


start_atm()
