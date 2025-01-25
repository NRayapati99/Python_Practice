Classic = ['Vanila','Chocolate','Strawberry']
Trendy = ['Macha','Caramel']
Kid_friendly = ['bubblegum','rainbowshebet']

flavour = input("Enter the desired flavour nmae: ")

if flavour in Classic:
    print(f"{flavour} is a classic and the price $10.")
elif flavour in Trendy:
    print(f"{flavour} is a Trendy and the price $15.")
elif flavour in Kid_friendly:
    print(f"{flavour} is a Kid_Friendly and the price $5.")
else:
    print(f"we are so sorry for that {flavour} is out of stock.")