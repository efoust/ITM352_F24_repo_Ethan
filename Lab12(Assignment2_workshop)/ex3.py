# Read a file from a URL and write a local file "sales_data_test.csv"
# containing just the first 10 rows of data
#allow users to interactivley explore and analyze sales data from a csv file by 
# providing a simple command line interface. 
import pandas as pd
import pyarrow  
import ssl
import time


ssl._create_default_https_context = ssl._create_unverified_context

#set the display to show all columns 
#pd.set_option("display.max_columns", None)
#set the display to show all rows
pd.set_option("display.max_rows", None)

# Import the data file.  This needs to be downloaded to be used by Pandas.  
# It is in CSV format.

def load_csv(file_path):
    # Attempt to read the CSV file  
    try:
        print(f"Reading CSV file {file_path}")
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

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file {file_path} was empty.")
    except pd.errors.ParserError as e: 
        print(f"Error: there was a problem parsing {file_path}.")
    except Exception as e:
        print(f"an error has occured: {e}.")

#function to display a user-choosable number of rows. 
def display_rows(data):
    while True:
        numRows = len(data) -1 
        print("\nEnter number of rows to display")
        print(f" - Enter a number between 1 and {numRows}")
        print(" - To see all rows enter 'all'.")
        print(" - To skip press enter")
        user_choice = input("Your choice: ").strip().lower()
        
        if user_choice == '':
            print("Skipping preview")
            break
        elif user_choice == 'all':
            print(data)
            break
        elif user_choice.isdigit() and 1 <= int(user_choice) <= numRows:
            print(data.head(int(user_choice)))
            break
        else:
            print("Invalid input. Please re-enter.")




# Call load_csv to load the file
# url is the google drive link for the data
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
local_file = "sales_data_test.csv"
sales_data = load_csv(local_file)

#Main loop for user interaction
def main():
    while True:
        display_rows(sales_data)
#if this is the main program call main().
#if __name__ == "___main___":
main()

