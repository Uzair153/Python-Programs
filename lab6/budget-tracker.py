'''Write a program that asks the user to enter the amount that he or she has budgeted for a
month. A loop should then prompt the user to enter each of his or her expenses for the
month, and keep a running total. When the loop finishes, the program should display the
amount that the user is over or under budget'''


# Ask the user to input the budget for the month
budget = float(input("Enter your budget for the month: "))

# Initialize a variable to keep track of total expenses
total_expenses = 0

# Loop to prompt the user to enter each expense
while True:
    expense = input("Enter your expense for the month (or 'done' to finish): ")
    if expense.lower() == 'done':
        break
    else:
        # Convert the expense to a float and add it to total expenses
        total_expenses += float(expense)

# Calculate the difference between budget and total expenses
difference = total_expenses - budget

# Display the result
if difference > 0:
    print(f"You are over budget by ${difference:.2f}.")
elif difference < 0:
    print(f"You are under budget by ${-difference:.2f}.")
else:
    print("You have spent exactly your budget for the month.")
