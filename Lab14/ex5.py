import matplotlib.pyplot as plt
import pandas as pd

#different plot styles
plt.style.use('ggplot')
#plt.style.use("fivethirtyeight")

datafileName = "../Trips from area 8.json"
trips_df = pd.read_json(datafileName)
trip_miles_gt_0 = trips_df[['trip_miles','fare']].query('trip_miles > 2')


fares_series = trip_miles_gt_0.fare
trip_miles = trip_miles_gt_0.trip_miles

plt.plot(fares_series,trip_miles, marker="o", linestyle = "none", alpha=0.3)
plt.title("Fares by taxi trip miles > 2")
plt.xlabel("Fare in $")
plt.ylabel("Distance in Miles")

plt.legend()
plt.savefig("FaresXMiles2.png", dpi=300)
plt.show()

