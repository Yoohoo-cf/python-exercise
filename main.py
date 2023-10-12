# Exercises Module 6.5

"""
Write a function that gets a list of integers as a parameter.
The function returns a second list that is otherwise the same as the original list
except that all uneven numbers have been removed. For testing, write a main program
where you create a list, call the function, and then print out both the original
as well as the cut-down list.
"""

def remove_odd_list(list):

    even_list = []

    for x in list:
        if x % 2 == 0:
            even_list.append(x)

    return even_list

def main():
    list = [5, 7, 90, 23, 56, 70]

    even_list = remove_odd_list(list)

    print(f"The original list is: {list}")
    print(f"The list has been remove uneven number is: {even_list}")

main()


