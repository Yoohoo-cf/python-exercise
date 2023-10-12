# Exercises Module 6.4

"""
Write a function that gets a list of integers as a parameter.
The function returns the sum of all the numbers in the list.
For testing, write a main program where you create a list,
call the function, and print out the value it returned.
"""

def int_sum(list):

    total = sum(list)
    return total


def main():
    int_list = [1, 4, 5, 7, 9]
    result = int_sum(int_list)

    print(f"The sum of all the numbers in the list is: {result}")

main()












