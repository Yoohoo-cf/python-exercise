# Exercises 6.5

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


