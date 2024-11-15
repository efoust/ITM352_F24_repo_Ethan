#create a scatter plot of fares and tips from the json file. 
import matplotlib.pyplot as plt
import pandas as pd

datafileName = "../Trips_Fri07072017T4 trip_miles gt1.json"
trips_df = pd.read_json(datafileName)

fares_series = trips_df.fare
trips_series = trips_df.tips

fig = plt.figure()

plt.plot(fares_series, trips_series,marker=".", linestyle = "none")
plt.title("Tips by Fare")
plt.xlabel("Fare in $")
plt.ylabel("Tips in $")
plt.show()