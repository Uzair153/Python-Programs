'''Write a code to accept 3 test score and display them for a student. Use a while loop for this code.
Sample output:

Enter test score: 90
Test score you entered is : 90
Enter test score: 80
Test score you entered is 80
Enter test score: 85
Test score you entered is 85'''


# Initialize a counter to keep track of the number of test scores entered
count = 0

# Loop until 3 test scores are entered
while count < 3:
    # Ask the user to input a test score
    score = input("Enter test score: ")
    
    # Display the entered test score
    print("Test score you entered is:", score)
    
    # Increment the counter
    count += 1
