
#Debugging exercise # 5
def fibonacci(list):
    fibValue = 0
    x = 0
    for val in list:
        fibValue = fibValue + list[x]
        x = x +1

    return fibValue

my_list = [1, 2, 3, 4, 5]
print(fibonacci(my_list)) 

