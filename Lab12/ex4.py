# Extract JSON data from data.cityofchicago.org on vehicles and their fuel sources.
import pandas as pd
from sodapy import Socrata

# Initialize the Socrata client
client = Socrata("data.cityofchicago.org", None)

results = client.get("rr23-ymwb", limit=500)

# Print the results as stored in the DataFrame
results_df = pd.DataFrame.from_records(results)
print("API call results:")
print(results_df.head())

# Look at just the vehicle number and fuel source
vehicles_and_fuel_sources = results_df[["public_vehicle_number", "vehicle_fuel_source"]]
print(f"Vehicles and fuel sources\n {vehicles_and_fuel_sources}")

vehicles_by_group = vehicles_and_fuel_sources.groupby("vehicle_fuel_source")
print(vehicles_by_group.count())