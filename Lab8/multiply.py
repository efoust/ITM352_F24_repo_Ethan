#algorithm for multiplying two numbers
def multiply(x, y):
    product = 0
    for z in range(y):
        product = product + x
    return product

first = int(input("enter the first number: "))
second = int(input("enter the second number: "))
prod = multiply(first, second)
print(f"the product of {first} and {second} is {prod}")

