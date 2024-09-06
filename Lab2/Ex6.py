#Ask the user to enter their weight in pounds. convert to kilos and output value. 

weightInPounds = input("please enter your weight in pounds: ")
weightInPounds = float(weightInPounds)
poundsToKilos = 0.453592 
weightInKilos = weightInPounds * poundsToKilos
print("You weigh ", round(weightInKilos,1), " kilos")