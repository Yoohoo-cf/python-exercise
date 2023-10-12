# Exercises Module 5

num = int(input("Enter a number to check if it is a prime number: "))

if num > 1:
    is_prime = True
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number")

    else:
        print(num, "is not a prime number")

else:
    print(num, "is not a prime number")