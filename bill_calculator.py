# Week 2 Assignment: Simple Bill Calculator

# 1. Ask the user for the price and quantity using input()
price_input = input("Enter the price of one item: ")
quantity_input = input("Enter the quantity you want: ")

# 2. Convert the input strings to numerical values (float for price, int for quantity)
price = float(price_input)
quantity = int(quantity_input)

# 3. Calculate the total cost
total = price * quantity

# 4. Print a friendly summary using an f-string formatted to 2 decimal places
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
