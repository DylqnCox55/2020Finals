logIn="C$R0cks20"       #the passowrd required to run the program
attempts=3              #number of log in attempts the user has until the program shuts down.
passed="a"              #The first section allowing for multiple while loops
print("Welcome to the password manager!")       #welcomes the user to the password manager
while passed=="a":                              #creates a while loop for when in the log in stage
    log=input("Hello, please log in to get started: ")      #asks the user to type in the LogIn password to begin the program
    if (logIn in log):                                      #conditional statement checking to see if the user got the password correct                      
        print("Successfully logged in")                     #if succesful login, lets the user know the password is correct
        passed="in"                                         #changes the while loop variable, letting the program know that the second while loop can begin
        break                                               #ends the first while loop
    elif (logIn not in log):                                #conditional statement checking to see if the user did not get the password correct   
        attempts-=1                                         #subtracts one attempt for failing inputting the correct password
        print("You have two attempts left")                 #warns the user they have two attempts left
        second=input("Please log in to get started: ")      #asks the user to input the password to get into the main program
        if (logIn in second):                                  #conditional statement checking to see if the user got the password correct                      
            print("Successfully logged in")                    #if succesful login, lets the user know the password is correct
            passed="in"                                        #changes the while loop variable, letting the program know that the second while loop can begin
            break                                              #ends the first while loop
        elif (logIn not in second):                            #conditional statement checking to see if the user did not get the password correct   
            attempts-=1                                        #subtracts one attempt for failing inputting the correct password
            help=input("You have one attempt left, would you like a hint? (y) or (n): ")        #Warns the user they have one attempt left before the program closes and asks if they want a hint
            if ("y" in help):                                                                   #checks to see if the user did want a hint, and if so tell them the hint
                print("You're an AM student at SICTC, and we all know it rocks ;)")             #print statement telling the user a hint to the password
                finalAttempt=input("Please enter your password: ")           #asks the user to input a password
                if (logIn in finalAttempt):                                  #conditional statement checking to see if the user got the password correct                      
                    print("Successfully logged in")                          #if succesful login, lets the user know the password is correct
                    passed="in"                                              #changes the while loop variable, letting the program know that the second while loop can begin
                    break                                                    #ends the first while loop
                elif (logIn not in finalAttempt):                            #conditional statement checking to see if the user did not get the password correct   
                    attempts-=1                                              #subtracts one attempt for failing inputting the correct password
                    print("You have no attempts left, goodbye T-T")          #allows the user to know the program is shutting itself down
                    break                                                    #ends the first while loop
            elif ("n" in help):                                              #checks to see if the user did not want help, and if so moves the program along without a hint
                finalAttempt=input("Please enter your password: ")           #asks the user to input the password
                if (logIn in finalAttempt):                                  #conditional statement checking to see if the user got the password correct                      
                    print("Successfully logged in")                          #if succesful login, lets the user know the password is correct
                    passed="in"                                              #changes the while loop variable, letting the program know that the second while loop can begin
                    break                                                    #ends the first while loop
                elif (logIn not in finalAttempt):                            #conditional statement checking to see if the user did not get the password correct   
                    attempts-=1                                              #subtracts one attempt for failing inputting the correct password
                    print("You have no attempts left, goodbye T-T")          #allows the user to know the program is shutting itself down
                    break                                                    #ends the first while loop
while passed=="in":                                                          #debugger to check and make sure the second while loop and vaiable work
    print("made it")
    


    categoryList=["home", "work", "entertainment", "bills"]
    homeList=[]
    workList=[]
    entList=[]
    billList=[]

    userInput=input('''
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

    ''')

    while userInput!="quit":
        if userInput=="add":
            password=input("""
            "input" - Enter your own password
            "generate" - The program will make one for you 
            """)
            while password!="input" and password!="generate":
                print("Invalid command")
                password=input("""
                "input" - Enter your own password
                "generate" - The program will make one for you """)
            if password=="input":
                password=input("Enter your password: ")     #needs to check input for safe password
            elif password=="generate":
                print("oh no")              #needs an actual generator

            print(categoryList)
            category=input("What category do you want to store it in? ")
            while category!="home" and category!="work" and category!="entertainment" and category!="bills":
                print("Not a category")
                category=input("What category do you want to store it in? ")
            if category=="home":
                homeList.append(password)
            if category=="work":
                workList.append(password)
            if category=="entertainment":
                entList.append(password)
            if category=="bills":
                billList.append(password)
            

        elif userInput=="change":
            print(categoryList)
            category=input("What category is the password you want to change? ")
            while category!="home" and category!="work" and category!="entertainment" and category!="bills":
                print("Not a category")
                category=input("What category is the password you want to change? ")
            if category=="home":
                print(homeList)     #user should select which password they want to change
            if category=="work":
                print(workList)     #user should select which password they want to change
            if category=="entertainment":
                print(entList)      #user should select which password they want to change
            if category=="bills":
                print(billList)     #user should select which password they want to change


        elif userInput=="delete":
            print(categoryList)
            category=input("What category is the password you want to delete? ")
            while category!="home" and category!="work" and category!="entertainment" and category!="bills":
                print("Not a category")
                category=input("What category is the password you want to delete? ")
            if category=="home":
                print(homeList)     #user should select which password they want to change
            if category=="work":
                print(workList)     #user should select which password they want to change
            if category=="entertainment":
                print(entList)      #user should select which password they want to change
            if category=="bills":
                print(billList)     #user should select which password they want to change


        elif userInput=="view":
            print(categoryList)
            category=input("What category do you want to view? ")
            while category!="home" and category!="work" and category!="entertainment" and category!="bills":
                print("Not a category")
                category=input("What category do you want to view? ")
            if category=="home":
                print(homeList)     #needs to print out individual passwords instead of fuill list
            if category=="work":
                print(workList)
            if category=="entertainment":
                print(entList)
            if category=="bills":
                print(billList)


        else:
            print("Invalid command")


    print("Goodbye")
    break





