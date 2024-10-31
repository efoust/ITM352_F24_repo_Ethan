# Allow users to interactively explore and analyze sales data from a CSV file by
# providing a simple command-line interface.
import pandas as pd
import pyarrow  
import ssl
import time
import sys

ssl._create_default_https_context = ssl._create_unverified_context

# Set the display to show all columns
#pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


# Import the data file.  This needs to be downloaded to be used by Pandas.  
# It is in CSV format.
def load_csv(file_path):
    # Attempt to read the CSV file  
    try:
        print(f"Reading CSV file: {file_path}")
        start_time = time.time()
        sales_data = pd.read_csv(file_path, dtype_backend='pyarrow', on_bad_lines="skip")
        load_time = time.time() - start_time  
        print(f"File loaded in {load_time:.2f} seconds")
        print(f"Number of rows: {len(sales_data)}")
        #print(f"Columns: {sales_data.columns.to_list()}")

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
        print(f"Error: the file {file_path} was not found.")
    except pd.errors.EmptyDataError as e:
        print(f"Error: the file {file_path} was empty.")
    except pd.errors.ParserError as e:
        print(f"Error: there was a problem parsing {file_path}.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

#Option 1: Function to display a number of rows set by the user. 
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

# Cleanly exit the program
def exit_program(data):
    sys.exit(0)

# Display the top-level menu of user options
def display_menu(data):
    menu_options = (
        ("Show the first n rows of data", display_rows),
        ("Show the total number of sales by region", total_sales_by_region),
        ("Average Sales per region with average sales by state and sale type", Avg_Sales),
        ("Sales by customer type and order type by state", Sales_by_customer_type),
        ("Total Sales quantity and price by region and product",Total_Sales_quantity_and_Price_by_region_and_Product),
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


#Option 2: prints the total number of sales by region and order type. 
def total_sales_by_region(data):
    try:
        pivot_table = pd.pivot_table(data, index="sales_region", columns= "order_type", values="quantity", aggfunc='sum', fill_value=0)
        pivot_table.index.name = 'Sales Region'
        pivot_table.columns = [f'{col}' for col in pivot_table.columns]
        print("\n Total Sales by Region and Order Type")
        print(pivot_table)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    
#Option 3: Average sales by region with average sales by state and order type
def Avg_Sales(data):
    try:
        pivot_table = pd.pivot_table(data, index = ['sales_region', 'customer_state','order_type'], values= 'quantity', aggfunc='mean', fill_value=0 )
        pivot_table.index.names = ['Sales Region', 'Customer State', 'Order Type']
        pivot_table.columns = ['Average Sales']
       
        print(pivot_table)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")

#Option 4: sales by customer type and order type by state. 
def Sales_by_customer_type(data):
    try:
        #creates pivot table and organizes columns using index, calculates mean of the value(quantity)
        pivot_table = pd.pivot_table(data, index = ['customer_state', 'customer_type', 'order_type'], values= 'quantity', aggfunc='sum', fill_value=0 )
        #rename the column headers(indexes)
        pivot_table.index.names = ['Customer State', 'Customer Type', 'Order Type']
        #rename the column header(value)
        pivot_table.columns = ['Total Sales']
       
        print(pivot_table)
        pivot_table.to_csv('Sales_by_customer_type.csv')
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")

#Option 5: Total Sales quantity and price by region and product. 
def Total_Sales_quantity_and_Price_by_region_and_Product(data):
    try:
        data['total_sales_price'] = data['quantity'] * data['unit_price']
        pivot_table = pd.pivot_table(data,
        index = ['sales_region', 'product_category'], 
        values = ['quantity', 'total_sales_price'],
        aggfunc= {'quantity': 'sum', 'total_sales_price': 'sum'},
        fill_value = 0)
        pivot_table.index.names = ['Sales Region', 'Product Type']
        pivot_table.columns = ['Total Quantity', 'Total Sales Price']
        print(pivot_table)
        pivot_table.to_csv('Option5.csv')
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")


# Call load_csv to load the file
url = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"

#url = 'sales_data_test.csv'
sales_data = load_csv(url)

# Main loop for user interaction
def main():
    while True:
        display_menu(sales_data)

# If this is the main program, call main()
if __name__ == "__main__":
    main()