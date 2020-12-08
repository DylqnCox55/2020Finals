print("Welcome to the Krusty Krab")
total=0                     #accumulative variable
sandwichSelected=False      #flag variable
beverageSelected=False
bitsSelected=False

#iteration 1
sandwich=input("Would you like a Krabby Patty, y or n? ")
if sandwich=="y":
    sandwich=input("What kind of Krabby Patty do you want, original for $1.25 (o), Double for $2.00 (d), or Triple for $3.00 (t)? ")
    print(sandwich)
    sandwichSelected=True
    cheese=input("Would you like to add cheese for $0.25, y or n? ")
    if cheese=="y":
        total+=.25
else:
    print("no")
if sandwich=="o":
    total+=1.25
elif sandwich=="d":
    total+=2
elif sandwich=="t":
    total+=3
    
#iteration 2
beverage=input("Would you like a beverage, y or n? ")
if beverage=="y":
    beverage=input("Small Seafoam Soda for $1.00 (s), Medium Seafoam Soda for $1.25 (m), Large Seafoam Soda for $1.50 (l), or a Kelp Shake for $2.00 (k)? ")
    print("You said",beverage) #print(string,string,string)
    beverageSelected=True
else:
    print("no")

if beverage=="s":
    total+=1
elif beverage=="m":
    total+=1.25
elif beverage=="l":
    total+=1.5
elif beverage=="k":
    total+=2

#iteration 3
bits=input("Would you like Coral Bits, y or n? ")
if bits=="y":
    bits=input("Small for $1.00 (s), medium for $1.25 (m), or large for $1.50 (l)? ")
    print("You said",bits)
    bitsSelected=True
else:
    print("no")

if bits=="s":
    total+=1
elif bits=="m":
    total+=1.25
elif bits=="l":
    total+=1.5


print("Your order is a",sandwich,"sandwich with a",beverage,"drink,",bits,"bits")

print("${:,.2f}".format(total))