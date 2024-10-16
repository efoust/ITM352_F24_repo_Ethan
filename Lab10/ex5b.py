#Read in a csv file containing the real estate data in NYC and turn it into a dataFrame
import pandas as pd
df_homes = pd.read_csv("../homes_data.csv")

#Print Dimensions of the data in the first 10 rows
shape = df_homes.shape
print(f"The homes data has {shape[0]} rows and {shape[1]} columns")

#select properties with 500 or more units and rop the rest
df_big_apartments = df_homes[df_homes.units >= 500]
df_big_apartments = df_big_apartments.drop(columns =['id','easement'])
print("first 10 rows:\n", df_big_apartments.head(10))