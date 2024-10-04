
#Debugging exercise # 2
prices = [5.95, 3.00, 12.50]
total_price = 0
tax_rate = 1.08    # 8% tax 
for price in prices:
    priceAndTax = price * tax_rate
    total_price = total_price + priceAndTax


print(f"Total price (with tax): ${round(total_price,2)}")

