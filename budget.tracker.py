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
      





rint("Invalid option. Try again.")
