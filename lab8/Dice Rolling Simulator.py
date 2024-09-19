import random

def roll_dice():
    print("Rolling the dice...")
    print("Their values are:")
    for _ in range(3):
        print(random.randint(1, 6))
    return input("Roll them again? (y = yes): ").lower() == 'y'

while roll_dice():
    pass
