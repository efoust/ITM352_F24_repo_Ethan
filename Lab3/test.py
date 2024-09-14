
#Return the smaller value(minValue)
def minValue(num1, num2):
    return (num1 < num2) * num1 + (num2 <= num1) * num2
num1 = float(input("inout a value to be evalueated: "))
num2 = float(input("inout a value to be evalueated: "))
print(minValue(num1,num2))