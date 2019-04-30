# Module 2
#   Programming Assignment 3
#     Prob-5.py

# Rachel Watson

from math import *

def main():

    Pizza= 2.00
    Drink= 1.50
    Donut= 0.56

    print("Pizza @ 2:", " ", Pizza + Pizza)

    print("Drink:", " ", " ", " ", Drink)

    print("Donut @ 2:", " ", Donut + Donut)

    print("---------------------")

    Subtotal= float(Pizza + Pizza + Drink + Donut + Donut)

    print("Subtotal:", " ", Subtotal)

    print("Tax:", " ", " ", " ", " ", .56)
    
    Tax= 0.56

    Total= Pizza + Pizza + Drink + Donut + Donut + Tax

    print()

    print("Total:", Total)

    amount = input("Please enter an amount: ")

    Tendered = float(10.00)

    print("Tendered:", Tendered)

    Change= Tendered - Total

    print("Change:", Change)

main()