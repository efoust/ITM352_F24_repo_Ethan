#helpful math functions

#find the midpoint of 2 numbers
def midpoint(num1,num2):
    return ((num1+num2)/2)
#num1 = input("enter first value: ")
#num2 = float(input("enter second value: "))
#num1 = float(num1)

#midValue = midpoint(num1,num2)
#print("The midpoint is: ", midValue)


#return squareroot of the inputted number
#num1 = float(input("enter value to find the square root of: "))
def squareroot(num1):
    return (num1**0.5)
#squarerootValue = squareroot(num1)
#print(squareroot(num1))

#return the value of a exponential function. 
#num1 = float(input("enter value to find the exponent of: "))
#num2 = float(input("enter the value of your exponent: "))
def exponent(num1,num2):
    return (num1**num2)
#exponentValue = exponent(num1,num2)
#print(exponent(num1,num2))

#Return the bigger value(maxValue)
#num1 = float(input("inout a value to be evalueated: "))
#num2 = float(input("inout a value to be evalueated: "))
def max(num1, num2):
    return (num1 > num2) * num1 + (num2 >= num1) * num2
#maxValue = max(num1,num2)
#print(max(num1,num2))


#Return the smaller value(minValue)
#num1 = float(input("inout a value to be evalueated: "))
#num2 = float(input("inout a value to be evalueated: "))
def min(num1, num2):
    return (num1 < num2) * num1 + (num2 <= num1) * num2
#minValue = min(num1,num2)
#print(min(num1,num2))
