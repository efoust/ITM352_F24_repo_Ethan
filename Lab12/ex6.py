# Use the requests library to pull data from hicentral.com (Hawaii Reality Site) on
# current mortgage rates and lenders

import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

# Fetch the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Get the rate table with current mortgage rates and lender info
    rate_table = soup.find("table")

    if rate_table:
        # Extract each row from the table
        rows = rate_table.find_all("tr")

        # Print the table headers
        headers = [header.text.strip() for header in rows[0].find_all("th")]
        print(" | ".join(headers))

        # Print each row's data
        for row in rows[1:]:
            cells = [cell.text.strip() for cell in row.find_all("td")]
            print(" | ".join(cells))
    else: 
        print("Rate table not found")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")