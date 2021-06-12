# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


import os
from dotenv import load_dotenv
from datetime import datetime

# Define the list of all possible product IDs for use in validation later
all_product_ids =[]
for i in products:
    all_product_ids.append(str(i["id"]))

# Request user to input product ids. Validate that the ids are in our list of products and save ids for use later
print("Please enter the products being purchased. Type 'DONE' when you have finished entering items")

scanned_product = []
selected_products = []

while True: 
    scanned_product = input("Please input a product identifier: ")
    if scanned_product in all_product_ids:
        selected_products.append(int(scanned_product))
    elif scanned_product == "DONE":
        break
    else:
        print("I'm sorry I can't find that product ID, please try again.")
    

# Define a function to look up the price of a product when given a product
def price_lookup(id): # TODO turn into list comprehension?
    for i in products:
        if i["id"] == id:
            selected_price = i["price"]
    return selected_price

# Sum up the prices of the selected items
subtotal = 0

for i in selected_products:
    subtotal += price_lookup(i)

# Get the tax rate from the .env file and calculate the tax amount
load_dotenv()
tax_rate = float(os.getenv("TAX_RATE", default=.0875))

tax_amount = subtotal * tax_rate

# Sum up the cost of the selected products and the tax
grand_total = tax_amount + subtotal

# Store current time as the checkout time 
checkout_time = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")

# Assemble receipt with items and amounts in a new variable. Print the receipt.
receipt = ""
receipt += f"""---------------------------------
Thank you for shopping at Frank's Foods.
Call us at (212) 998-1212 or visit us online at www.franksfoods.com
--------------------------------- 
Checkout time: {checkout_time}
---------------------------------
Selected Products:\n"""
for h in selected_products:
    for i in products:
        if i["id"] == h:
            receipt += "... " + i["name"] + " (" + to_usd(i['price'])+")\n"
receipt += f"""---------------------------------
Subtotal:{to_usd(subtotal)}
Tax: {to_usd(tax_amount)}
Total: {to_usd(grand_total)}
---------------------------------
Thank you for shopping with us! Please come again!
---------------------------------"""
print(receipt)

# Save the receipt to a text file
receipt_name = datetime.now().strftime("%d-%m-%Y-%I-%M-%S-%f")

file_name = f"receipts/{receipt_name}.txt"

with open(file_name, "w") as file: # "w" means "open the file for writing"
    file.write(receipt)

# TODO send email receipt