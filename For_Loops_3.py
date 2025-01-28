ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Matcha", "Caramel"]
toppings = ["Sprinkles", "Crushed Cookies", "Chocolate Chips", "Whipped Cream", "Caramel Drizzle"]

print("The possible ice cream and single topping combinations are:")

for i in ice_cream_flavors:
    for j in toppings:
        print(f"{i} with {j}")