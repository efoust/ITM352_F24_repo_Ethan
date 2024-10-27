# Read a file from a URL and write a local file "sales_data_test.csv"
# containing just the first 10 rows of data
import pandas as pd
import pyarrow  # not needed here
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context
pd.set_option("display.max_columns", None)

# Import the data file.  This needs to be downloaded to be used by Pandas.  
# It is in CSV format.

def load_csv(file_path):
    # Attempt to read the CSV file  
    try:
        print("Reading CSV file...")
        start_time = time.time()
        sales_data = pd.read_csv(file_path, dtype_backend='pyarrow', on_bad_lines="skip")
        load_time = time.time() - start_time  
        print(f"File loaded in {load_time:.2f} seconds")
        print(f"Number of rows: {len(sales_data)}")
        print(f"Columns: {sales_data.columns.to_list()}")

        # List the required columns
        required_columns = ['quantity', 'order_date', 'unit_price']

        # Check for missing columns
        missing_columns = [col for col in required_columns if col not in sales_data.columns]

        if missing_columns:
            print(f"\nWarning: The following required columns are missing: {missing_columns} ")
        else:
            print(f"\nAll required columns are present")

        # Ask Pandas to parse the order_date field into a standard representation
        sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format="mixed")

        # Save the first 10 rows of the data in sales_data_test.csv
        sales_data.head(10).to_csv('sales_data_test.csv')

        return sales_data

    except Exception as e:
        print(f"An error has occurred: {e}")


# Call load_csv to load the file
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
#local_file = "sales_data_test.csv"
sales_data = load_csv(url)

if sales_data is not None:
    print(sales_data.head())
else:
    print(f"Failed to load the CSV file {url}")