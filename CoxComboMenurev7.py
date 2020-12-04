print("Welcome to the Krusty Krab")                     
loop=0              #loops are counted so the final order print separates orders
itemNum=0           #items ordered are numbered for removal
orderList=[]        #items are stored in a list
totalList=[]        #Money is added into a list so it can be removed with items
order=input("Would you like to make an order, y or n? ")
while order !="y":
    order=input("Would you like to make an order, y or n? ")
while order!="n":
    loop+=1
    totalList.append(0)     #0 is added so totalList and OrderList indexes are lined up
    orderList.append(f"Order {loop}:")


    sandwich=input("Would you like a Krabby Patty, y or n? ")
    while sandwich!="y" and sandwich!="n":
        sandwich=input("Would you like a Krabby Patty, y or n? ")
    if sandwich=="y":
        itemNum+=1
        sandwich=input("What kind of Krabby Patty do you want, original for $1.25 (o), Double for $2.00 (d), or Triple for $3.00 (t)? ")
        while sandwich !="o" and sandwich !="d" and sandwich !="t":
            sandwich=input("What kind of Krabby Patty do you want, original for $1.25 (o), Double for $2.00 (d), or Triple for $3.00 (t)? ")
        print(sandwich)
        if sandwich=="o":
            totalList.append(1.25)
            orderList.append(f"{itemNum} Krabby Patty")     #itemNum is added with f{} so items are numbered without increasing the index
        elif sandwich=="d":
            totalList.append(2)
            orderList.append(f"{itemNum} Double Krabby Patty")
        elif sandwich=="t":
            totalList.append(3)
            orderList.append(f"{itemNum} Triple Krabby Patty")
        cheese=input("Would you like to add cheese for $0.25, y or n? ")
        while cheese !="y" and cheese !="n":
            cheese=input("Would you like to add cheese for $0.25, y or n? ")
        if cheese=="y":
            itemNum+=1
            totalList.append(.25)
            orderList.append(f"{itemNum} with cheese")
    else:
        print("no")


    bits=input("Would you like Coral Bits, y or n? ")
    while bits!="y" and bits!="n":
        bits=input("Would you like Coral Bits, y or n? ")
    if bits=="y":
        itemNum+=1
        bits=input("Small for $1.00 (s), medium for $1.25 (m), or large for $1.50 (l)? ")
        while bits !="s" and bits !="m" and bits!="l":
            bits=input("Small for $1.00 (s), medium for $1.25 (m), or large for $1.50 (l)? ")
        print("You said",bits)
        if bits=="s":
            totalList.append(1)
            orderList.append(f"{itemNum} Small Coral Bits")
        elif bits=="m":
            totalList.append(1.25)
            orderList.append(f"{itemNum} Medium Coral Bits")
        elif bits=="l":
            totalList.append(1.5)
            orderList.append(f"{itemNum} Large Coral Bits")
    else:
        print("no")


    rings=input("Would you like Kelp Rings for $1.50, y or n? ")
    while rings!="y" and rings!="n":
        rings=input("Would you like Kelp Rings for $1.50, y or n? ")
    if rings=="y":
        itemNum+=1
        totalList.append(1.5)
        orderList.append(f"{itemNum} Kelp Rings")
        print("You ordered Kelp Rings")
        saltySauce=input("Would you like salty sauce with that for an extra $0.50, y or n? ")
        while saltySauce!="y" and saltySauce!="n":
            saltySauce=input("Would you like salty sauce with that for an extra $0.50, y or n? ")
        if saltySauce=="y":
            itemNum+=1
            totalList.append(.5)
            orderList.append(f"{itemNum} with salty sauce")
            print("You ordered salty sauce")
    else:
        print("no")


    meal=input("Would you like a Krabby Meal, y or n? ")
    while meal!="y" and meal!="n":
        meal=input("Would you like a Krabby Meal, y or n? ")
    if meal=="y":
        itemNum+=1
        meal=input("Original for $3.50 (o), Double for $3.75 (d), or Triple for $4.00 (t)? ")
        while meal!="o" and meal!="d" and meal!="t":
            meal=input("Original for $3.50 (o), Double for $3.75 (d), or Triple for $4.00 (t)? ")
        print("You said",meal)
        if meal=="o":
            totalList.append(3.5)
            orderList.append(f"{itemNum} Krabby Meal")
        elif meal=="d":
            totalList.append(3.75)
            orderList.append(f"{itemNum} Double Krabby Meal")
        elif meal=="t":
            totalList.append(4)
            orderList.append(f"{itemNum} Triple Krabby Meal")
    else:
        print("no")

        
        

    dog=input("Would you like a Salty Sea Dog, y or n? ")
    while dog!="y" and dog!="n":
        dog=input("Would you like a Salty Sea Dog, y or n? ")
    if dog=="y":
        itemNum+=1
        dog=input("Regular for $1.25 (r) or a footlong for $2.00 (f)? ")
        while dog!="r" and dog!="f":
            dog=input("Regular for $1.25 (r) or a footlong for $2.00 (f)? ")
        print("You said",dog)
        if dog=="r":
            totalList.append(1.25)
            orderList.append(f"{itemNum} Salty Sea Dog")
        elif dog=="f":
            totalList.append(2)
            orderList.append(f"{itemNum} Footlong")
    else:
        print("no")



    surprise=input("Would you like a Sailors Surprise for $3.00, y or n? ")
    while surprise!="y" and surprise!="n":
        surprise=input("Would you like a Sailors Surprise for $3.00, y or n? ")
    if surprise=="y":
        itemNum+=1
        totalList.append(3)
        orderList.append(f"{itemNum} Sailors Surprise")
        print("You ordered a Sailors Surprise")
    else:
        print("no")


    loaf=input("Would you like a Golden Loaf for $2.00, y or n? ")
    while loaf!="y" and loaf!="n":
        loaf=input("Would you like a Golden Loaf for $2.00, y or n? ")
    if loaf=="y":
        itemNum+=1
        totalList.append(2)
        orderList.append(f"{itemNum} Golden Loaf")
        print("You ordered a Golden Loaf")
        sauce=input("Would you like sauce with that for an extra $0.50, y or n? ")
        while sauce!="y" and sauce!="n":
            sauce=input("Would you like sauce with that for an extra $0.50, y or n? ")
        if sauce=="y":
            itemNum+=1
            totalList.append(.5)
            orderList.append(f"{itemNum} with sauce")
            print("You ordered sauce")
    else:
        print("no")


    beverage=input("Would you like a beverage, y or n? ")
    while beverage!="y" and beverage!="n":
        beverage=input("Would you like a beverage, y or n? ")
    if beverage=="y":
        itemNum+=1
        beverage=input("Small Seafoam Soda for $1.00 (s), Medium Seafoam Soda for $1.25 (m), Large Seafoam Soda for $1.50 (l), or a Kelp Shake for $2.00 (k)? ")
        print("You said",beverage)
        while beverage!="s" and beverage!="m" and beverage!="l" and beverage!="k":
            beverage=input("Small Seafoam Soda for $1.00 (s), Medium Seafoam Soda for $1.25 (m), Large Seafoam Soda for $1.50 (l), or a Kelp Shake for $2.00 (k)? ")
        if beverage=="s":
            totalList.append(1)
            orderList.append(f"{itemNum} Small Seafoam Soda")
        elif beverage=="m":
            totalList.append(1.25)
            orderList.append(f"{itemNum} Medium Seafoam Soda")
        elif beverage=="l":
            totalList.append(1.5)
            orderList.append(f"{itemNum} Large Seafoam Soda")
        elif beverage=="k":
            totalList.append(2)
            orderList.append(f"{itemNum} Kelp Shake")
    else:
        print("no")
    
    print(*orderList, sep=" ")

    order=input("Would you like to make another order, y or n? ")
    while order!="y" and order!="n":
        order=input("Would you like to make another order, y or n? ")
    if order=="y":
        itemNum+=1
    
remove=input("Would you like to remove an item from the order, y or n? ")
while remove!="y" and remove!="n":
    remove=input("Would you like to remove an item from the order, y or n? ")
while remove!="n":
    if remove=="y":
        remove=int(input("Which item number would you like to remove? "))
        del orderList[remove]
        del totalList[remove]
        print(*orderList, sep=" ")
    remove=input("Would you like to remove another item from the order, y or n? ")
        


total=sum(totalList)

print("Subtotal: ${:,.2f}".format(total))
print("Tax: ${:,.2f}".format(total * .07))
print("Total: ${:,.2f}".format(total * 1.07))