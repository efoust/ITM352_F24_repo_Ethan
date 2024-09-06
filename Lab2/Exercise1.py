# Write Python code that uses the input built-in function to ask the user to enter a whole number between 1 and 100. The input function always returns a string value, so use the int built-in function to convert the value entered to an integer data type and square the number that the user entered using the exponentiation operator. Print a message to the user stating the value that they entered and the square of the value that they entered. Author: Ethan Foust Date: 9/4/24

value_entered = input("please enter a value between 1 and 100: ")
int_value_entered = int(value_entered)
if((int_value_entered>0)and(int_value_entered<101)):
    value_squared = int_value_entered**2
    print("the value you entered is ",value_entered, "the value squared is ",value_squared)
else:
    print("the value you entered does not meet the specified parameters.")
