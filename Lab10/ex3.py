import pandas as pd
data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
   'Age': [25, 30, 35, 40, 22],
   'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
   'Salary': [70000, 80000, 120000, 90000, 60000]
}

#convert the dict to a pandas DataFrmae
df = pd.DataFrame(data)

#print the dataframw
print("DataFra,e:\n ",df)
