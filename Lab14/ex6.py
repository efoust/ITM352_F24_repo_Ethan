import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
file_name = "../Trips from area 8.json"
trips_df = pd.read_json(file_name)
trips_gt_1 = trips_df[['trip_miles','fare','dropoff_community_area']].query('trip_miles > 1')

fare_series = trips_gt_1.fare
trip_miles = trips_gt_1.trip_miles
dropoff_area = trips_gt_1.dropoff_community_area

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
#put fare series on x axis, miles on the Y, dropoff area on Z axis
ax.scatter(fare_series,trip_miles, dropoff_area, c = 'b', marker ='.' )

plt.savefig("FaresXMiles3.png", dpi=300)
