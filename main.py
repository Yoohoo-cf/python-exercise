# Exercises Module 6.3

"""
Write a function that gets the quantity of gasoline in American gallons
and returns the number converted to litres. Write a main program that
asks for a volume in gallons from the user and converts the value to liters.
The conversion must be done by using the function. Conversions continue
until the user inputs a negative value.
"""

def gallons_to_litres(gallons):

    litres = gallons * 3.78541

    return litres


def main():
    while True:
        gallons = float(input("Enter the quantity of gasoline in American gallons: "))

        if gallons < 0:
            print("You should have a positive gallons volume.")
            break

        litres = gallons_to_litres(gallons)
        print(f"{gallons} American gallons is equal to {litres: .2f} liters.")

main()











