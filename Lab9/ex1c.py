

with open("Names.txt") as textFile:
    read = textFile.read()

names = read.split("\n")
name_count = 0
for name in names:
    name_count += 1
   
print(read)
print(f"Names.txt contains {name_count} names")