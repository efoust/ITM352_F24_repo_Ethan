#playing around with strings
firstName = input("input your first name: ")
middleName = input("input your middle name: ")
lastName = input("input your last name: ")
#print(firstName + " " + middleName + " " + lastName)
#print(f"{firstName} {middleName} {lastName}")
#print(("My name is %s %s %s") % (firstName, middleName, lastName))
#print("My Name is {} {} {}".format(firstName, middleName, lastName))

names = [firstName, middleName, lastName]
#fullName = " ".join(names)
#print(fullName)

formattedString = "My name is {} {} {}, I am 21 years old.".format(*names)
print(formattedString)

