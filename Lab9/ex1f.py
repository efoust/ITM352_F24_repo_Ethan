import os
fileName = "Names.txt"
if os.path.exists(fileName) and os.access(fileName, os.R_OK):
    with open("Names.txt", mode = "r") as textFile:
     lines = textFile.readlines()
     count = 0
     for line in lines:
        count += 1
        print(line)
    print(f"There are {count} names in the file.")
else:
   print("cannot accesss file")