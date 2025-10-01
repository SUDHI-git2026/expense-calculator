def add_expense():
    description = input("Enter expense description: ")
    amount = input("Enter amount: ")

    file = open("expense cal.txt", "a")
    file.write(description + "\n")
    file.write(amount + "\n")
    file.close()

    print("Expense added successfully...")


def view_expenses():
    print("\n   All Expenses    ")
    file = open("expense cal.txt", "r")

    count = 1
    lines = []
    for line in file:
        lines.append(line)
    file.close()

    i = 0
    while i < len(lines) - 1:
        description = lines[i]
        amount = lines[i+1]
        print(str(count) + ". Description:", description, end="")
        print("   Amount:", amount, end="")
        print()
        count = count + 1
        i = i + 2
    print()


def calculate_total():
    total = 0
    file = open("expense cal.txt", "r")

    lines = []
    for line in file:
        lines.append(line)
    file.close()

    i = 1
    while i < len(lines):
        total = total + int(lines[i])
        i = i + 2

    print("\n   Total Expenses =", total, "\n")


def main():
    while True:
        print("    Expense Tracker   ")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_total()
        elif choice == "4":
            print("Exiting - Goodbye! 👋")
            break
        else:
            print("Wrong choice. Please try again.")


main()





