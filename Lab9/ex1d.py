#

with open("Names.txt", mode = "r") as textFile:
    line = textFile.readline()
    count = 0
    while line: 
        count += 1
        print(line)
        line = textFile.readline()
       

print(f"There are {count} names in the file.")