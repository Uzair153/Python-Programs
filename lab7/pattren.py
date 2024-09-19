rows = 9  # Number of rows in the pattern

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for columns
    for j in range(1, i + 1):
        print('*', end='')  # Print '*' without a newline
    print()  # Move to the next line after printing each row
