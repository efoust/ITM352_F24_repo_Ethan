import pandas as pd
# List of individuals' ages
ages = [25, 30, 22, 35, 28, 40, 50, 18, 60, 45]


#Lists of individuals' names and genders
namess = ["Joe", "Jaden", "Max", "Sidney", "Evgeni", "Taylor", "Pia", "Luis", "Blanca", "Cyndi"]
gender = ["M", "M", "M", "F", "M", "F", "F", "M", "F", "F"]

dict = zip(ages, gender)
#convert the dictonary to a dataframe
df = pd.DataFrame(dict, columns=['Age', 'Gender'], index=namess)

# Summarize the DataFrame
print(df)
summary = df.describe()
print(summary)

#calc the average age by gender
average_age_bg = df.groupby('Gender')['Age'].mean()
print(average_age_bg)
