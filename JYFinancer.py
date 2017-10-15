#!/usr/bin/python
# -*- coding: UTF-8 -*-

#### IMPORTING STUFF

from modules import hcu
from modules import warning
import gtk
import os
import pango
import random


#Constants

username = None
password = None
userstring = ""
changes = 0


mainwindow = gtk.Window()
mainwindow.connect("destroy", lambda w: gtk.main_quit())
mainwindow.set_default_size(400, 400)
mainwindow.maximize()
mainwindow.set_position(gtk.WIN_POS_CENTER)
mainwindow.set_title("JYFinancer")
gtk.window_set_default_icon_from_file("py_data/icon.png")

mainbox = gtk.VBox(False)
mainwindow.add(mainbox)


# LOGIN FUNCTION
def login(widget=None):
    
    widget.set_sensitive(False)
    
    def return_sensitive(w=None):
        widget.set_sensitive(True)
    
    logwin = gtk.Window()
    logwin.connect("destroy", return_sensitive)
    
    logbox = gtk.VBox()
    logwin.add(logbox)
    logwin.set_position(gtk.WIN_POS_CENTER)
    
    def userbutton(name, box):
        
        def clickpassword(w, name):
            
            logwin.destroy()
            
            widget.set_sensitive(False)
    
            def return_sensitive(w=None):
                widget.set_sensitive(True)
            
            
            
            passw = gtk.Window()
            passw.connect("destroy", return_sensitive)
            passw.set_position(gtk.WIN_POS_CENTER)
            
            
            
            passbox = gtk.VBox()
            passw.add(passbox)
            
            passbox.pack_start(gtk.Label("  Password for "+name+"  "))
            
            def testpassword(w=None):
                
                text = entry.get_text()
                
                rawfile = open("users/"+name, "r").read()
    
                
                
                if len(text) > 0 and hcu.passworded(text) == rawfile.split("\n")[0]:
                   
                    
                    global username
                    global userstring
                    global changes 
                    global password
                    
                    password = text
                    changes = 0
                    username = name
                    userstring = hcu.uncode(rawfile[rawfile.find("\n")+1:], text)
                    
                    print "Login successfull"
                    
                    
                    reload_win()
                    
                else:
                    
                    warning.warn(None, "Password incorrect")
                    
                    
                
                passw.destroy()
                
                
            
            entry = gtk.Entry()
            entry.set_visibility(False)
            entry.connect("activate", testpassword)
            passbox.pack_start(entry)
            
            okbutton = gtk.Button("OK")
            okbutton.connect("clicked", testpassword)
            passbox.pack_start(okbutton)
            
            
            passw.show_all()
        
        
        button = gtk.Button()
        button.connect("clicked", clickpassword, name)
        bb = gtk.HBox(False)
        
        icon = gtk.Image()
        icon.set_from_file("py_data/icons/person.png")
        bb.pack_start(icon)
        bb.pack_start(gtk.Label(name))
        
        button.add(bb)
        box.pack_start(button)
    
    
    for i in os.listdir(os.getcwd()+"/users/"):
        userbutton(i, logbox)
        
    
    
    logwin.show_all()
    



def reload_win(w=None):
    
    global mainbox
    mainbox.destroy()
    
    mainbox = gtk.VBox(False)
    mainwindow.add(mainbox)
    
    # X_[] TOP PANNEL ###############
    
    
    toppanel = gtk.HBox(False)
    mainbox.pack_start(toppanel, False)
    

    # LOGIN BUTTON
    loginbutton = gtk.Button()
    loginicon = gtk.Image()
    loginbox = gtk.HBox(False)
    loginicon.set_from_file("py_data/icons/person.png")
    loginbutton.set_tooltip_text("open")
    loginbutton.add(loginbox)
    loginbox.pack_start(loginicon)
    loginbox.pack_start(gtk.Label(str(username)))

    loginbutton.connect("clicked", login)
    toppanel.pack_start(loginbutton, False)
    
    
    # SAVE BUTTON
    
    savebutton = gtk.Button()
    saveicon = gtk.Image()
    saveicon.set_from_file("py_data/icons/save.png")
    savebutton.add(saveicon)
    savebutton.set_tooltip_text("Save")
    
    toppanel.pack_start(savebutton, False)
    
    mainbox.pack_start(gtk.HSeparator(), False)
    
    
    #### SECOND PANEL
    
    
    
    
    
    
    
    
    
    
    
    
    
    ##### ACTUALL THING
    
    tablescrollable = gtk.ScrolledWindow()
    mainbox.pack_start(tablescrollable)
    
    scrollbox = gtk.VBox()
    tablescrollable.add_with_viewport(scrollbox)
    
    
    rows = ( len(userstring.split("\n")) +1 ) * 2
    if rows == 0:
        rows = 1
    
    rawtable = gtk.Table(rows, 3, False)
    scrollbox.pack_start(rawtable)
    
    eb = gtk.EventBox()
    eb.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("#777777"))
    
    
    
    rawtable.attach(gtk.Label("Amount") , 0, 1 , 0, 1)
    rawtable.attach(gtk.Label("Comment"), 1, 2 , 0, 1)
    rawtable.attach(gtk.Label("Date")   , 2, 3 , 0, 1)
    
    # an attempt to colorize a cell
    #rawtable.attach(eb, 0 , 3, 0, 1)
    
    try:
        tothescreen = userstring.split("\n")[::-1]
    except:
        tothescreen = []
    
    for x, line in enumerate(tothescreen):
        
        rawtable.attach(gtk.Label(line[:line.replace(" ", "", 1).find(" ")+1]), 0, 1 , x*2+2, x*2+3)
        rawtable.attach(gtk.Label(line[line.replace(" ", "", 1).find(" ")+1:line.rfind(" ")]), 1, 2 , x*2+2, x*2+3)
        rawtable.attach(gtk.Label(line[line.rfind(" "):]), 2, 3 , x*2+2, x*2+3)
        
        rawtable.attach(gtk.HSeparator(), 0, 3, x*2+1, x*2+2)
        
    rawtable.show_all()
    
    
    
    
    
    
    mainbox.show_all()

reload_win()

mainwindow.show_all()

gtk.main()


