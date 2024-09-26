myList = [
[1, 2, "abc", (1,2,3), True, ["a", 2, 3], 10, 20, 33, "howdy", False],
[1, 2, "abc", (1,2,3)],
[1, 2, "abc", (1,2,3), True]
]

if (len(myList[2]) < 5):
    print("Less than 5 elements")
elif(5 <= len(myList[2]) <= 10):
    print("Between 5 and 10 elements")
else:
    print("Greater than 11 elements")
    