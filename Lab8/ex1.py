
#Debugging exercise # 1
product = {
    "name": 'small gumball', 
    "price": 0.34
}

tax_rate = 0.045

total = product["price"] + product["price"] * tax_rate

print(f"A {product["name"]} costs ${round(total,2)}")
