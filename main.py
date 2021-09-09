print("MENU: \nSmall Pizza: $15 \nMedium Pizza: $20 \nLarge Pizza: $25 \nPepperoni for Small Pizza: +$2 \nPepperoni for Medium or Large Pizza: +$3 \nExtra cheese for any size pizza: + $1 \n")

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :").upper()
pepperoni = input("Do you want pepperoni? Y or N :").upper()
cheese = input("Do you want extra cheese? Y or N :").upper()
bill=0
if(size=="S"):
  bill=15
  if(pepperoni=="Y"):
    bill+=2
elif(size=="M"):
  bill=20
  if(pepperoni=="Y"):
    bill+=3
elif(size=="L"):
  bill=25
  if(pepperoni=="Y"):
    bill+=3
if(cheese=="Y"):
  bill+=1
print(f"Your final bill is: ${bill}.")





