#Read in a csv file containing the real estate data in NYC and turn it into a dataFrame
import pandas as pd
df_homes = pd.read_csv("../homes_data.csv")

#Print Dimensions of the data in the first 10 rows
shape = df_homes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns")

print("first 10 rows:\n", df_homes.head(10))
