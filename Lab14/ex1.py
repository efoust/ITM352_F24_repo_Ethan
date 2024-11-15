 #create a histogram from the trip miles data

import matplotlib.pyplot as plt
import pandas as pd

datafileName = "../Trips from area 8.json"
#read the datafile and create a dataframe.
trips_df = pd.read_json(datafileName)
trip_miles_series = trips_df.trip_miles

fig = plt.figure()#Not strictly necessary somce plt.hist below will create a figure object 


#create the histogram
plt.hist(trip_miles_series)
plt.title("Distribution of trip Miles")
plt.xlabel("Trip Miles")
plt.ylabel("Frequency")

plt.show() 