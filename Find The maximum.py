""" number = list(input("Eneter the list of Numbers : "))"""
numbers = list(map(float, input("Enter three numbers separated by spaces: ").split()))
Large_Number = int(max(numbers))
print(f"The Biggest Number is {Large_Number}") 