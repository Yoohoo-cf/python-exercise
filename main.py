# Exercises 6.3

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











