def show_menu():
    print("\n--- Budget Tracker ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. Exit")

income = 0
expenses = 0

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter income amount: "))
        income += amount
        print("Income added.")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        expenses += amount
      print("Income added.")

    elif choice == "2":
        amount = float(input("Enter expense amount: "))
        expenses += amount
        print("Expense added.")

    elif choice == "3":
        balance = income - expenses
        print(f"Income: ${income}")
        print(f"Expenses: ${expenses}")
        print(f"Balance: ${balance}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")

import json

def show_menu():
    print("\n--- Budget Tracker ---")
    print("1. Add income")
    print("2. Add expense")
    print("3. View balance")
    print("4. Save and Exit")

# Load data from file
def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            return data["income"], data["expenses"]
    except:
        return 0, 0

# Save data to file
def save_data(income, expenses):
    data = {
        "income": income,
        "expenses": expenses
    }
    with open("data.json", "w") as file:
        json.dump(data, file)

income, expenses = load_data()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        try:
            amount = float(input("Enter income amount: "))
            income += amount
            print("Income added.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "2":
        try:
            amount = float(input("Enter expense amount: "))
            expenses += amount
            print("Expense added.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    elif choice == "3":
        balance = income - expenses
        print(f"Income: ${income}")
        print(f"Expenses: ${expenses}")
        print(f"Balance: ${balance}")

    elif choice == "4":
        save_data(income, expenses)
        print("Data saved. Goodbye!")
        break

    else:
        print("Invalid option. Try again.")
      






