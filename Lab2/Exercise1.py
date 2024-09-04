# Write Python code that uses the input built-in function to ask the user to enter a whole number between 1 and 100. The input function always returns a string value, so use the int built-in function to convert the value entered to an integer data type and square the number that the user entered using the exponentiation operator. Print a message to the user stating the value that they entered and the square of the value that they entered. Author: Ethan Foust Date: 9/4/24

value_entered = input("please enter a value between 1 and 100:  ");
value_squared = int(value_entered)**2
print ("the value squared = ", value_squared)
