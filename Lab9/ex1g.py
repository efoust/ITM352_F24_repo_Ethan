import os

fileName = "Names.txt"

with open(fileName, mode="a") as textFile:
    textFile.write("\nDan Port")

print(textFile)
    

with open(fileName, mode = "r") as textFile:
    lines = textFile.readlines()
    count = 0
    for line in lines:
        count += 1
        print(line)
print(f"There are {count} names in the file.")
