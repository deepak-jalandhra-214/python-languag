import csv

expenses = []


def load_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                expense = {
                    "name": row[0],
                    "amount": float(row[1])
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass


def save_expense(expense):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            expense["name"],
            expense["amount"]
        ])


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    save_expense(expense)

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['name']} - ₹{expense['amount']}")


def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense = ₹{total}")


# Program start
load_expenses()


while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")