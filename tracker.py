# Expense_Tracker

import datetime
import csv
import os

FILENAME = 'expenses.csv'

def load_expenses():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ['Date', 'Category', 'Amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expenses:
            writer.writerow(exp)

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date == '':
        date = str(datetime.date.today())
    category = input("Enter category: ")
    amount = input("Enter amount: ")

    expense = {'Date': date, 'Category': category, 'Amount': amount}
    return expense

def view_expenses(expenses):
    if not expenses:
        print("No expenses to show.")
        return
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['Date']} - {exp['Category']} - ₹{exp['Amount']}")

def monthly_summary(expenses):
    summary = {}
    for exp in expenses:
        cat = exp['Category']
        amount = float(exp['Amount'])
        summary[cat] = summary.get(cat, 0) + amount
    print("---- Monthly Summary ----")
    for cat, amt in summary.items():
        print(f"{cat}: ${amt:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Save & Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            expenses.append(add_expense())
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            monthly_summary(expenses)
        elif choice == '4':
            save_expenses(expenses)
            print("Expenses saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
