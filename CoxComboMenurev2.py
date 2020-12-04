print("Welcome to Good Burger")
total=0

#iteration 1
sandwich=input("What kind of sandwich do you want, chicken for $5.25 (c), beef for $6.25 (b), or tofu for $5.75 (t)? ")
print(sandwich)
if sandwich=="c":
    total+=5.25
elif sandwich=="b":
    total+=6.25
elif sandwich=="t":
    total+=5.75

#iteration 2
beverage=input("Would you like a beverage, y or n? ")
if beverage=="y":
    beverage=input("Small for $1.00 (s), medium for $1.75 (m), large for $2.25 (l), or child for $2.63 (c)? ")
    print("You said",beverage) #print(string,string,string)
else:
    print("no")

if beverage=="s":
    total+=1
elif beverage=="m":
    total+=1.75
elif beverage=="l":
    total+=2.25
elif beverage=="c":
    total+=2.63

#iteration 3
fries=input("Would you like fries, y or n? ")
if fries=="y":
    fries=input("Small for $1.00 (s), medium for $1.50 (m), or large for $2.00 (l)? ")
    print("You said",fries)
else:
    print("no")

if fries=="s":
    total+=1
elif fries=="m":
    total+=1.5
elif fries=="l":
    fries=input("Would you like a child size fry instead for an additional $0.38, y or n? ")
    if fries=="y":          #nested conditional statement
        total+=2.38
    else:
        total+=2



#print("Your total is $",total)
print("${:,.2f}".format(total))     #string formation