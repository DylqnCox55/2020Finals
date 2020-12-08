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



class Checker:
    def __init__(self, password):
        self.passToCheck = password

    