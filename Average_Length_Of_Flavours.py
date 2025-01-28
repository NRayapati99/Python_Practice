flavors = ["Vanilla", "Chocolate", "Strawberry", "Matcha", "Caramel", "Bubblegum", "Rainbow Sherbet"]

total_length = sum(len(flavor) for flavor in flavors)

average_length = total_length / len(flavors)

print(f"Average length of flavor names: {average_length:.2f}")
