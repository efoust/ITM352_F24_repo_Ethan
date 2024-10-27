#Read a file from a url and write a local file "sales_data_test.csv"
#containing just the first 10 rows of data
import pandas as pd
import pyarrow #not needed?
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#import the datafile. This should be downloaded to be used by pandas. it is in csv format. 
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
#attepmt to read the csv file
try:
    print("Reading csv file")
#reads the csv file using the variable url, onBadLines skips the bad data or lines without values. 
    sales_data = pd.read_csv(url, dtype_backend = 'pyarrow', on_bad_lines="skip")
#ask pandas to parse the order_data field into a standard representation 
#replace order date with a cleaner version
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format = 'mixed')

#save the first 10 rows of the data into sales_data_test.csv
    sales_data.head(10).to_csv('sales_data_test.csv')
except Exception as e:
    print(f"An error has occured: {e}")

