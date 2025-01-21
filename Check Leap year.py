Year = int(input("Eneter A year To Find"))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 ==0):
    print (f"Given Year {Year} is a Leap Year")
else:
    print(f"Given Year {Year} is not a leap year")