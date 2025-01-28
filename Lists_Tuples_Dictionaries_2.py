topping_prices = {
    "sprinkles": 0.50,
    "crushed cookies": 0.50,
    "chocolate chips": 0.50,
    "fresh fruit": 0.75,
    "whipped cream": 0.75,
    "caramel drizzle": 0.75,
    "chocolate drizzle": 0.75,
    "Pop Rocks": 1.00,
    "Tajín spice": 1.00,
    "gummy bears": 1.00
}

selected_toppings = ["chocolate chips", "whipped cream", "gummy bears"]

total_cost = sum(topping_prices[topping] for topping in selected_toppings)

print(f"Total cost for the selected toppings: ${total_cost:.2f}")


'''
# Create a dictionary of toppings and their prices
topping_prices = {
    "sprinkles": 0.50,
    "crushed cookies": 0.50,
    "chocolate chips": 0.50,
    "fresh fruit": 0.75,
    "whipped cream": 0.75,
    "caramel drizzle": 0.75,
    "chocolate drizzle": 0.75,
    "Pop Rocks": 1.00,
    "Tajín spice": 1.00,
    "gummy bears": 1.00
}

# Ask user to input the selected toppings
selected_toppings = input("Enter the toppings you want, separated by commas (e.g., 'chocolate chips, whipped cream, gummy bears'): ").lower().split(", ")

# Validate if all selected toppings are in the dictionary
valid_toppings = [topping for topping in selected_toppings if topping in topping_prices]

# Calculate the total cost
total_cost = sum(topping_prices[topping] for topping in valid_toppings)

# Print the total cost
if valid_toppings:
    print(f"Total cost for the selected toppings: ${total_cost:.2f}")
else:
    print("No valid toppings were selected.")

'''

