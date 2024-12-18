#Assingment 2
import pandas as pd
import pyarrow  
import ssl
import time
import sys

ssl._create_default_https_context = ssl._create_unverified_context

# Set the display to show all columns
#pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

def load_csv(file_path):
    #read the csv file. 
    try:
        #load the file, print how long it takes to load, and the number of rows loaded, skip lines without data. 
        print(f"Reading CSV file: {file_path}")
        start_time = time.time()
        sales_data = pd.read_csv(file_path, dtype_backend='pyarrow', on_bad_lines="skip")
        load_time = time.time() - start_time  
        print(f"File loaded in {load_time:.2f} seconds")
        print(f"Number of rows: {len(sales_data)}")

        # List the required columns
        required_columns = ['quantity', 'order_date', 'unit_price']

        missing_columns = [col for col in required_columns if col not in sales_data.columns]
        #print error if columns are not found. 
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
    print("Exiting...")
    sys.exit(0)

# Display the top-level menu of user options
def display_menu(data):
    menu_options = (
        ("Show the first n rows of data", display_rows),
        ("Show the total number of sales by region", total_sales_by_region),
        ("Average Sales per region with average sales by state and sale type", Avg_Sales),
        ("Sales by customer type and order type by state", Sales_by_customer_type),
        ("Total Sales quantity and price by region and product",Total_Sales_quantity_and_Price_by_region_and_Product),
        ("Total Sales Quantity and Price by Customer Type",Total_Sales_quantity_and_Price_by_Customer_Type),
        ("Minium and Maximum Sales Price by Category",Min_Max_Sales_price_by_catagory),
        ("Number of Unique Employees by Region",Unique_employees_by_region),
        ("Custom Pivot Table", Custom_Pivot_Table),
        ("Exit the program", exit_program)    
    )
#print the menu options. 
    print("\nPlease choose from among these options:")
    for index, (description, _) in enumerate(menu_options):
        print(f"{index+1}: {description}")
#user inputs the menu option they want. 
    num_choices = len(menu_options)
    choice = int(input(f"Select an option between 1 and {num_choices}: "))
#find the chosen menu option, print error if the chosen value is not an option. 
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
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    
#Option 3: Average sales by region with average sales by state and order type
def Avg_Sales(data):
    try:
        pivot_table = pd.pivot_table(data, index = ['sales_region', 'customer_state','order_type'], values= 'quantity', aggfunc='mean', fill_value=0 )
        pivot_table.index.names = ['Sales Region', 'Customer State', 'Order Type']
        pivot_table.columns = ['Average Sales']
        print("\nAverage Sales by Region with Average Sales by State and Order Type.")
        print(pivot_table)
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
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
        print("\nSales by Customer Type")
        print(pivot_table)
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
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
        print("\nTotal Sales by Quantity and Price by Region and Product")
        print(pivot_table)
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")

#Option 6: Total Sales Quantity and price by customer type. 
def Total_Sales_quantity_and_Price_by_Customer_Type(data):
    try:
        data['total_sales_price'] = data['quantity'] * data['unit_price']
        pivot_table = pd.pivot_table(data,
        index = 'customer_type', 
        values = ['quantity', 'total_sales_price'],
        aggfunc= {'quantity': 'sum', 'total_sales_price': 'sum'},
        fill_value = 0)
        pivot_table.index.name = 'Customer Type'
        pivot_table.columns = ['Total Quantity', 'Total Sales Price']
        print("\nTotal Sales Quantity and Price by Customer Type")
        print(pivot_table)
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")


#Option 7: min and max sales price by ccatagory
def Min_Max_Sales_price_by_catagory(data):
    try:
        pivot_table = pd.pivot_table(data,
        index = 'product_category', 
        values = 'unit_price',
        aggfunc= {'unit_price': ['max','min']},
        fill_value = 0)
        pivot_table.index.name = 'Product Category'
        pivot_table.columns = ['Min Sales Price', 'Max Sales Price']
        print("\nMinimum and Maximum Sales Price by Category")
        print(pivot_table)
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")

#option 8: Number of unique employees by region
def Unique_employees_by_region(data):
    try:
        pivot_table = pd.pivot_table(data,
        index = 'sales_region', 
        values = 'employee_id',
        aggfunc= {'employee_id': pd.Series.nunique},
        fill_value = 0)
        pivot_table = pivot_table.reset_index()
        pivot_table.columns = ['Region    ', 'Number of Unique Employees']
        print("\nNumber of Unique employees by region")
        print(pivot_table)
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")

#Option 9, custom pivot table
def Custom_Pivot_Table(data):
    try:
        #creating lists of options for the user to be able to call. 
        index_options = list(data.columns)
        value_options = list(data.columns)
        function_options = {'1': 'sum', '2': 'mean', '3': 'min', '4': 'max', '5': 'nunique'}
        #user chooses their own index
        print("Choose an index column from the options below:")
        for i, col in enumerate(index_options, 1):
            print(f"{i}. {col}")
        indexchoice = int(input("Please enter your prefered index with its corresponding number: "))
        index_column = index_options[indexchoice - 1]
        #user chooses their own value
        print("Choose a value column from the options below: ")
        for i, col in enumerate(value_options, 1):
            print(f"{i}. {col}")
        valuechoice = int(input("Please enter your prefered value with its corresponding number: "))
        value_column = value_options[valuechoice - 1]
        #user chooses their function for the custom pivot table. 
        print("Choose a function you would like the pivot table to preform.")
        for i, function in function_options.items():
            print(f"{i}. {function}")
        function_choice = input("Please enter your prefered function with its corresponding number: ")
        function_final = function_options[function_choice]
        function_final = pd.Series.nunique if function_options == 'nunique' else function_final

        pivot_table = pd.pivot_table(data,
        index = index_column,
        values = value_column,
        aggfunc= {value_column: function_final},
        fill_value = 0)

        print("\nCustom Pivot Table")
        print(pivot_table)
        print("Would you like to save your pivot table as a CSV file?\nIf you would not like to save, enter no")
        csv_name = input("\nPlease enter the name you would like for your file. Do not include spaces.")
        to_Excel(pivot_table,csv_name)
        return pivot_table
    except Exception as e:
        print(f"An unexpected error occured: {e}")

#turn pivot table into a csv file. ask user what file name they want. 
def to_Excel(data, filename):
    try:
        if(filename.lower() == 'no'):
            return 
        else:
            csv_filename = filename + '.csv'
            data.to_csv(csv_filename, index = False)
            print(f"Your table has been saved as {csv_filename}")
    except Exception as e:
        print(f"an error has occurd saving the table to CSV: {e}")

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

