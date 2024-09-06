#user imputs temperature in degrees fahrenheit 
#convert temperature to celsius and output it

#function to convert ferinheight to celcius
def FtoC(temperatureF):
    degreesC = (float(degreesF) - 32) * (5/9)
    return(degreesC)


degreesF = input("Enter a temperature in fahrenheit: ")

print("this converts to ", FtoC(degreesF), "Celcius")

