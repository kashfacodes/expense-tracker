expenses = []


def add_expense():
    name = input("What did you spend on? ")

    try:
        amount = float(input("How much did you spend? ₹"))
    except ValueError:
        print("Please enter a valid number.")
        return

    category = input("Category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    with open("expenses.txt", "a") as file:
        file.write(f"{name},{amount},{category}\n")

    print("Expense added successfully! ✅")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        print("\nYour Expenses:")

        for i, expense in enumerate(expenses, start=1):
            print(
                f"{i}. {expense['name']} - ₹{expense['amount']} - {expense['category']}"
            )


def show_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print(f"Total spent: ₹{total}")


def spending_by_category():
    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    print("\nSpending by category:")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount}")


def delete_expense():
    view_expenses()

    if len(expenses) == 0:
        return

    try:
        number = int(input("Enter the expense number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(expenses):
        print("Invalid expense number.")
        return

    deleted = expenses.pop(number - 1)

    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(
                f"{expense['name']},{expense['amount']},{expense['category']}\n"
            )

    print(f"{deleted['name']} deleted successfully! 🗑️")


# Load saved expenses
with open("expenses.txt", "r") as file:
    for line in file:
        if line.strip():
            name, amount, category = line.strip().split(",")

            expense = {
                "name": name,
                "amount": float(amount),
                "category": category
            }

            expenses.append(expense)


# Main menu
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Spending by category")
    print("5. Delete expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        spending_by_category()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")