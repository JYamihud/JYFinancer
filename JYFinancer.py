#!/usr/bin/python
# -*- coding: UTF-8 -*-

VERSION = 0.0

#### IMPORTING STUFF

from modules import hcu
from modules import warning
from modules import jyfi
from modules import getlocation

jyfi.VERSION = VERSION

import gtk
import os
import pango
import random
from datetime import datetime

lastdateformat = "%Y/%m/%d"

savefile = None
cbs = [0]
pds = [0]
pdsettings = ["m", 10]

lastdate = str(datetime.now().strftime(lastdateformat))
stores = []
items = []
recietes = []

        
    


mainwindow = gtk.Window()
mainwindow.connect("destroy", lambda w: gtk.main_quit())
mainwindow.set_default_size(400, 400)
mainwindow.maximize()
mainwindow.set_position(gtk.WIN_POS_CENTER)
mainwindow.set_title("JYFinancer")
gtk.window_set_default_icon_from_file("py_data/icon.png")

mainbox = gtk.VBox(False)
mainwindow.add(mainbox)

#def Print(text):
#    global consolestring
#    consolestring = text + "\n" + consolestring
    
#    print text


#Print("Start Up")

# ITEM VIEVER

class item_viewer:
    
    def __init__(self, w, r):
        self.w = w
        self.r = r
    
        try:
            self.w.set_sensitive(False)
        except:
            pass
        
        
        self.itemwindow = gtk.Window()
        self.itemwindow.set_default_size(400, 400)
        self.itemwindow.set_position(gtk.WIN_POS_CENTER)
        
        if current == "i":
            self.itemwindow.set_title(items[self.r])
        elif current == "s":
            self.itemwindow.set_title(stores[self.r])
        def close(w):
            
            try:
                self.w.set_sensitive(True)
            except:
                pass
        self.itemwindow.connect("destroy", close)
        
        
        self.box = gtk.VBox(False)
        self.itemwindow.add(self.box)
        
        # IF IT'S ITEM
        
        if current == "i":
            
            #sto
            
            
            
            self.stcroll = gtk.ScrolledWindow()
            self.stcroll.set_size_request(200, 200)
            self.box.pack_start(self.stcroll, True)
            
            self.storebox = gtk.VBox(False)
            self.stcroll.add_with_viewport(self.storebox)
            
            
            # rec
            
            
            
            self.recscroll = gtk.ScrolledWindow()
            self.recscroll.set_size_request(200, 200)
            self.box.pack_start(self.recscroll, True)
            
            self.recbox = gtk.VBox(False)
            self.recscroll.add_with_viewport(self.recbox)
            
            storefound = []
            
            for index, i in enumerate(recietes):
                
                for b in i[4]:
                    if b[1] == r:
                        
                        if i[0] not in storefound:
                            storefound.append(i[0])
                        
                        
                        recb = gtk.HBox(False)
                        recicon = gtk.Image()
                        recicon.set_from_file("py_data/icons/file.png")
                        
                        recb.pack_start(recicon, False)
                        
                        text = "  "+str(i[2][0])+"/"+str(i[2][1])+"/"+str(i[2][2])+"     "+str(i[1][0])+":"+str(i[1][1])+"     "+str(stores[i[0]]+"  "+str(b[2]*b[0])+" $")
                
                        recb.pack_start(gtk.Label(text), False)
            
                        self.recbox.pack_start(recb, False)
                        
            for i in storefound:
                
                storeicon = gtk.Image()
                storeicon.set_from_file("py_data/icons/store.png")          
                
                storeb = gtk.HBox(False)
                storeb.pack_start(storeicon, False)
                storeb.pack_start(gtk.Label("  "+stores[i]), False)
                
                
                self.storebox.pack_start(storeb, False)
                        
                
        # IF IT'S STORE
        
        if current == "s":
            
            #sto
            
            
            
            self.stcroll = gtk.ScrolledWindow()
            self.stcroll.set_size_request(200, 200)
            self.box.pack_start(self.stcroll, True)
            
            self.storebox = gtk.VBox(False)
            self.stcroll.add_with_viewport(self.storebox)
            
            
            # rec
            
            
            
            self.recscroll = gtk.ScrolledWindow()
            self.recscroll.set_size_request(200, 200)
            self.box.pack_start(self.recscroll, True)
            
            self.recbox = gtk.VBox(False)
            self.recscroll.add_with_viewport(self.recbox)
            
            itemfound = []
            
            for index, i in enumerate(recietes):
                
                
                if i[0] == r:
                    
                    
                    
                    for b in i[4]:
                        if b[1] not in itemfound:
                            itemfound.append(b[1])
                    
                        
                    recb = gtk.HBox(False)
                    recicon = gtk.Image()
                    recicon.set_from_file("py_data/icons/file.png")
                    
                    recb.pack_start(recicon, False)
                
                    try:    
                        text = "  "+str(i[2][0])+"/"+str(i[2][1])+"/"+str(i[2][2])+"     "+str(i[1][0])+":"+str(i[1][1])+"     "+str(stores[i[0]]+"  "+str(b[2]*b[0])+" $")
                    except:
                        text = "  "+str(i[2][0])+"/"+str(i[2][1])+"/"+str(i[2][2])+"     "+str(i[1][0])+":"+str(i[1][1])+"     "+str(stores[i[0]])
                
                    recb.pack_start(gtk.Label(text), False)
                    self.recbox.pack_start(recb, False)
                    
            for i in itemfound:
                
                storeicon = gtk.Image()
                storeicon.set_from_file("py_data/icons/item.png")          
                
                storeb = gtk.HBox(False)
                storeb.pack_start(storeicon, False)
                storeb.pack_start(gtk.Label("  "+items[i]), False)
                
                
                self.storebox.pack_start(storeb, False)
        
        
        
        
        
        
        
        
        
        self.itemwindow.show_all()
            
    



#RECIETE EDITOR

class reciete_editor:
        
        def __init__(self, w, r):
            self.w = w
            self.r = r   
        
            try:
                self.w.set_sensitive(False)
            except:
                pass
            
            
            
            self.addrecwin = gtk.Window()
            
            
            self.addrecwin.set_default_size(400, 400)
            
            self.addrecwin.set_position(gtk.WIN_POS_CENTER)
            
            
            
            
            
            
            
            if self.r == -1:
                self.tag = len(recietes)
                self.store = ""
                self.time = [int(datetime.now().hour), int(datetime.now().minute)]
                self.date = [int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)]
                self.total = 0
                self.rlist = []
                self.comment = "Comment:"
                
                print "Self is -1"
                
                
            else:
                print "Self is something else"
        
                print recietes, self.r
        
                self.tag = self.r
                self.store = stores[recietes[self.r][0]]
                self.time  = recietes[self.r][1]
                self.date  = recietes[self.r][2]
                self.total = recietes[self.r][3]
                rlist = recietes[self.r][4]
                
                self.rlist = []
                
                print "HERE", rlist
                
                for i in rlist:
                    i[1] = items[i[1]]
                    self.rlist.append(i)
                
                
                self.comment = recietes[self.r][5]
    
            
            
            
            self.newgain = 0
            self.newitemname = ""
            self.newamoun = 1
            
            
            # STORE
            
            self.recbox = gtk.VBox(False)
            self.addrecwin.add(self.recbox)
            
            
            self.addrecwin.set_title("Reciete No: "+str(self.tag))
            
            self.storebox = gtk.HBox(False)
            self.recbox.pack_start(self.storebox, False)
            
            storeicon = gtk.Image()
            storeicon.set_from_file("py_data/icons/store.png")
            self.storebox.pack_start(storeicon, False)
            
            def storeentry(w):
                self.store = w.get_text()
            
            self.storelist = gtk.ListStore(str)
            for i in stores:
                self.storelist.append([i])
            self.comp = gtk.EntryCompletion()
            self.comp.set_model(self.storelist)
            self.comp.set_text_column(0)
            self.comp.set_inline_completion(True)
            
            
            self.storeEntry = gtk.Entry()
            self.storeEntry.set_text(self.store)
            self.storeEntry.set_completion(self.comp)
            self.storeEntry.connect("changed", storeentry)
            self.storebox.pack_start(self.storeEntry, True)
            
            
            
            
            #DATE TIME
            
            
            self.datebox = gtk.HBox(False)
            self.recbox.pack_start(self.datebox, False)
            self.datebox.pack_start(gtk.Label(" At: "), False)
            
            def timechange(w):
                self.time[0] = int(self.hourbutton.get_value())
                self.time[1] = int(self.minutebutton.get_value())
                self.date[0] = int(self.yearbutton.get_value())
                self.date[1] = int(self.monthbutton.get_value())
                self.date[2] = int(self.daybutton.get_value())
                self.total = float(self.totalbutton.get_value())
                self.newamoun = float(self.amountbutton.get_value())
                self.newgain = float(self.newgainbutton.get_value())
            # HOUR
            self.houradj = gtk.Adjustment(1.0,0.0, 23, 1.0, 0.0)
            self.hourbutton = gtk.SpinButton(self.houradj, 0, 0)
            self.hourbutton.set_value(int(self.time[0]))
            self.hourbutton.set_wrap(True)
            self.datebox.pack_start(self.hourbutton, False)
            self.hourbutton.connect("value-changed", timechange)
            
            self.datebox.pack_start(gtk.Label(" : "), False)
            
            # MINUTE
            self.minuteadj = gtk.Adjustment(1.0,0.0, 59, 1.0, 0.0)
            self.minutebutton = gtk.SpinButton(self.minuteadj, 0, 0)
            self.minutebutton.set_value(int(self.time[1]))
            self.minutebutton.set_wrap(True)
            self.datebox.pack_start(self.minutebutton, False)
            self.minutebutton.connect("value-changed", timechange)
        
            # DAY
            self.dayadj = gtk.Adjustment(1.0,1.0, 32, 1.0, 0.0)
            self.daybutton = gtk.SpinButton(self.dayadj, 0, 0)
            self.daybutton.set_value(int(self.date[2]))
            self.daybutton.set_wrap(True)
            self.datebox.pack_end(self.daybutton, False)
            self.daybutton.connect("value-changed", timechange)
            
            self.datebox.pack_end(gtk.Label(" / "), False)    
            
            # MONTH
            self.monthadj = gtk.Adjustment(1.0,1.0, 12, 1.0, 0.0)
            self.monthbutton = gtk.SpinButton(self.monthadj, 0, 0)
            self.monthbutton.set_value(int(self.date[1]))
            self.monthbutton.set_wrap(True)
            self.datebox.pack_end(self.monthbutton, False)
            self.monthbutton.connect("value-changed", timechange)
            
            self.datebox.pack_end(gtk.Label(" / "), False)    
            
            # YEAR
            self.yearadj = gtk.Adjustment(1.0,0.0, 9999, 1.0, 0.0)
            self.yearbutton = gtk.SpinButton(self.yearadj, 0, 0)
            self.yearbutton.set_value(int(self.date[0]))
            self.yearbutton.set_wrap(True)
            self.datebox.pack_end(self.yearbutton, False)
            self.yearbutton.connect("value-changed", timechange)
            
            
            # TOTAL WASTE OR GAIN
            
            self.totalbox = gtk.HBox(False)
            self.recbox.pack_start(self.totalbox, False)
            self.totalbox.pack_start(gtk.Label(" Total $"), False)    
            
            # TOTAL VALUE
            self.totaladj = gtk.Adjustment(0.01,-999999999999999999, 999999999999999999, 0.01, 0.01)
            self.totalbutton = gtk.SpinButton(self.totaladj, 0.01, 2)
            self.totalbutton.set_value(float(self.total))
            self.totalbutton.set_wrap(True)
            self.totalbox.pack_start(self.totalbutton, False)
            self.totalbutton.connect("value-changed", timechange)
            
            self. recbox.pack_start(gtk.HSeparator(), False)
            
            
            #### ADD NEW ITEM
            
            self.itembox = gtk.HBox(False)
            self.recbox.pack_start(self.itembox, False)
            
            
            
            # AMOUNT
            
            self.itembox.pack_start(gtk.Label("  X"), False)
            
            self.amountadj = gtk.Adjustment(0.01, 0.001, 99999, 1.0,0.001)
            self.amountbutton = gtk.SpinButton(self.amountadj, 1.0, 3)
            self.amountbutton.set_value(float(self.newamoun))
            self.amountbutton.set_wrap(True)
            self.itembox.pack_start(self.amountbutton, False)
            self.amountbutton.connect("value-changed", timechange)
            
            itemicon = gtk.Image()
            itemicon.set_from_file("py_data/icons/item.png")
            self.itembox.pack_start(itemicon, False)
            
            
            def newitem(w):
                self.newitemname = w.get_text()
            
            self.itemlist = gtk.ListStore(str)
            for i in items:
                self.itemlist.append([i])
            self.comp2 = gtk.EntryCompletion()
            self.comp2.set_model(self.itemlist)
            self.comp2.set_text_column(0)
            self.comp2.set_inline_completion(True)
            
            
            self.itemname = gtk.Entry()
            self.itemname.set_completion(self.comp2)
            self.itemname.connect("changed", newitem)
            self.itembox.pack_start(self.itemname, True)
            
            # ADD BUTTOM
            
            def additem(w=None):
                
                self.rlist.append([self.newamoun, self.newitemname, self.newgain])
                self.totalbutton.set_value(self.totalbutton.get_value()+self.newamoun*self.newgain)
                
                self.newgainbutton.set_value(0.0)
                self.amountbutton.set_value(1.0)
                self.itemname.set_text("")
                self.amountbutton.grab_focus()
                
                refrash()
            
            self.addbutton = gtk.Button()
            addbuttonicon = gtk.Image()
            addbuttonicon.set_from_file("py_data/icons/add.png")
            self.addbutton.add(addbuttonicon)
            self.addbutton.props.relief = gtk.RELIEF_NONE
            self.itembox.pack_end(self.addbutton, False)
            self.addbutton.connect("clicked", additem)
            
            
            
            
            # NEW GAIN
            
            self.newgainadj = gtk.Adjustment(0.01,-999999999999999999, 999999999999999999, 0.01, 0.01)
            self.newgainbutton = gtk.SpinButton(self.newgainadj, 0.01, 2)
            self.newgainbutton.set_value(float(self.newgain))
            self.newgainbutton.set_wrap(True)
            self.itembox.pack_end(self.newgainbutton, False)
            self.newgainbutton.connect("value-changed", timechange)
            
            self.itembox.pack_end(gtk.Label(" One Item $"), False)
            
            self.recbox.pack_start(gtk.HSeparator(), False)
            
            
            ### SCROLLABLE
            
            self.recietescroll = gtk.ScrolledWindow()
            self.recbox.pack_start(self.recietescroll, True)
            self.orgabox = gtk.VBox(False)
            self.recietescroll.add_with_viewport(self.orgabox)
            
            
            def refrash(w=None):
            
                try:
                    self.itemsbox.destroy()
                except:
                    pass
                
                
                
                
                self.itemsbox = gtk.VBox(False)
                
                self.orgabox.pack_start(self.itemsbox, False)
                
                
                
                
                def itemline(index, inf):
                    
                    self.oneibox = gtk.HBox(False)
                    self.itemsbox.pack_end(self.oneibox, False)
                    
                    itemicon = gtk.Image()
                    itemicon.set_from_file("py_data/icons/item.png")
                    self.oneibox.pack_start(itemicon, False)
                    
                    self.oneibox.pack_start(gtk.Label(str(inf[2]*inf[0])+"$ |  X  "+str(inf[0])+" | "+inf[1]+" | Per 1: "+str(inf[2])+"$"), False)
                    
                    def deletebutton(w, ind):
                        
                        self.totalbutton.set_value(self.totalbutton.get_value()-self.rlist[ind][0]*self.rlist[ind][2])
                        
                        del self.rlist[ind]
                        refrash()
                    
                    deleteline = gtk.Button()
                    deletelineicon = gtk.Image()
                    deletelineicon.set_from_file("py_data/icons/delete.png")
                    deleteline.add(deletelineicon)
                    deleteline.props.relief = gtk.RELIEF_NONE
                    self.oneibox.pack_end(deleteline, False)
                    
                    deleteline.connect("clicked", deletebutton, index)
                    
                    
                for index, i in enumerate(self.rlist):
                    itemline(index, i)
                
                
                
                
                self.itemsbox.show_all()
                
            refrash()
            
            self.comview = gtk.TextView()
            self.comscroll = gtk.ScrolledWindow()
            self.comscroll.add(self.comview)
            self.comscroll.set_size_request(100,100)
            self.recbox.pack_start(self.comscroll, False)
            
            self.comtext = self.comview.get_buffer()
            
            self.comtext.set_text(self.comment)
            
            
            self.recbox.pack_start(gtk.HSeparator(), False)
            finishbox = gtk.HBox(False)
            self.recbox.pack_start(finishbox, False)
            
            def cancelb(w):
                self.addrecwin.destroy()
            cancel_button = gtk.Button()
            cancel_buttonbox = gtk.HBox(False)
            cancel_buttonicon = gtk.Image()
            cancel_buttonicon.set_from_file("py_data/icons/delete.png")
            cancel_buttonbox.pack_start(cancel_buttonicon, False)
            cancel_buttonbox.pack_start(gtk.Label("  Cancel"))
            cancel_button.add(cancel_buttonbox)
            cancel_button.props.relief = gtk.RELIEF_NONE
            cancel_button.connect("clicked", cancelb)
            finishbox.pack_end(cancel_button, False)
            
            self.converted = False
            
            def okb(w):
                
                if self.store == "":
                    self.store = "Unknown"
                
                
                self.comment = str( self.comtext.get_text(self.comtext.get_start_iter(), self.comtext.get_end_iter()))
                
                
                
                # adding all the stores, items
                
                global stores
                global itmes
                
                if self.store not in stores:
                
                    stores.append(self.store)
                
                storeindex = 0
                for i, s in enumerate(stores):
                    if self.store == s:
                        storeindex = i
                
                self.store = storeindex
                
                
                for num, item in enumerate(self.rlist):
                    
                    if item[1] == "":
                        item[1] = "Unknown"
                    
                    
                    if item[1] not in items:
                        items.append(item[1])
                    
                    self.converted = True
                    
                    itemsindex = 0
                    for i, t in enumerate(items):
                        if item[1] == t:
                            itemindex = i
                    print self.rlist[num][1], "rlist[num][1]"
                    
                    self.rlist[num][1] = itemindex
                    
                    print self.rlist[num][1], "rlist[num][1]"
                    print
                    
                
                global recietes
                if self.r == -1:
                    recietes.append([self.store, self.time, self.date, self.total, self.rlist, self.comment])
                else:
                    recietes[self.tag] = [self.store, self.time, self.date, self.total, self.rlist, self.comment]
                
                
                print stores
                print items
                    
                    
                self.addrecwin.destroy()
                
                reload_win()
                
                
                
            ok_button = gtk.Button()
            
            ok_buttonbox = gtk.HBox(False)
            ok_buttonicon = gtk.Image()
            ok_buttonicon.set_from_file("py_data/icons/ok.png")
            ok_buttonbox.pack_start(ok_buttonicon, False)
            ok_buttonbox.pack_start(gtk.Label("  Ok"))
            ok_button.add(ok_buttonbox)
            ok_button.props.relief = gtk.RELIEF_NONE
            
            
            ok_button.connect("clicked", okb)
            finishbox.pack_end(ok_button, False)
            
             
            #################
            
            
            
            
                        
            def close(k=None):
                w.set_sensitive(True)
                print self.time
                
                
                
                if self.converted == False:
                    
                    for num, item in enumerate(self.rlist):
                        
                        if item[1] == "":
                            item[1] = "Unknown"
                        
                        
                        
                        if item[1] not in items:
                            items.append(item[1])
                        
                        
                        itemsindex = 0
                        for i, t in enumerate(items):
                            if item[1] == t:
                                itemindex = i
                        print self.rlist[num][1], "rlist[num][1]"
                        
                        self.rlist[num][1] = itemindex
                        
                        print self.rlist[num][1], "rlist[num][1]"
                        print
                
                
                
            self.addrecwin.connect("destroy", close)
            
            
            self.addrecwin.show_all()
    

current = "r"

def reload_win(w=None):
    
    
    global cbs
    global pds
    
    nowcb = 0
    
    for i in recietes:
        nowcb = nowcb + i[3]
        
    
    
    FMT = "%y-%m-%d"
        
    today = str(datetime.today().strftime(FMT))
    
    
    
    
    
    nextsalary = ""
    tmp = today.split("-")
    
    if int(tmp[2]) > 9:
    
        nextsalary = nextsalary + tmp[0] + "-"
        nextsalary = nextsalary + str(int(tmp[1])+1) + "-"
        nextsalary = nextsalary + "10"
            
    else:
        
        nextsalary = nextsalary + tmp[0] + "-"
        nextsalary = nextsalary + str(int(tmp[1])) + "-"
        nextsalary = nextsalary + "10"
        
    
    x =  datetime.strptime(nextsalary, FMT) - datetime.today()
   
    nowpd = (float(nowcb)/int(x.days)*100)/100
    
    if lastdate == str(datetime.now().strftime(lastdateformat)):
        cbs[-1] = nowcb
        pds[-1] = nowpd
    else:
        cbs.append(nowcb)
        pds.append(nowpd) 
    
    
    
    global lastdate
    lastdate = str(datetime.now().strftime(lastdateformat))
    
    global mainbox
    mainbox.destroy()
    
    mainbox = gtk.VBox(False)
    mainwindow.add(mainbox)
    
    
    # TOP PANEL
    
    toppanel = gtk.HBox(False)
    mainbox.pack_start(toppanel, False)
    
    def openbuttonaction(w):
        
        global cbs, pds, pdsettings, lastdate, stores, items, recietes
        
        global savefile
        savefile = getlocation.get()
        
        cbs, pds, pdsettings, lastdate, stores, items, recietes = jyfi.openfile(savefile)
        
        mainwindow.set_title("J.Y.FINANCER "+savefile)
        
        reload_win()
        
    openfilebutton = gtk.Button()
    
    openfilebuttonicon = gtk.Image()
    
    openfilebuttonicon.set_from_file("py_data/icons/open.png")
    
    openfilebuttonbox = gtk.HBox(False)
    openfilebuttonbox.pack_start(openfilebuttonicon,False)
    openfilebuttonbox.pack_start(gtk.Label("  Open"))
    openfilebutton.add(openfilebuttonbox)
    toppanel.pack_start(openfilebutton, False)
    openfilebutton.props.relief = gtk.RELIEF_NONE
    openfilebutton.connect("clicked", openbuttonaction)
    
    def savebuttonaction(w):
        
        if not savefile:
            jyfi.savefile(getlocation.get(), cbs, pds, pdsettings, lastdate, stores, items, recietes)
        else:
            jyfi.savefile(savefile, cbs, pds, pdsettings, lastdate, stores, items, recietes)
    savefilebutton = gtk.Button()
    toppanel.pack_start(savefilebutton, False)
    savefilebuttonicon = gtk.Image()
    savefilebuttonicon.set_from_file("py_data/icons/save.png")
    savefilebuttonbox = gtk.HBox(False)
    savefilebuttonbox.pack_start(savefilebuttonicon,False)
    savefilebuttonbox.pack_start(gtk.Label("  Save"))
    savefilebutton.add(savefilebuttonbox)
    savefilebutton.connect("clicked", savebuttonaction)
    savefilebutton.props.relief = gtk.RELIEF_NONE
    
    def saveasbuttonaction(w):
        
        global savefile
        savefile = getlocation.get()
        
        jyfi.savefile(savefile, cbs, pds, pdsettings, lastdate, stores, items, recietes)
        mainwindow.set_title("J.Y.FINANCER "+savefile)
        
    saveasfilebutton = gtk.Button()
    saveasfilebuttonicon = gtk.Image()
    saveasfilebuttonicon.set_from_file("py_data/icons/saveas.png")
    saveasfilebuttonbox = gtk.HBox(False)
    saveasfilebuttonbox.pack_start(saveasfilebuttonicon,False)
    saveasfilebuttonbox.pack_start(gtk.Label("  Save As..."))
    saveasfilebutton.add(saveasfilebuttonbox)
    saveasfilebutton.props.relief = gtk.RELIEF_NONE
    saveasfilebutton.connect("clicked", saveasbuttonaction)
    toppanel.pack_start(saveasfilebutton, False)
    
    
    # CB AND PD
    
    text = "CB: "+ str(cbs[-1]) + "  PD: "+ str(int(pds[-1]))
    toppanel.pack_start(gtk.Label(text))
    
    
    
    
    
    
    # COUNT
    
    count = gtk.Button()
    counticon = gtk.Image()
    counticon.set_from_file("py_data/icons/money.png")
    countbox = gtk.HBox(False)
    countbox.pack_start(counticon, False)
    countbox.pack_start(gtk.Label("  Count CB"))
    count.add(countbox)
    count.props.relief = gtk.RELIEF_NONE
    toppanel.pack_start(count, False)
    
    def counting(w):
        
        countwindow = gtk.Window()
        countwindow.set_default_size(300, 300)
        countwindow.set_position(gtk.WIN_POS_CENTER)
        countwindow.set_title("Counting CB")
        
        
        cbox = gtk.VBox(False)
        countwindow.add(cbox)
        cbox.pack_start(gtk.Label("\nCB means Current Balance\nThis is a window to output your CB.\nIt will do it by creating an\nempty reciete with a formula.\nCB - previous CB\nTo make the CB correct."), False)
        
        abox = gtk.HBox(False)
        cbox.pack_start(abox, False)
        
        abox.pack_start(gtk.Label("Your CB: "))
        
        newcbadj = gtk.Adjustment(0.01,-999999999999999999, 999999999999999999, 0.01, 0.01)
        newcb = gtk.SpinButton(newcbadj, 0.01, 2)
        newcb.set_value(float(0))
        newcb.set_wrap(True)
        abox.pack_start(newcb)
        
        
        
        finishbox = gtk.HBox(False)
        cbox.pack_end(finishbox, False)
        
        def okb(w):
            global recietes
            #[self.store, self.time, self.date, self.total, self.rlist, self.comment]
            
            global stores
            if "COUNTING" not in stores:
                stores.append("COUNTING")
            
            
            
            for index, i in enumerate(stores):
                if "COUNTING" == i:
                    break
            
            
            
            time = [int(datetime.now().hour), int(datetime.now().minute)]
            date = [int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)]
            
            recietes.append([index, time, date, float(newcb.get_value()-cbs[-1]),[], "COUNTING CB "+str(newcb.get_value()) ])
                
            countwindow.destroy()
            reload_win()
            
            
            
        ok_button = gtk.Button()
            
        ok_buttonbox = gtk.HBox(False)
        ok_buttonicon = gtk.Image()
        ok_buttonicon.set_from_file("py_data/icons/ok.png")
        ok_buttonbox.pack_start(ok_buttonicon, False)
        ok_buttonbox.pack_start(gtk.Label("  Ok"))
        ok_button.add(ok_buttonbox)
        ok_button.props.relief = gtk.RELIEF_NONE
        
        
        ok_button.connect("clicked", okb)
        finishbox.pack_end(ok_button, False)
        
        countwindow.show_all()
    
    count.connect("clicked", counting)
    
    
    
    #search
    searchbox = gtk. HBox(False)
    toppanel.pack_end(searchbox, False)
    
    searchentry = gtk.Entry()
    searchbox.pack_start(searchentry, False)
    
    searchbutton = gtk.Button()
    searchbuttonicon = gtk.Image()
    searchbuttonicon.set_from_file("py_data/icons/search.png")
    searchbutton.add(searchbuttonicon)
    searchbox.pack_start(searchbutton, False)
    searchbutton.props.relief = gtk.RELIEF_NONE
    
    
    
    
    
    
    #toolbar
    
    toolbar = gtk.HBox(False)
    mainbox.pack_start(toolbar, False)
    
    def setcurrent(w, r):
        global current
        current = r
        reload_win()
    
    receitesbutton = gtk.Button()
    receitesbuttonbox = gtk.HBox(False)
    receitesbuttonicon = gtk.Image()
    receitesbuttonicon.set_from_file("py_data/icons/file.png")
    receitesbuttonbox.pack_start(receitesbuttonicon, False)
    receitesbutton.add(receitesbuttonbox)
    receitesbuttonbox.pack_start(gtk.Label("  Recietes"))
    receitesbutton.props.relief = gtk.RELIEF_NONE
    receitesbutton.connect("clicked", setcurrent, "r")
    toolbar.pack_start(receitesbutton, False)
    
    itemsbutton = gtk.Button()
    itemsbuttonbox = gtk.HBox(False)
    itemsbuttonicon = gtk.Image()
    itemsbuttonicon.set_from_file("py_data/icons/item.png")
    itemsbuttonbox.pack_start(itemsbuttonicon, False)
    itemsbutton.add(itemsbuttonbox)
    itemsbuttonbox.pack_start(gtk.Label("  Items"))
    itemsbutton.props.relief = gtk.RELIEF_NONE
    itemsbutton.connect("clicked", setcurrent, "i")
    toolbar.pack_start(itemsbutton, False)
    
    storesbutton = gtk.Button()
    storesbuttonbox = gtk.HBox(False)
    storesbuttonicon = gtk.Image()
    storesbuttonicon.set_from_file("py_data/icons/store.png")
    storesbuttonbox.pack_start(storesbuttonicon, False)
    storesbutton.add(storesbuttonbox)
    storesbuttonbox.pack_start(gtk.Label("  Places"))
    storesbutton.props.relief = gtk.RELIEF_NONE
    storesbutton.connect("clicked", setcurrent, "s")
    toolbar.pack_start(storesbutton, False)
    
    
    
    
    
    
        
        
    
    addreciet = gtk.Button() #"Add Reciete"
    addrecietbox = gtk.HBox(False)
    addrecieticon = gtk.Image()
    addrecieticon.set_from_file("py_data/icons/add_file.png")
    addrecietbox.pack_start(addrecieticon, False)
    addrecietbox.pack_start(gtk.Label("  Add Reciete"))
    addreciet.props.relief = gtk.RELIEF_NONE
    addreciet.add(addrecietbox)
    
    toolbar.pack_end(addreciet, False)
    addreciet.connect("clicked", reciete_editor, -1)
    
    
    # RECIETES
    
    rscroll = gtk.ScrolledWindow()
    mainbox.pack_start(rscroll)
    
    rbox1 = gtk.VBox(False)
    rscroll.add_with_viewport(rbox1)
    
    rbox = gtk.VBox()
    rbox1.pack_start(rbox, False)
    
    # FUNCTION THAT DRAWS THE RECIETES LIST ONTO THE SCREEN
    def rec(index, r):
        rebox = gtk.HBox(False)
        rbox.pack_end(rebox, False)
        
        if current == "r":
            text = "  "+str(r[2][0])+"/"+str(r[2][1])+"/"+str(r[2][2])+"     "+str(r[1][0])+":"+str(r[1][1])+"     "+str(stores[r[0]]+"  "+str(r[3])+" $")
        
        else:
            text = str(r)
        # 3 2 4 1
        
        
        callrec = gtk.Button()
        callrec.props.relief = gtk.RELIEF_NONE
        callrecbox = gtk.HBox(False)
        callicon = gtk.Image()
        
        if current == "r":
            callicon.set_from_file("py_data/icons/file.png")
        elif current == "i":
            callicon.set_from_file("py_data/icons/item.png")
        elif current == "s":
            callicon.set_from_file("py_data/icons/store.png")
        callrecbox.pack_start(callicon, False)
        callrecbox.pack_start(gtk.Label("  "+text), False)
        callrec.add(callrecbox)
        
        
        
        rebox.pack_start(callrec)
        
        if current == "r":
            
            callrec.connect("clicked", reciete_editor, index)
            
            deletebutton = gtk.Button()
            deletebutton.props.relief = gtk.RELIEF_NONE
            deleteicon = gtk.Image()
            deleteicon.set_from_file("py_data/icons/delete.png")
            deletebutton.add(deleteicon)
            rebox.pack_end(deletebutton, False)
            
            def deleter(w, i):
                
                del recietes[i]
                reload_win()
                
            deletebutton.connect("clicked", deleter, index)
                
            
            
            
        else:
            
            callrec.connect("clicked", item_viewer, index)
        
    if current == "r":
        for index, i in enumerate(recietes):
        
            rec(index, recietes[index])        
    elif current == "i":
        for index, i in enumerate(items):
            rec(index, items[index])
    elif current == "s":
        for index, i in enumerate(stores):
            rec(index, stores[index])
    
    mainbox.show_all()



reload_win()

mainwindow.show_all()

gtk.main()

