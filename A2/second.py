import pandas as pd
import pyarrow
import ssl
import time
import sys

ssl._create_default_https_context = ssl._create_unverified_context

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

#load the csv file
def load_csv(file_path):
    try:
        print(f"Reading CSV file: {file_path}")
        start_time = time.time()
        sales_data = pd.read_csv(file_path, dtype_backend='pyarrow', on_bad_lines="skip")
        load_time = time.time() - start_time
        print(f"File loaded in {load_time:.2f} seconds")
        print(f"Number of rows: {len(sales_data)}")

        required_columns = ['quantity', 'order_date', 'unit_price']
        missing_columns = [col for col in required_columns if col not in sales_data.columns]
        if missing_columns:
            print(f"\nWarning: The following required columns are missing: {missing_columns} ")
        else:
            print(f"\nAll required columns are present")

        sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format="mixed")
        sales_data.head(10).to_csv('sales_data_test.csv')
        return sales_data
    except FileNotFoundError:
        print(f"Error: the file {file_path} was not found.")
    except pd.errors.EmptyDataError as e:
        print(f"Error: the file {file_path} was empty.")
    except pd.errors.ParserError as e:
        print(f"Error: there was a problem parsing {file_path}.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
#option 1:  display the number of rows of data. asks user to specfy how many rows should be displayed. 
def display_rows(data):
    while True:
        numRows = len(data) - 1
        print("\nEnter number of rows to display:")
        print(f"- Enter a number between 1 and {numRows}")
        print("- To see all rows enter 'all'")
        print("- To skip, press Enter")
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
#ends the program
def exit_program(data):
    sys.exit(0)
#displays the menu options, user picks the function they want to execute wit a number 
def display_menu(data):
    menu_options = (
        ("Show the first n rows of data", display_rows),
        ("Show the total number of sales by region", total_sales_by_region),
        ("Exit the program", exit_program)
    )
    print("\nPlease choose from among these options:")
    for index, (description, _) in enumerate(menu_options):
        print(f"{index+1}: {description}")
    num_choices = len(menu_options)
    choice = int(input(f"Select an option between 1 and {num_choices}: "))
    if 1 <= choice <= num_choices:
        action = menu_options[choice-1][1]
        action(data)
    else:
        print("Invalid input. Please re-enter.")

#option 2, prints the sales by region when requested by the user. 
def total_sales_by_region(data):
    print("\nColumns in Data:", data.columns)

    print("\nChecking for null values in 'sales_region' and 'order_type'")
    print(data[['sales_region', 'order_type']].isnull().sum())

    print("\nSample of Data:")
    print(data.head())

    try:
        pivot_table = pd.pivot_table(data, index="sales_region", columns="order_type", values="quantity", aggfunc=pd.Series.nunique)
        print("\nTotal Sales by Region and Order Type")

        print(pivot_table)
        return pivot_table
    except KeyError as e:
        print(f"Error: {e} - column missing in data")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")
#var stores the datafile as a link. 
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
sales_data = load_csv(url)
#infinite loop allowing the user to interact with the program. 
def main():
    while True:
        display_menu(sales_data)
#starts the rpogram. 
if __name__ == "__main__":
    main()
