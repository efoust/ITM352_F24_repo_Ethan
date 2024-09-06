#user imputs temperature in degrees fahrenheit 
#convert temperature to celsius and output it
degreesF = input("Enter a temperature in fahrenheit: ")

degreesC = (float(degreesF) - 32) * (5/9)

print("this converts to ", degreesC, "Celcius")