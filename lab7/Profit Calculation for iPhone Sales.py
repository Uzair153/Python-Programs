def profitcalc():
    while True:
        cost = float(input("Enter the item's wholesale cost: $"))
        if cost < 0:
            print("ERROR: The cost cannot be negative.")
        else:
            profit = cost * 2.5
            print(f"Profit price: ${profit:.2f}.")
            return

def main():
    while True:
        profitcalc()
        choice = input("Do you have another item? (Enter 'y' for yes): ")
        if choice.lower() != 'y':
            break

main()
