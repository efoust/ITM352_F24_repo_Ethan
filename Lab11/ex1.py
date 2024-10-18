import pandas as pd

sales_data = pd.read_csv("../sales_data.csv").convert_dtypes(dtype_backend="pyarrow")


sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format = 'mixed')

#set the display.max_columns colums to None, to force display of all columns
pd.set_option("display.max_columns", None)
print(sales_data.head(5))
