import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#create a bar chart historgam from the trip miles data found in the json file. 
datafileName = "../Trips from area 8.json"
trips_df = pd.read_json(datafileName)
#drop rows with empty values
trips_df = trips_df.dropna()
#sum of the tips(currently saved as strings)
#Grab trips and payment columns from dataframe
trips_df = trips_df[['tips','payment_type']]
trips_df = trips_df.astype({"tips": float})
#set index
trips_df = trips_df.set_index('payment_type')

#sum tips per payment type
tips_by_payment_type = trips_df.groupby('payment_type').sum()

x_labels = pd.Series(tips_by_payment_type.index.values)
y_values = pd.Series(tips_by_payment_type['tips'].values)
#create labels and ticks for the bars
bars = np.array(range(len(x_labels)))
plt.xticks(bars, x_labels, color = "red", fontweight = 'bold')

plt.bar(bars, y_values)

plt.title("Taxi Tips by Payment Type")
plt.xlabel("Payment Type")
plt.ylabel("Tips in $")
plt.show()
