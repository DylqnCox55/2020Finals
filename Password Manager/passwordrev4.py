import random

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
        "generate" - The program will make one for you
                 """)
            
            
            
            if password=="input":
                 
                reqCheckList=[False,False,False,False,False,]           
                passwordList=[]
                strengthList=[]
                
                while False in reqCheckList:
                    password=input("Enter your password: ")
                    passwordList.append(password)
                    passwordLIST=[]
                    for i in range(len(password)):
                        passwordLIST.append(False)
                    if(len(password)>=6 and len(password)<=16):
                        reqCheckList[0]=True
                        for i in range (len(password)):
                            
                            if(ord(password[i]) in range(97,123)):
                                passwordLIST[i]=True   #a-z on ASCII is 97-123
                                reqCheckList[1]=True
                            elif(ord(password[i]) in range(65,91)):
                                passwordLIST[i]=True    #A-Z on ASCII is 65-91
                                reqCheckList[2]=True
                            elif(ord(password[i]) in range(48,58)):
                                passwordLIST[i]=True    #0-9 on ASCII is 48-58
                                reqCheckList[3]=True
                            elif(ord(password[i]) in range(33,42)):
                                passwordLIST[i]=True
                                reqCheckList[4]=True
                    if(False in passwordLIST or False in reqCheckList):
                        print("Password didn't meet the requirements")
                    else:
                        print("Password did meet the requirements")





            elif password=="generate":
                capital=input("How many capital letters do you want? ")
                lowercase=input("How many lowercase letters do you want? ")
                numbers=input("How many numbers do you want? ")
                symbols=input("How many symbols do you want? ")
                for i in range(int(capital)):
                    password+=chr(random.randint(65,90))
                for i in range(int(lowercase)):
                    password+=chr(random.randint(97,122))
                for i in range(int(numbers)):
                    password+=chr(random.randint(48,57))
                for i in range(int(symbols)):
                    password+=chr(random.randint(33,42))
                print(password)
                #needs to call checker class

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
            userInput=input('''
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

            ''')
            

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

            userInput=input('''
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

            ''')


        elif userInput=="delete":
            print(categoryList)
            category=input("What category is the password you want to delete? ")
            while category!="home" and category!="work" and category!="entertainment" and category!="bills":
                print("Not a category")
                category=input("What category is the password you want to delete? ")
            if category=="home":
                print(homeList)
                delete=int(input("Which number password do you want to delete? "))
                del homeList[delete-1]
            if category=="work":
                print(workList)
                delete=int(input("Which number password do you want to delete? "))
                del workList[delete-1]
            if category=="entertainment":
                print(entList)
                delete=int(input("Which number password do you want to delete? "))
                del entList[delete-1]
            if category=="bills":
                print(billList) 
                delete=int(input("Which number password do you want to delete? "))
                del billList[delete-1]
            
            userInput=input('''
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

            ''')


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

            userInput=input('''
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

                ''')


        else:
            print("Invalid command")


    print("Goodbye")
    break





