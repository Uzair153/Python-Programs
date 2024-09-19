# Write a program to convert distances in kilometers to miles. Use a `for` loop to iterate over a sequence of distances in kilometers (using `range(1, 11)`) and calculate their equivalent in miles (using the conversion factor: 1 kilometer is approximately 0.621371 miles). Display the result as a conversion table.

def km_to_miles(km):
    return km * 0.621371

print("Kilometers\tMiles")
for km in range(1, 11):
    miles = km_to_miles(km)
    print("{:9.2f}\t{:6.2f}".format(km, miles))
