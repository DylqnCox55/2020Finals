print("Welcome to Good Burger")
total=0
sandwich=input("What kind of sandwich do you want, chicken for $5.25 (c), beef for $6.25 (b), or tofu for $5.75 (t)? ")
print(sandwich)
if sandwich=="c":
    total+=5.25
elif sandwich=="beef":
    total+=6.25
elif sandwich=="tofu":
    total+=5.75

beverage=input("Would you like a beverage, y or n? ")
if beverage=="y":
    beverage=input("Small for $1.00 (s), medium for $1.75 (m), or large for $2.25 (l)? ")
    print("You said ",beverage) #print(string,string,string)
else:
    print("no")

if beverage=="s":
    total+=1
elif beverage=="m":
    total+=1.75
elif beverage=="l":
    total+=2.25



print("$",total)