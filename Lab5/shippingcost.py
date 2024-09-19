'''Fast Freight Shipping Co. has set its pricing based on the weight of packages as follows:
Up to 2 pounds: $1.10 per pound
More than 2 pounds, up to 6 pounds: $2.20 per pound
More than 6 pounds, up to 10 pounds: $3.70 per pound
Above 10 pounds: $3.80 per pound
Please design a program that prompts the user to input the weight of their package. The program should then calculate and display the total shipping cost. The check has to be done in a function and the main function passes the variable to the other function.'''



def calculate_shipping_cost(weight):
    if weight <= 2:
        return weight * 1.10
    elif weight <= 6:
        return weight * 2.20
    elif weight <= 10:
        return weight * 3.70
    else:
        return weight * 3.80

def main():
    weight = float(input("Enter the weight of the package in pounds: "))
    total_cost = calculate_shipping_cost(weight)
    print("The total shipping cost is: $", format(total_cost, ".2f"))

if __name__ == "__main__":
    main()
