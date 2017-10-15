import random

def passworded(word):

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

    hashed = ""
    num = 0
    theb = len(word)
    
    while len(str(word)) < 20:
        rehashed = []
        for i in word:
            rehashed.append(i)
        rehashed = reversed(rehashed)
        
        hashed2 = ""
        for i in rehashed:
            hashed2 = hashed2 + i
        
        word = word + hashed2
    
    if len(str(word)) > 20:
        word = word[-20:]

    for i in word:
        num = letters.find(i)
        
        try:
            b = letters.find(hashed[-1])
        except:
            b = theb
  
        
        while b+num  > len(letters)-1:
            
            numsofb = []
            for c in str(b):
                numsofb.append(int(c))
            b = sum(numsofb)
            
            numsofb = []
            for c in str(num):
                numsofb.append(int(c))
            num = sum(numsofb)
        
        
        hashed = hashed + letters[b+num]
    
    
    
    return hashed

#coding HCU
def code(word, passw):
    
    #word = word.split("\n")
    
    string = ""
    
    
    onepass = passw
    for line in word:
        while len(passw) < len(word)+1:
            passw = passw+onepass
    
    for x, i in enumerate(word):
        
        #print "Letter",i, "Passletter", passw[x] , ord(i)+ord(passw[x])-ord(passw[x-1]), "\n"
        lcode = ord(i)+ord(passw[x])-ord(passw[x-1])
        #print lcode
        
        if lcode in range(254):
         string = string + chr(lcode)
        else:
            string = string + chr(254) + str(lcode) + chr(255)
    
    
    
    return string

def uncode(word, passw):
    
    
    #un-compressing the code
    
    tmpstr = ""
    skiplist = []
    for x, i in enumerate(word):
        
        if x in skiplist:
            
            continue
        if i != chr(254):
            tmpstr = tmpstr + str(ord(i))+"\n"
        else:   
            ll = 0
            num = ""
            skiplist = [x]
            
            while True:
                ll = ll + 1
                
                if word[x+ll] != chr(255):
                    num = num + word[x+ll]
                    skiplist.append(x+ll)
                else:
                    skiplist.append(x+ll)
                    
                    break
            
            tmpstr = tmpstr + str(num)+"\n"
    
    word = tmpstr
    
    
    
           
    # uncoding
    
    string = ""
    
    onepass = passw
    
    
    # password rematching in size
    for line in word:
        while len(passw) < len(word)+1:
            passw = passw+onepass


    sline = ""        
    for x, i in enumerate(word.split("\n")):
        
        if i not in  ["","\n"]:
            
            
            #print "line",int(i),  "pass" ,ord(passw[x])
            sline = sline + chr(int(i)+ord(passw[x-1])-ord(passw[x]))
    
    string = string + sline
    
    return string
    
