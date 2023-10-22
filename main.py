# Exercises Module 6.1

import random

def roll_dice():
    return random.randint(1, 6)

def main():
    rolls = 0
    while True:
        result = roll_dice()
        rolls += 1
        print(f"Roll {rolls}: {result}")

        if result == 6:
            break


main()





