#!/usr/bin/python
# -*- coding: UTF-8 -*-

#### IMPORTING STUFF

from modules import hcu
import os
import datetime
import random



VERSION = 0.0

# 100 , 100

class colors:
    NORMAL = '\033[m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system("clear")

print colors.WARNING,colors.UNDERLINE,colors.BOLD,  " "*30 + "JY FINANCER " + str(VERSION) + " "*30, colors.NORMAL
print "| type help to see availbale functions"

newpassword = ""
def save():
    
    if username == "":
        print "| ERROR! No user. Try 'newuser' to create a user"
        return
    #print "|"+username
    #print "|"+userstring
    print "| Been made "+str(changes)+" changes to the file."
    confirm = raw_input("|"+str(printname)+" : Confirm save (y|n) : ")
    
    if confirm in ['y', 'Y']:
        try:
            savefile = open('users/'+username, "w")
            
            savefile.write( hcu.passworded(newpassword)+"\n" )
            savefile.write( hcu.code(userstring, newpassword) )
            savefile.close()
            
            print "| FILE SAVED"
            
            global changes 
        
            changes = 0
            
        except:
            print "| FILE FAILED SAVING (probably because it has No user)"
            raise
def cb(userstring,equel="="):
    
    b = 0
    cub = 0
    cuh = 0
    for i in userstring.split("\n"):
       
        value = i[i.find(" ")+1:i.replace(" ", "y", 1).find(" ")]
        
        
        if equel != "cu":
            if i.startswith("=") and equel not in [ '-', '+' ]:
                b = float(value)
            if i.startswith("+") and equel != '-':
                b = b + float(value)
            if i.startswith("-") and equel != '+':
                b = b - float(value)
        else:
            
            if i.startswith("="):
                
                tmp = float(value) - b
                if tmp > 0:
                    cub = cub + tmp
                else:
                    cuh = cuh + tmp
                
                b = float(value)
                
            if i.startswith("+"):
                b = b + float(value)
            if i.startswith("-"):
                b = b - float(value)
            
            
    if equel != "cu":    
        return b
    else:
        return cub, cuh
        
def openf():
    
    filename = raw_input("|"+str(printname)+" : Username : ")
    
    if filename not in os.walk(os.getcwd()+"/users").next()[2]:
        print "| ERROR! No such user found!"
        return 
    
    password = raw_input("|"+str(printname)+" : Password : ")
    global newpassword
    newpassword = password
    
    
    rawfile = open("users/"+filename, "r").read()
    
    if hcu.passworded(password) == rawfile.split("\n")[0]:
        
        global username
        global userstring
        global changes 
        
        changes = 0
        username = filename
        userstring = hcu.uncode(rawfile[rawfile.find("\n")+1:], password)
        
        print "| FILE SUCCESSFULLY OPENNED"
    else:
        print "| FILE FAILED TO OPEN"
username = ""
userstring = ""
changes = 0

while True:
    
    printname = username
    
    print "|",colors.NORMAL
    com = raw_input("|"+str(printname)+" : "+colors.WARNING)
    
    if len(com) > 0:
        ccom = com
    else:
        ccom = "    "    
    
    
    def help():
        
        print open("py_data/help.txt", "r").read()[:-1]
    
    
        
    if com == "help":
        help()
    
    
    elif com == "exit":
        break
    
    elif com == "users":
        
        if len(os.walk(os.getcwd()+"/users").next()[2]) == 0:
            print "| NO USERS CREATED YET. type 'newuser' to create one:"
            continue
        
        
        for i in os.walk(os.getcwd()+"/users").next()[2]:
            print "|", i
    
    elif com == "newuser":
        
        # NAME
        
        expire = 5
        while expire != 0:
            newusername = raw_input("|"+str(printname)+" :Name    : ")
            
            if len(newusername) > 0:
                break
            
            elif newusername in os.walk(os.getcwd()+"/users").next()[2]:
                print "| ERROR! Username exists\n|\n|\n|"
                expire = expire - 1  
            
            else:
                print "| ERROR! Username should be at least one character\n|\n|\n|"
                expire = expire - 1    
                
            
        if expire == 0:
            print "| Amount of attempt expired."
            continue
        
        # PASSWORD
        
        expire = 5
        while expire != 0:
            newpassword = raw_input("|"+str(printname)+" :Password: ")
            
            if len(newpassword) > 0:
                break
            else:
                print "| ERROR! Password should be at least one character\n|\n|\n|"
                expire = expire - 1    
                
            
        if expire == 0:
            print "| Amount of attempt expired."
            continue
        
        # CONFIRM
        
        expire = 5
        while expire != 0:
            newconfirm = raw_input("|"+str(printname)+" :Password: ")
            
            if newconfirm == newpassword:
                break
            else:
                print "| ERROR! Passwords don't match\n|\n|\n|"
                expire = expire - 1    
                
            
        if expire == 0:
            print "| Amount of attempt expired."
            continue
        
        
        
        
        # BALANCE
        
        
        expire = 5
        while expire != 0:
            newusersbalance = raw_input("|"+str(printname)+" :Balance : ")
            
            try:
                 float(newusersbalance)
                 break
            except:
                
                expire = expire - 1
                
                print "| ERROR! balance supposed to be a number (or a float)\n|\n|\n|"
                continue       
        if expire == 0:
            print "| Amount of attempt expired."
        
        userstring = "= "+newusersbalance+" "+str(datetime.date.today())
        username = newusername
        changes = 0
        
        print "| User created... To save user as a file type 'save'"
        
    
    elif com == "raw":
        for i in userstring.split("\n"):
            print "| "+i
    
    elif com == "save":
        save()
    
    elif com == "open":
        openf()
    
    
    
    elif com == "cb":
        print "| "+colors.BOLD+str(cb(userstring))
    
    
    #### NOW THE + and - and = sing
    
    
    
    elif ccom[0] in ['+','-','=']:
            
            
            try: 
                number = float(com[1:])
                comment = raw_input("|"+str(printname)+" : Comment :")
                
                userstring = userstring + "\n" + com[0] + " " + str( number ) + " " + comment + " " + str(datetime.date.today())
                changes = changes + 1
                
                 
            except:
                
                
                if com in ['+','-','=']:
                    for i in userstring.split('\n'):
                        if i.startswith(com):
                            print "| "+i
                    
                    if com != "=":
                        print "| TOTALLY "+str(cb(userstring, com))
                
                else:
                    print "| ERROR! variable must a number"
    
    
    
    elif com == "compare":
        
        i1 = raw_input("|"+str(printname)+" : Search 1 :")
        i2 = raw_input("|"+str(printname)+" : Search 2 :")
        
        iall = [i1, i2]
        answers = {}
        countans = []        
                
        for i in range(2):
            
            
            
            count = 0
        
            countstring = ""
            
            for b in userstring.split('\n'):
                if iall[i].upper() in b.upper():
                    print "| "+b
                    count = count + 1
                    
                    countstring = countstring + b + "\n"
            
            countstring = countstring[:-1]
            
            
            if len(iall[i]) != 0:
                
                countans.append( [iall[i], cb(countstring,"+"), cb(countstring,"-") ] )
                
                answers[str(i)+"total"] = "| Found "+ str(count) + " " + iall[i] + " TOTALLING +"+str(cb(countstring,"+"))+" "+str(cb(countstring,"-"))
            else:
                print "| "+iall[i]+" not found"
    
        for i in answers:
            print answers[i]
        
        
        print "| "+colors.BOLD
        
        i01 , i02 = countans[0][1], countans[0][2]
        i11 , i12 = countans[1][1], countans[1][2]
        
        i0 = i01 + i02
        i1 = i11 + i12
        
        if i0 > i1:
        
            percent = i0 / i1  *100
            print "|", colors.OKGREEN, countans[0][0], colors.NORMAL ,"is", colors.BOLD , percent, "%", colors.NORMAL ," better then", colors.WARNING, countans[1][0]
        else:
            percent = i1 / i0  *100
            print "|", colors.OKGREEN, countans[1][0], colors.NORMAL , "is", colors.BOLD , percent, "%", colors.NORMAL ," better then", colors.WARNING, countans[0][0]
        
    elif com == "cu":
            
        print "| Unknown benefits: +", cb(userstring, "cu")[0], "and hazard:", cb(userstring, "cu")[1]
    
    elif com == "mostused":
        
        print "Loading..."
        
        mostlist = {}
        for b in userstring.split("\n"):
            for i in b.split(" "):
                if i not in mostlist:
                    mostlist[i] = 1
                else:
                    mostlist[i] = mostlist[i] + 1
        x = []
        for i in mostlist:
            
            x.append([mostlist[i], i])
        
        mostlist = x
        
        
        for i in sorted(mostlist):
            print "|", i[0]," :[", i[1], "]"
    
    elif com == "edit.py":
        os.system( "xdg-open "+__file__ ) # ONLY IN LINUX
    
    elif com == "usersdir":
        os.system("nautilus "+__file__[:__file__.rfind("/")]+"/users") # ONLY IN LINUX
    
    
            
    elif len(com) > 0: # SEARCH
        
        count = 0
        
        countstring = ""
        
        for i in userstring.split('\n'):
            if com.upper() in i.upper():
                print "| "+i
                count = count + 1
                
                countstring = countstring + i + "\n"
        
        countstring = countstring[:-1]
        
        
        if len(com) != 0:
            print "| Found "+str(count)+" Instances of ",colors.BOLD+com+colors.NORMAL, colors.WARNING+" In the file"
            print "| TOTALLING +"+str(cb(countstring,"+"))+" "+str(cb(countstring,"-"))
        else:
            print "| "+com+" not found"
        
        
        
    
    
    
    
    
    
    
    
        
