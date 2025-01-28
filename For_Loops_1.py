'''flavours = ("Vanilla", "Chocolate", "Strawberry", "Matcha", "Caramel", "Bubblegum", "Rainbow Sherbet")
Prices = (2.50, 3.00, 2.75, 3.50, 3.00, 2.25, 3.25)'''

Flavor_Price = {
    "Vanilla": 2.5, 
    "Chocolate": 3.0, 
    "Strawberry": 2.75, 
    "Matcha": 3.5, 
    "Caramel": 3.0, 
    "Bubblegum": 2.25, 
    "Rainbow Sherbet": 3.25 }

topping_price = {
    "sprinkles": 0.50,
    "crushed cookies": 0.50,
    "chocolate chips": 0.50,
    "fresh fruit": 0.75,
    "whipped cream": 0.75,
    "caramel drizzle": 0.75,
    "chocolate drizzle": 0.75,
    "Pop Rocks": 1.00,
    "Tajín spice": 1.00,
    "gummy bears": 1.00 }

for i, j in Flavor_Price.items():
  
    for k, l in topping_price.items():
        tp = j + l
        print(f"{i} + {k} = {tp}")


    
    