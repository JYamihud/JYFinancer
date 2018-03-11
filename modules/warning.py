import gtk
import pango

def warn(w=None, text="Mistake Happened"):
    
    
    
    win = gtk.Window()
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_default_size(200, 0)
    box = gtk.VBox()
    win.add(box)
    
    print text
    
    warning = gtk.Label()
    warning.modify_font(pango.FontDescription("Bold 20"))
    warning.set_markup('<span color="#FF0000">WARNING</span>')
    box.pack_start(warning)
    
    box.pack_start(gtk.Label(text))
    
    ok = gtk.Button("OK")
    def d(w=None):
        win.destroy()
    ok.connect("clicked", d)
    box.pack_start(ok)
    
    
    
    win.show_all()
    
