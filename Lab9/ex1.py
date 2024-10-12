with open("Names.txt", mode = "r") as textFile:
    nameList = textFile.read()
    print(type(textFile))
    print(nameList)
seperatedList = nameList.split("\n")
print(seperatedList)
count = len(seperatedList)
print(f"There are {count} names in the file")