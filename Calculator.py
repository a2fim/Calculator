#Calculater done by Abdelrahman Mobarak
import math

print("Select one of the following operations: ")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.SQUARE ROOT")
print("6.RAISE TO POWER")

operation = input()

if operation == "1":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("The result is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("The result is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("The result is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("The result is " + str(int(num1) / int(num2)))
elif operation == "5":
    num = input("enter number: ")
    print("The result is %f" % (math.sqrt(int(num))))
elif operation == "6":
    num = input("enter number: ")
    print("The result is %d" % (math.pow(int(num), 2)))
else:
    print("Incorrect input")
