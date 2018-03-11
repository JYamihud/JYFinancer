
from modules import warning

line = 0

def openfile(filename):
    
    global line
    line = 0
    
    cbs = [0]
    pds = [0]
    pdsettings = ["m", 10]
    
    lastdate = ""



    stores = []
    items = []
    recietes = []

    
    
    
    try:
        f = open(filename, "r")
    except:
        
        warning.warn( text="File Does Not Exists\n"+str(filename) )
        return
    
    #CHECKING THE SIGNATURE
    
    def gnl(f):
        
        global line
        line = line + 1
        print "LINE ", line
        
        s = ""
        while not s.endswith("\n"):
            s = s + f.read(1)
        
        return s[:-1]
        
    sig = gnl(f)
    if sig.split(" ")[0] != "JYFI":
        warning.warn( text="Not a vlid file format")
        return
    
    if VERSION < float(sig.split(" ")[1]):
        warning.warn( text="The file version is too new\nUpdate the software before using this file")
        return
    
    # EVERYTNING IS CHECKED NOW READING THE FILE
    
    
    # LASTDATE
    
    lastdate = gnl(f)
    print lastdate
    
    
    #CBS
    l = int(gnl(f))
    
    cbs = []
    for i in range(l):
        cbs.append(float(gnl(f)))
        
    print cbs 
    
    #PDS
    s = gnl(f) # PDSETTINGS FIRST
    pdsettings = [s.split(" ")[0], int(s.split(" ")[1])]
    print pdsettings
    
    l = int(gnl(f))
    
    pds = []
    for i in range(l):
        pds.append(float(gnl(f)))
        
    print pds 
    
    
    
    # STORES
    l = int(gnl(f))
    
    stores = []
    for i in range(l):
        stores.append(str(gnl(f)))
    print stores    
    
    # ITEMS
    l = int(gnl(f))
    
    items = []
    for i in range(l):
        items.append(str(gnl(f)))
    print items
    
    #RECIETES
    
    recietes = []
    #[self.store, self.time, self.date, self.total, self.rlist, self.comment]
    rlen = int(gnl(f))
    
    for i in range(rlen):
        rec = []
        
        rec.append(int(gnl(f))) # STORE INDEX
        ts = gnl(f)
        rec.append([int(ts.split(":")[0]), int(ts.split(":")[1])]) # TIME
        ds = gnl(f)
        rec.append([int(ds.split("/")[0]), int(ds.split("/")[1]), int(ds.split("/")[2])]) # DATE
        rec.append(float(gnl(f))) # TOTAL
        
        
        # [self.newamoun, self.newitemname, self.newgain]
        
        rcl = []
        
        l = int(gnl(f))
        
        for b in range(l):
            recl = []
            recl.append(float(gnl(f)))
            recl.append(int(gnl(f)))
            recl.append(float(gnl(f)))
            rcl.append(recl)
        print "rcl",rcl 
        rec.append(rcl)
        
        lc = int(gnl(f))
        rec.append(str(f.read(lc)))
        
        print rec
        
        recietes.append(rec)

    return cbs, pds, pdsettings, lastdate, stores, items, recietes
    
    
    print recietes


def savefile(filename, cbs, pds, pdsettings, lastdate, stores, items, recietes):
    
    f = open(filename, "w")
    
    #SINGATURE
    f.write("JYFI "+str(VERSION)+"\n")
    
    #LASTDATE
    f.write(str(lastdate)+"\n")
    
    #CBS
    f.write(str(len(cbs))+"\n")
    for i in cbs:
        f.write(str(i)+"\n")
    
    #PDS
    
    f.write(pdsettings[0]+" "+str(pdsettings[1])+"\n")
    f.write(str(len(pds))+"\n")
    for i in pds:
        f.write(str(i)+"\n")
    
    
    #STORES
    f.write(str(len(stores))+"\n")
    for i in stores:
        f.write(str(i)+"\n")

    #ITEMS
    f.write(str(len(items))+"\n")
    for i in items:
        f.write(str(i)+"\n")
        
    #RECIETES
    f.write(str(len(recietes))+"\n")
    for i in recietes:
        
        #[self.store, self.time, self.date, self.total, self.rlist, self.comment]
        
        f.write(str(i[0])+"\n")
        # TIME
        
        time = str(i[1][0])+":"+str(i[1][1])
        
        
        
        f.write(str(time)+"\n")
        
        
        # DATE
        
        date = str(i[2][0])+"/"+str(i[2][1])+"/"+str(i[2][2])
        f.write(str(date)+"\n")
        
        
        
        f.write(str(i[3])+"\n")
        f.write(str(len(i[4]))+"\n")
        print i[4]
        for line in i[4]:
            f.write(str(line[0])+"\n")
            f.write(str(line[1])+"\n")
            f.write(str(line[2])+"\n")
        f.write(str(len(i[5]))+"\n")
        f.write(str(i[5]))
    
        # [self.newamoun, self.newitemname, self.newgain]
    f.close()
