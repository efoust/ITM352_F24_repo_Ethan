# Get the users birth year and subtract the current year to get their current age. 


birthyear = input("Please enter your four digit birth year: ")
birthyear = int(birthyear)
currentyear = 2024
age = currentyear - birthyear
print("You entered: ", birthyear)
print("Your age is: ", age)