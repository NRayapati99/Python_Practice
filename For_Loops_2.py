Price_List = {
    "Single_Scoop": 3.00, 
    "Double_Scoop": 5.50, 
    "Triple_Scoop": 7.50,
    "Ice Cream Bars": 3.00, 
    "Popsicles" : 2.50, 
    "Mini_Tubs" : 4.00
    }

Order_List= { 
    "Single_Scoop": 1,
    "Mini_Tubs" : 2
    }
Sub_Total = 0
print ("Customer Copy")
for i,q in Order_List.items():
    Price = Price_List[i]
    cost = Price * q
    Sub_Total += cost 
    print(f"{i} x {q}  : ${cost:.2f}")

print("--------------------------")

print(f"Sub Total      : ${Sub_Total:.2f}")

GST = Sub_Total * 0.18
print(f"GST 18%        : ${GST:}")
Gross_Total = Sub_Total + GST
print(f"Gross Total    : ${Gross_Total}")