import random

def coin_toss():
    for _ in range(10):
        if random.randint(1, 2) == 1:
            print("Heads")
        else:
            print("Tails")

coin_toss()
