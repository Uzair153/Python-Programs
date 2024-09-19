# 50Write a script where a user can input their expected monthly income. Then, using a loop, allow them to enter various expenses until they choose to stop. Afterward, calculate and display the total expenses and the remaining amount from the income. Display a warning if expenses exceed income.

def calculate_expenses(income):
    total_expenses = 0
    while True:
        expense = float(input("Enter expense (or 0 to stop): "))
        if expense == 0:
            break
        total_expenses += expense

    remaining_income = income - total_expenses

    print("Total expenses:", total_expenses)
    print("Remaining income:", remaining_income)

    if remaining_income < 0:
        print("WARNING: Expenses exceed income!")

income = float(input("Enter expected monthly income: "))
calculate_expenses(income)
