import csv
from datetime import datetime

expenses = []


# Load expenses from CSV
def load_expenses():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                expense = {
                    "name": row[0],
                    "amount": float(row[1]),
                    "category": row[2],
                    "date": row[3]
                }

                expenses.append(expense)

    except FileNotFoundError:
        pass


# Save all expenses to CSV
def save_all_expenses():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for expense in expenses:
            writer.writerow([
                expense["name"],
                expense["amount"],
                expense["category"],
                expense["date"]
            ])


# Add expense
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    date = datetime.now().strftime("%d-%m-%Y")

    expense = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_all_expenses()

    print("Expense added successfully!")


# Show all expenses
def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n--- Your Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} - "
            f"₹{expense['amount']} - "
            f"{expense['category']} - "
            f"{expense['date']}"
        )


# Calculate total expense
def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expense = ₹{total}")


# Delete expense
def delete_expense():
    show_expenses()

    if len(expenses) == 0:
        return

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_all_expenses()

            print(f"{deleted['name']} deleted successfully!")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Edit expense
def edit_expense():
    show_expenses()

    if len(expenses) == 0:
        return

    try:
        number = int(input("Enter expense number to edit: "))

        if 1 <= number <= len(expenses):

            expense = expenses[number - 1]

            print("\nLeave blank if you don't want to change it.")

            name = input(f"Enter new name ({expense['name']}): ")
            amount = input(f"Enter new amount ({expense['amount']}): ")
            category = input(
                f"Enter new category ({expense['category']}): "
            )

            if name != "":
                expense["name"] = name

            if amount != "":
                expense["amount"] = float(amount)

            if category != "":
                expense["category"] = category

            save_all_expenses()

            print("Expense updated successfully!")

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid value.")


# Search expense
def search_expense():
    keyword = input("Enter name or category to search: ").lower()

    found = False

    print("\n--- Search Results ---")

    for i, expense in enumerate(expenses, start=1):

        if (
            keyword in expense["name"].lower()
            or keyword in expense["category"].lower()
        ):
            print(
                f"{i}. {expense['name']} - "
                f"₹{expense['amount']} - "
                f"{expense['category']} - "
                f"{expense['date']}"
            )

            found = True

    if not found:
        print("No matching expense found.")


# Category-wise summary
def category_summary():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n--- Category Summary ---")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")


# Load previous expenses
load_expenses()


# Main menu
while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Search Expense")
    print("7. Category Summary")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        edit_expense()

    elif choice == "6":
        search_expense()

    elif choice == "7":
        category_summary()

    elif choice == "8":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")