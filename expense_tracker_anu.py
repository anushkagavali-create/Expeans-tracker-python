# Simple Expense Tracker
# Keeps income and expenses in a CSV file so nothing is lost when the program closes.

import csv
import os
from datetime import date, datetime

# save the file next to this script, no matter where it is run from
FILE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "transactions_anu.csv")
FIELDS = ["date", "type", "description", "amount"]


def load_transactions():
    transactions = []
    if not os.path.exists(FILE_NAME):
        return transactions

    with open(FILE_NAME, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                transactions.append({
                    "date": row["date"],
                    "type": row["type"],
                    "description": row["description"],
                    "amount": float(row["amount"]),
                })
            except (ValueError, KeyError, TypeError):
                # skip any broken line instead of crashing
                print("Skipped a bad line in the file.")
    return transactions


def save_transactions(transactions):
    with open(FILE_NAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for t in transactions:
            writer.writerow(t)


def ask_amount():
    while True:
        text = input("Amount: ").strip()
        try:
            amount = float(text)
        except ValueError:
            print("Please enter a number, like 25 or 12.50")
            continue
        if amount <= 0:
            print("Amount must be more than 0.")
            continue
        return round(amount, 2)


def ask_date():
    today = date.today().strftime("%Y-%m-%d")
    while True:
        text = input(f"Date (YYYY-MM-DD, press Enter for {today}): ").strip()
        if text == "":
            return today
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("That date doesn't look right. Example: 2026-11-05")


def add_transaction(transactions):
    print("\n--- Add Transaction ---")
    print("1. Income")
    print("2. Expense")
    choice = input("Choose type (1 or 2): ").strip()

    if choice == "1":
        kind = "income"
    elif choice == "2":
        kind = "expense"
    else:
        print("Invalid choice, going back to menu.")
        return

    description = input("Description: ").strip()
    if description == "":
        description = "No description"

    amount = ask_amount()
    when = ask_date()

    transactions.append({
        "date": when,
        "type": kind,
        "description": description,
        "amount": amount,
    })
    save_transactions(transactions)
    print(f"Saved {kind}: {description} (${amount:.2f})")


def view_transactions(transactions):
    print("\n--- All Transactions ---")
    if len(transactions) == 0:
        print("No transactions yet.")
        return

    print(f"{'No.':<4} {'Date':<11} {'Type':<8} {'Description':<22} {'Amount':>10}")
    print("-" * 60)
    number = 1
    # show oldest first (dates are YYYY-MM-DD so normal sorting works)
    for t in sorted(transactions, key=lambda x: x["date"]):
        print(f"{number:<4} {t['date']:<11} {t['type']:<8} {t['description'][:22]:<22} {t['amount']:>10.2f}")
        number += 1


def show_summary(transactions):
    total_income = 0
    total_expenses = 0
    biggest = None

    for t in transactions:
        if t["type"] == "income":
            total_income += t["amount"]
        else:
            total_expenses += t["amount"]
            if biggest is None or t["amount"] > biggest["amount"]:
                biggest = t

    balance = total_income - total_expenses

    print("\n--- Summary ---")
    print(f"Total income:   ${total_income:.2f}")
    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Balance:        ${balance:.2f}")

    if biggest is not None:
        print(f"Biggest expense: {biggest['description']} (${biggest['amount']:.2f})")
    if balance < 0:
        print("Careful, you have spent more than you earned!")


def main():
    transactions = load_transactions()
    print("=== Expense Tracker ===")

    while True:
        print("\n1. Add transaction")
        print("2. View all transactions")
        print("3. Show summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            show_summary(transactions)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Please enter a number from 1 to 4.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
