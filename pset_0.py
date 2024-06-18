import numpy

#Write a program that does the following in order:
#1. Asks the user to enter a number “x”
x = int(input("Please, write a number for x: "))

#2. Asks the user to enter a number “y”
y = int(input("Please, write a number for y: "))
#3. Prints out number “x”, raised to the power “y”.
result = x**y
print(x, "raised to the power of", y, "is equal to", result)

#4. Prints out the log (base 2) of “x”.
print("log(" + str(x) + ") = " + str(numpy.log(x)))