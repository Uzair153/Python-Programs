'''Your friend Chris wants you to convert Fahrenheit (F) to celsius (C). She has asked you to write a program that displays a table of temperature in C with their values converted to F.  The formula for converting C to F is F =((9/5)*C + 32).   After thinking about this table of values, you decide that you will write a for loop. The list of values that the loop will iterate over will be Celsius(C). In the loop   you will call the range function like this: range(10, 51, 5) . Notice that the third argument specifies 5 as the step value. This means that the numbers in the list will be 10, 15, 20, and so forth. The second
argument specifies 51 as the sequence’s ending limit, so the last number in the sequence will be 50. Inside the loop you will use the target variable to calculate a Fahrenheit'''


# Loop over a range of temperatures in Celsius
for celsius in range(10, 51, 5):
    # Convert Celsius to Fahrenheit
    fahrenheit = (9/5) * celsius + 32
    
    # Display the converted temperature
    print(f"Celsius: {celsius}, Fahrenheit: {fahrenheit}")
