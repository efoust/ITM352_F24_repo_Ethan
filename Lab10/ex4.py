import pandas as pd

#read json file of taxi trip data and create a dataframe from it

results_df = pd.read_json("Taxi_Trips.json")
print(results_df.describe())
print(results_df.head(10))

print("the median fare value is: ", results_df['fare'].median())

