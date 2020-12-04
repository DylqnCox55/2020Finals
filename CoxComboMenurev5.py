print("Welcome to the Krusty Krab")
total=0                     
loop=0
orderList=[]
order=input("Would you like to make an order, y or n? ")
while order !="y":
    order=input("Would you like to make an order, y or n? ")
while order!="n":
    loop+=1
    orderList.append(f"Order {loop}:")
    sandwich=input("Would you like a Krabby Patty, y or n? ")
    while sandwich!="y" and sandwich!="n":
        sandwich=input("Would you like a Krabby Patty, y or n? ")
    if sandwich=="y":
        sandwich=input("What kind of Krabby Patty do you want, original for $1.25 (o), Double for $2.00 (d), or Triple for $3.00 (t)? ")
        while sandwich !="o" and sandwich !="d" and sandwich !="t":
            sandwich=input("What kind of Krabby Patty do you want, original for $1.25 (o), Double for $2.00 (d), or Triple for $3.00 (t)? ")
        print(sandwich)
        if sandwich=="o":
            total+=1.25
            orderList.append("Krabby Patty")
        elif sandwich=="d":
            total+=2
            orderList.append("Double Krabby Patty")
        elif sandwich=="t":
            total+=3
            orderList.append("Triple Krabby Patty")
        cheese=input("Would you like to add cheese for $0.25, y or n? ")
        while cheese !="y" and cheese !="n":
            cheese=input("Would you like to add cheese for $0.25, y or n? ")
        if cheese=="y":
            total+=.25
            orderList.append("with cheese")
    else:
        print("no")


    bits=input("Would you like Coral Bits, y or n? ")
    while bits!="y" and bits!="n":
        bits=input("Would you like Coral Bits, y or n? ")
    if bits=="y":
        bits=input("Small for $1.00 (s), medium for $1.25 (m), or large for $1.50 (l)? ")
        while bits !="s" and bits !="m" and bits!="l":
            bits=input("Small for $1.00 (s), medium for $1.25 (m), or large for $1.50 (l)? ")
        print("You said",bits)
        if bits=="s":
            total+=1
            orderList.append("Small Coral Bits")
        elif bits=="m":
            total+=1.25
            orderList.append("Medium Coral Bits")
        elif bits=="l":
            total+=1.5
            orderList.append("Large Coral Bits")
    else:
        print("no")


    rings=input("Would you like Kelp Rings for $1.50, y or n? ")
    while rings!="y" and rings!="n":
        rings=input("Would you like Kelp Rings for $1.50, y or n? ")
    if rings=="y":
        total+=1.5
        orderList.append("Kelp Rings")
        print("You ordered Kelp Rings")
        saltySauce=input("Would you like salty sauce with that for an extra $0.50, y or n? ")
        while saltySauce!="y" and saltySauce!="n":
            saltySauce=input("Would you like salty sauce with that for an extra $0.50, y or n? ")
        if saltySauce=="y":
            total+=.5
            orderList.append("with salty sauce")
            print("You ordered salty sauce")
    else:
        print("no")


    meal=input("Would you like a Krabby Meal, y or n? ")
    while meal!="y" and meal!="n":
        meal=input("Would you like a Krabby Meal, y or n? ")
    if meal=="y":
        meal=input("Original for $3.50 (o), Double for $3.75 (d), or Triple for $4.00 (t)? ")
        while meal!="o" and meal!="d" and meal!="t":
            meal=input("Original for $3.50 (o), Double for $3.75 (d), or Triple for $4.00 (t)? ")
        print("You said",meal)
        if meal=="o":
            total+=3.5
            orderList.append("Krabby Meal")
        elif meal=="d":
            total+=3.75
            orderList.append("Double Krabby Meal")
        elif meal=="t":
            total+=4
            orderList.append("Triple Krabby Meal")
    else:
        print("no")

        
        

    dog=input("Would you like a Salty Sea Dog, y or n? ")
    while dog!="y" and dog!="n":
        dog=input("Would you like a Salty Sea Dog, y or n? ")
    if dog=="y":
        dog=input("Regular for $1.25 (r) or a footlong for $2.00 (f)? ")
        while dog!="r" and dog!="f":
            dog=input("Regular for $1.25 (r) or a footlong for $2.00 (f)? ")
        print("You said",dog)
        if dog=="r":
            total+=1.25
            orderList.append("Salty Sea Dog")
        elif dog=="f":
            total+=2
            orderList.append("Footlong")
    else:
        print("no")



    surprise=input("Would you like a Sailors Surprise for $3.00, y or n? ")
    while surprise!="y" and surprise!="n":
        surprise=input("Would you like a Sailors Surprise for $3.00, y or n? ")
    if surprise=="y":
        total+=3
        orderList.append("Sailors Surprise")
        print("You ordered a Sailors Surprise")
    else:
        print("no")


    loaf=input("Would you like a Golden Loaf for $2.00, y or n? ")
    while loaf!="y" and loaf!="n":
        loaf=input("Would you like a Golden Loaf for $2.00, y or n? ")
    if loaf=="y":
        total+=2
        orderList.append("Golden Loaf")
        print("You ordered a Golden Loaf")
        sauce=input("Would you like sauce with that for an extra $0.50, y or n? ")
        while sauce!="y" and sauce!="n":
            sauce=input("Would you like sauce with that for an extra $0.50, y or n? ")
        if sauce=="y":
            total+=.5
            orderList.append("with sauce")
            print("You ordered sauce")
    else:
        print("no")


    beverage=input("Would you like a beverage, y or n? ")
    while beverage!="y" and beverage!="n":
        beverage=input("Would you like a beverage, y or n? ")
    if beverage=="y":
        beverage=input("Small Seafoam Soda for $1.00 (s), Medium Seafoam Soda for $1.25 (m), Large Seafoam Soda for $1.50 (l), or a Kelp Shake for $2.00 (k)? ")
        print("You said",beverage)
        while beverage!="s" and beverage!="m" and beverage!="l" and beverage!="k":
            beverage=input("Small Seafoam Soda for $1.00 (s), Medium Seafoam Soda for $1.25 (m), Large Seafoam Soda for $1.50 (l), or a Kelp Shake for $2.00 (k)? ")
        if beverage=="s":
            total+=1
            orderList.append("Small Seafoam Soda")
        elif beverage=="m":
            total+=1.25
            orderList.append("Medium Seafoam Soda")
        elif beverage=="l":
            total+=1.5
            orderList.append("Large Seafoam Soda")
        elif beverage=="k":
            total+=2
            orderList.append("Kelp Shake")
    else:
        print("no")
    

    order=input("Would you like to make another order, y or n? ")
    while order!="y" and order!="n":
        order=input("Would you like to make another order, y or n? ")


print(*orderList, sep=" ")

print("Subtotal: ${:,.2f}".format(total))
print("Tax: ${:,.2f}".format(total * .07))
print("Total: ${:,.2f}".format(total * 1.07))