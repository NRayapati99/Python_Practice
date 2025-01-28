Base_ice_creams = ("Vanilla", "Chocolate", "Strawberry", "Matcha", "Caramel", "Bubblegum", "Rainbow Sherbet")
Prices = (2.50, 3.00, 2.75, 3.50, 3.00, 2.25, 3.25)

Most_Expensive = max(Prices)
Least_Expesive = min(Prices)

ME_Index = Prices.index(Most_Expensive)
LE_Index = Prices.index(Least_Expesive)

ME_Flavour = Base_ice_creams[ME_Index]
LE_Flavour = Base_ice_creams[LE_Index]

print(f"The Most Expensive Flavour in the given List is: {ME_Flavour}")
print(f"The Least Expensive Flavour in the given List is: {LE_Flavour}")