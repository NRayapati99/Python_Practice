""" number = list(input("Eneter the list of Numbers : "))"""
numbers = list(map(float, input("Enter three numbers separated by spaces: ").split()))
Small_Number = int(min(numbers))
print(f"The Biggest Number is {Small_Number}") 