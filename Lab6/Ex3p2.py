
birthYear = int(input("Enter your birth year"))
if birthYear % 4 == 0 and birthYear % 100 != 0 or birthYear % 400 == 0:
    print(f"{birthYear} is a on a leap year!")
else:
    print(f"{birthYear} is not on a leap year.")
