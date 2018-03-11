import gtk

def get():
    
        
    dialog = gtk.FileChooserDialog("Select File",
                       None,
                       gtk.FILE_CHOOSER_ACTION_SAVE,
                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    dialog.set_default_response(gtk.RESPONSE_OK)

    
    filter = gtk.FileFilter()
    filter.set_name("JYFI files")
    filter.add_pattern("*.jyfi")
    dialog.add_filter(filter)
    
    filter = gtk.FileFilter()
    filter.set_name("TXT file")
    filter.add_pattern("*.txt")
    dialog.add_filter(filter)
    
    filter = gtk.FileFilter()
    filter.set_name("All files")
    filter.add_pattern("*")
    dialog.add_filter(filter)
    
    response = dialog.run()
    if response == gtk.RESPONSE_OK:
        
        filename = dialog.get_filename()
    
    dialog.destroy()
    return filename
