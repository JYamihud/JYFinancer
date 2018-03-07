#!/usr/bin/python
# -*- coding: UTF-8 -*-

#### IMPORTING STUFF

from modules import hcu
from modules import warning
import gtk
import os
import pango
import random
from datetime import datetime


#Constants

recietes = []
stores = ["Tiv Taam", "Walmart"]
items = ["Cola", "Shocko"]



consolestring = ""



mainwindow = gtk.Window()
mainwindow.connect("destroy", lambda w: gtk.main_quit())
mainwindow.set_default_size(400, 400)
mainwindow.maximize()
mainwindow.set_position(gtk.WIN_POS_CENTER)
mainwindow.set_title("JYFinancer")
gtk.window_set_default_icon_from_file("py_data/icon.png")

mainbox = gtk.VBox(False)
mainwindow.add(mainbox)

def Print(text):
    global consolestring
    consolestring = text + "\n" + consolestring
    try:
        output.set_text(consolestring)    
    except:
        pass
    print text


Print("Start Up")




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
            
            
            if self.r == 0:
                self.tag = len(recietes)+1
                self.store = ""
                self.time = [int(datetime.now().hour), int(datetime.now().minute)]
                self.date = [int(datetime.now().year), int(datetime.now().month), int(datetime.now().day)]
                self.total = 0
                self.rlist = []
                
                
                
                
            else:
                
                for i in recietes:
                    if i[0] == r:
                        
                
                        self.tag = self.r
                        self.store = i[1]
                        self.time  = i[2]
                        self.date  = i[3]
                        self.total = i[4]
                        self.rlist = i[5]
            
            
            
            
            self.newgain = 0
            self.newitemname = ""
            self.newamoun = 1
            
            
            # STORE
            
            self.recbox = gtk.VBox(False)
            self.addrecwin.add(self.recbox)
            
            
            self.addrecwin.set_title("Reciete No: "+str(self.tag))
            
            self.storebox = gtk.HBox(False)
            self.recbox.pack_start(self.storebox, False)
            self.storebox.pack_start(gtk.Label(" Store: "), False)
            
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
            
            self.itembox.pack_start(gtk.Label(" Item: "), False)
            
            
            
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
            
            self.addbutton = gtk.Button("Add Item")
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
            
            def refrash(w=None):
            
                try:
                    self.itemsbox.destroy()
                except:
                    pass
            
                self.itemsbox = gtk.VBox(False)
                self.recietescroll.add_with_viewport(self.itemsbox)
                
                def itemline(index, inf):
                    
                    self.oneibox = gtk.HBox(False)
                    self.itemsbox.pack_end(self.oneibox, False)
                    
                    
                    
                    self.oneibox.pack_start(gtk.Label(str(inf[2]*inf[0])+"$ |  X  "+str(inf[0])+" | "+inf[1]+" | Per 1: "+str(inf[2])+"$"), False)
                    
                    def deletebutton(w, ind):
                        del self.rlist[ind]
                        refrash()
                    
                    deleteline = gtk.Button("Delete")
                    self.oneibox.pack_end(deleteline, False)
                    deleteline.connect("clicked", deletebutton, index)
                    
                    
                for index, i in enumerate(self.rlist):
                    itemline(index, i)
                
                
                
                
                self.itemsbox.show_all()
                
            refrash()
            
            self.recbox.pack_start(gtk.HSeparator(), False)
            finishbox = gtk.HBox(False)
            self.recbox.pack_start(finishbox, False)
            
            def cancelb(w):
                self.addrecwin.destroy()
            cancel_button = gtk.Button("Cancel")
            cancel_button.connect("clicked", cancelb)
            finishbox.pack_end(cancel_button, False)
            
            
            def okb(w):
                
                
                
                global recietes
                if self.r == 0:
                    recietes.append([self.tag, self.store, self.time, self.date, self.total, self.rlist])
                else:
                    recietes[self.tag-1] = [self.tag, self.store, self.time, self.date, self.total, self.rlist]
                    
                self.addrecwin.destroy()
                
                reload_win()
                
                
                
            ok_button = gtk.Button("Save Reciete")
            ok_button.connect("clicked", okb)
            finishbox.pack_end(ok_button, False)
            
             
            #################
            
            
            
            
                        
            def close(k=None):
                w.set_sensitive(True)
                print self.time
                
            self.addrecwin.connect("destroy", close)
            
            
            self.addrecwin.show_all()
    



def reload_win(w=None):
    
    global mainbox
    mainbox.destroy()
    
    mainbox = gtk.VBox(False)
    mainwindow.add(mainbox)
    
    
    # TOP PANEL
    
    toppanel = gtk.HBox(False)
    mainbox.pack_start(toppanel, False)
    
    openfilebutton = gtk.Button("Open")
    toppanel.pack_start(openfilebutton, False)
    
    savefilebutton = gtk.Button("Save")
    toppanel.pack_start(savefilebutton, False)
    
    saveasfilebutton = gtk.Button("Save As")
    toppanel.pack_start(saveasfilebutton, False)
    
    filenamepreview = gtk.Label("No File")
    toppanel.pack_start(filenamepreview, False)
    
    
    
    
    
    
    
    #toolbar
    
    toolbar = gtk.HBox(False)
    mainbox.pack_start(toolbar, False)
    
    
    
    
    
    
    #search
    searchbox = gtk. HBox(False)
    toolbar.pack_end(searchbox, False)
    
    #searchentry = gtk.Entry()
    #searchbox.pack_start(searchentry, False)
    
    #searchbutton = gtk.Button("Search")
    #searchbox.pack_start(searchbutton, False)
    
    
        
        
    
    addreciet = gtk.Button("Add Reciete")
    toolbar.pack_end(addreciet, False)
    addreciet.connect("clicked", reciete_editor, 0)
    
    
    # RECIETES
    
    rscroll = gtk.ScrolledWindow()
    mainbox.pack_start(rscroll)
    
    rbox = gtk.VBox()
    rscroll.add_with_viewport(rbox)
    
    def rec(index):
        rebox = gtk.HBox(False)
        rbox.pack_end(rebox, False)
        
        r = recietes[index]
        text = "$"+str(r[4])+"     "+str(r[3][0])+"/"+str(r[3][1])+"/"+str(r[3][2])+"     "+str(r[2][0])+":"+str(r[2][1])+"     "+str(r[1])
        
        # 3 2 4 1
        
        
        callrec = gtk.Button(text)
        rebox.pack_start(callrec)
        callrec.connect("clicked", reciete_editor, index+1)
        
    
    for i in recietes:
        
        rec(i[0]-1)        
    
    
    mainbox.show_all()



reload_win()

mainwindow.show_all()

gtk.main()

