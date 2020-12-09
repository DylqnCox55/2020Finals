import random           #random is imported for the password generator

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
    


    categoryList=["home", "work", "entertainment", "bills"]         #list of categories
    homeAccountList=[]                      #list of accounts under home category
    homeList=[]                             #list of passwords under home category
    workAccountList=[]                      #list of accounts under work category
    workList=[]                             #list of passwords under work category
    entAccountList=[]                       #list of accounts under entertainment category
    entList=[]                              #list of passwords under entertainment category
    billAccountList=[]                      #list of accounts under bills category
    billList=[]                             #list of passwords under bills category
    
    userInput=input('''                     
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

    ''')                            #One input statement for adding, changing, deleting, and viewing passwords

    while userInput!="quit":            #loops while user doesn't close the program
        if userInput=="add":
            account=input("What account is the password for? ")     
            password=input("""
        "input" - Enter your own password
        "generate" - The program will make one for you 
            
        """)        #Gives the user the option to enter their own password or to generate a random password
            while password!="input" and password!="generate":
                print("Invalid command")        #loops if the user doesn't enter one of the options
                password=input("""
        "input" - Enter your own password
        "generate" - The program will make one for you
                 
        """)
            
            
            
            if password=="input":
                 
                reqCheckList=[False,False,False,False,False]           
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
                        #call checker class





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
                #needs to call generator class
                #needs to call checker class

            print(categoryList)                 #displays the categories so the user knows the options
            category=input("What category do you want to store it in? ")
            while category!="home" and category!="work" and category!="entertainment" and category!="bills":
                print("Not a category")         #loops if the user doesn't input a category
                category=input("What category do you want to store it in? ")
            if category=="home":
                homeList.append(password)           #adds account and passwords to their own lists
                homeAccountList.append(account)
            if category=="work":
                workList.append(password)
                workAccountList.append(account)
            if category=="entertainment":
                entList.append(password)
                entAccountList.append(account)
            if category=="bills":
                billList.append(password)
                billAccountList.append(account)
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
                print(homeList)     
                change=input("Which password do you want to change? ")      #asks for wrong password
                new=input("What is the new password? ")                     #asks for replacement
                #call checker class
                index=homeList.index(change)    #Can't remember if we learned this, got it from https://www.geeksforgeeks.org/python-string-index-applications/
                homeList[index]=new             #changes password to new one
                print(homeList)                 #prints list to show that it changed
            if category=="work":
                print(workList)    
                change=input("Which password do you want to change? ")
                new=input("What is the new password? ")
                #call checker class
                index=workList.index(change)
                workList[index]=new
                print(workList)
            if category=="entertainment":
                print(entList)     
                change=input("Which password do you want to change? ")
                new=input("What is the new password? ")
                #call checker class
                index=entList.index(change)
                entList[index]=new
                print(entList)
            if category=="bills":
                print(billList)     
                change=input("Which password do you want to change? ")
                new=input("What is the new password? ")
                #call checker class
                index=billList.index(change)
                billList[index]=new
                print(billList)

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
                delete=input("Which password do you want to delete? ")
                index=homeList.index(delete)        #finds index to remove account list's matching item
                homeList.remove(delete)
                del homeAccountList[index]
            if category=="work":
                print(workList)
                delete=input("Which password do you want to delete? ")
                index=homeList.index(delete)
                workList.remove(delete)
                del workAccountList[index]
            if category=="entertainment":
                print(entList)
                delete=input("Which password do you want to delete? ")
                index=homeList.index(delete)
                entList.remove(delete)
                del entAccountList[index]
            if category=="bills":
                print(billList) 
                delete=input("Which password do you want to delete? ")
                index=homeList.index(delete)
                billList.remove(delete)
                del billAccountList[index]
            
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
                for i in range(len(homeList)):
                    print("The password for",homeAccountList[i],"is",homeList[i])       #prints both account and password
            if category=="work":
                for i in range(len(homeList)):
                    print("The password for",workAccountList[i],"is",workList[i])
            if category=="entertainment":
                for i in range(len(homeList)):
                    print("The password for",entAccountList[i],"is",entList[i])
            if category=="bills":
                for i in range(len(homeList)):
                    print("The password for",billAccountList[i],"is",billList[i])

            userInput=input('''
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

    ''')


        else:
            print("Invalid command")            #loops if user doesn't enter an option
            userInput=input('''
    What would you like to do?
    "add" - Add a password
    "change" - Change a password
    "delete" - Delete a password
    "view" - View a category
    "quit" - Log off of the Password Manager

    ''')


    print("Goodbye")        #program says goodbye to the user
    break                   #breaks the loop to end the program





