# Exercises Module 5

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    # Check if the user wants to quit
    if user_input == "":
        break

    else:
        number = float(user_input)
        numbers.append(number)

# Check if there are at least 5 numbers before sorting
if len(numbers) >= 5:
    # Sort the numbers in descending order
    numbers.sort(reverse=True)

    # Print the five greatest numbers
    print("The five greatest numbers are: ")
    for i in range(5):
        print(numbers[i])
else:
    print("You entered less than five numbers, so there are not enough to find the five greatest numbers.")

