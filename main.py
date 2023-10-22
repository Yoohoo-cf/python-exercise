# Exercises Module 6.2

import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("How many sides are you playing on this dice? "))
    rolls = 0

    while True:
        result = roll_dice(sides)
        rolls += 1
        print(f"Roll {rolls}: {result}")

        if result == sides:
            break

main()











