#Create a pivot table, aggegrating sales by region with columns defined by order_type(which is either retail or wholesale)
import pandas as pd

sales_data = pd.read_csv("../sales_data.csv").convert_dtypes(dtype_backend="pyarrow")

#Create pivot table
pivot = sales_data.pivot_table(
    values = 'sale_price', index='sales_region', columns='order_type',
    aggfunc='sum', margins=True, margins_name="Totals"
)

sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format = 'mixed')

#set the display.max_columns colums to None, to force display of all columns
pd.set_option("display.max_columns", None)
print(sales_data.head(5))

print("\nPivot Table:\n", pivot)
