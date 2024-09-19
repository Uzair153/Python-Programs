total = 0

# Loop through the series from 1 to 30
for i in range(1, 31):
    # Add each term of the series to the total
    total += i / (31 - i)

print("Total of the series:", total)
