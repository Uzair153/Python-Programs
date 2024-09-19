def additionNum():
    total = 0
    for i in range(num):
        num_input = float(input(f"Enter number {i+1}: "))
        total += num_input
    print("Total sum:", total)

num = int(input("How many numbers do you want to add? "))
additionNum()
