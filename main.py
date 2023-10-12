# Exercises Module 5

import random

def rolldices():

    num_dices = int(input("How many dices do you want to run? "))

    total = 0

    for dice in range(num_dices):

        roll = random.randint(1, 6)
        total += roll

    # Prints out the sum of the numbers
    print(f"Total numbers of the dice rolls are {total} ")


rolldices()
