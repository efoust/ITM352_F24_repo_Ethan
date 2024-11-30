#create a scatter plot of fares and tips from the json file. 
import matplotlib.pyplot as plt
import pandas as pd

datafileName = "../Trips from area 8.json"
trips_df = pd.read_json(datafileName)
trip_miles_gt_0 = trips_df[['trip_miles','fare']].query('trip_miles > 0')
fares_series = trip_miles_gt_0.fare
trip_miles = trip_miles_gt_0.trip_miles



plt.plot(fares_series,trip_miles, marker = "v",linestyle = "none", color = "c", alpha = 0.2)
plt.title("Tips by Fare")
plt.xlabel("Fare in $")
plt.ylabel("Tips in $")


plt.savefig("FaresXMiles.png", dpi=300)
plt.show()