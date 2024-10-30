#grab info from the us treasury and get a table of interest rate data and store it as a datafraome

import urllib.request
import ssl
import pandas as pd
import pyarrow


ssl._create_default_https_context=ssl._create_unverified_context
pd.set_option("display.max_columns",None)

url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

#open the web page
print(f"Opening {url}...")
try:
    tables = pd.read_html(url)
    int_rate_table = tables[0]
    print(int_rate_table.columns)
    print(int_rate_table.head())

    for index, row in int_rate_table.iterrows():
        print(f"Index: {index}: 1 month rate: {row['1 Mo']}")
except Exception as e:
    print(f"An error has occured: {e}")
