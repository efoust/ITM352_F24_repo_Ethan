#create a list of trip durations in miles

tripDuration = [1.1, 0.8, 2.5, 2.6]
tripFares = ("$6.25", "$5.25", "$10.50", "$8.05")

tripDictionary = {
    "miles" : tripDuration,
    "fares" : tripFares
}

print(tripDictionary)
print(tripDictionary["miles"][2],tripDictionary["fares"][2])

zippedDictionary = dict(zip(tripDuration,tripFares))
print(f"Trip Duration ={tripDuration[2]} cost = {zippedDictionary[tripDuration[2]]}")
