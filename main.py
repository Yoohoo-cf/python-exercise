
# Exercises Module 6.6

import math
def d(dia,price):
    return price/math.pi*(dia/2)**2

pizzal_diameter=float(input("Enter the diameter of the pizza 1st(in cm):"))
price_of_pizza1=float(input("enter the price of the pizza 1st in euros):"))
d(pizzal_diameter,price_of_pizza1)
pizza2_diameter=float(input("Enter the diameter of the pizza 2nd(in cm):"))
price_of_pizza2=float(input("Enter the price of the pizza 2nd(in euros):"))
d(pizza2_diameter,price_of_pizza2)
if d(pizzal_diameter,price_of_pizza1)<d(pizza2_diameter,price_of_pizza2):
    print("The 1st pizza is a better option")

else:
    print("The 2nd pizza is a better option")




