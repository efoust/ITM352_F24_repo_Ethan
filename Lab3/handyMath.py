#helpful math functions

#find the midpoint of 2 numbers
def midpoint(num1,num2):
    return ((num1+num2)/2)
number1 = input("enter first value: ")
number2 = float(input("enter second value: "))
number1 = float(number1)

mid = midpoint(number1,number2)
print("The midpoint is: ", mid)


#return squareroot of the inputted number
num1 = float(input("enter value to find the square root of: "))
def squareroot(num1):
    return (num1**0.5)
print(squareroot(num1))

#return the value of a exponential function. 
num1 = float(input("enter value to find the exponent of: "))
num2 = float(input("enter the value of your exponent: "))
def exponent(num1,num2):
    return (num1**num2)
print(exponent(num1,num2))

#Return the bigger value(maxValue)
def maxValue(num1, num2):
    return (num1 > num2) * num1 + (num2 >= num1) * num2
num1 = float(input("inout a value to be evalueated: "))
num2 = float(input("inout a value to be evalueated: "))
print(maxValue(num1,num2))
