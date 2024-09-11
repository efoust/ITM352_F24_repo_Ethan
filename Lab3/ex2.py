#create a function called midpoint that taes two numbers as input
# returns the value halfway between them

def midpoint(num1,num2):
    return ((num1+num2)/2)

number1 = input("enter first value: ")
number2 = float(input("enter second value: "))
number1 = float(number1)


mid = midpoint(number1,number2)
print("The midpoint is: ", mid)