#!/usr/bin/python

# ZetCode PyGTK tutorial 
#
# This example shows a simple menu
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009

import gtk

class PyAppBasicMenu(gtk.Window):
    
    def __init__(self):
        
        super(PyAppBasicMenu, self).__init__()
        self.set_title("Basic Menu")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        
        mb = gtk.MenuBar()
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)
        
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        
        filemenu.append(exit)
        
        mb.append(filem)
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()

class PyAppMenuShortcuts(gtk.Window):
    
    def __init__(self):
        super(PyAppMenuShortcuts, self).__init__()
        self.set_title("another menu")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        
        mb = gtk.MenuBar()
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("_File")
        filem.set_submenu(filemenu)
        
        agr = gtk.AccelGroup()
        self.add_accel_group(agr)
        
        newi = gtk.ImageMenuItem(gtk.STOCK_NEW, agr)
        key, mod = gtk.accelerator_parse("<Control>N")
        newi.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        filemenu.append(newi)
        
        
        openm = gtk.ImageMenuItem(gtk.STOCK_OPEN, agr)
        key, mod = gtk.accelerator_parse("<Control>O")
        openm.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        filemenu.append(openm)
        
        sep = gtk.SeparatorMenuItem()
        filemenu.append(sep)
        
        exit = gtk.ImageMenuItem(gtk.STOCK_QUIT, agr)
        key, mod = gtk.accelerator_parse("<Control>Q")
        exit.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        
        exit.connect("activate", gtk.main_quit)
        
        filemenu.append(exit)
        
        mb.append(filem)
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
class PyAppCheckMenu(gtk.Window):
    
    def __init__(self):
        super(PyAppCheckMenu, self).__init__()
        self.set_title("Check box menu")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        
        mb = gtk.MenuBar()
        
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)
        
        viewmenu = gtk.Menu()
        view = gtk.MenuItem("View")
        view.set_submenu(viewmenu)
        
        stat = gtk.CheckMenuItem("View status bar")
        stat.set_active(True)
        stat.connect("activate", self.on_status_view)
        viewmenu.append(stat)
        
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)
        
        mb.append(filem)
        mb.append(view)
        
        self.statusbar = gtk.Statusbar()
        self.statusbar.push(1, "Ready")
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        vbox.pack_start(gtk.Label(), True, False, 0)
        vbox.pack_start(self.statusbar, False, False, 0)
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
    def on_status_view(self, widget):
        print widget
        if widget.active:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    
class PyAppSubmenu(gtk.Window):
    
    def __init__(self):
        super(PyAppSubmenu, self).__init__()
        
        self.set_title("Sub menu")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        
        mb = gtk.MenuBar()
        
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)
        
        mb.append(filem)
        
        imenu = gtk.Menu()
        
        importm = gtk.MenuItem("Import")
        importm.set_submenu(imenu)
        
        inews = gtk.MenuItem("Import news feed...")
        ibookmarks = gtk.MenuItem("Import Bookmarks")
        imail = gtk.MenuItem("Import emails...")
        
        imenu.append(inews)
        imenu.append(ibookmarks)
        imenu.append(imail)
        
        filemenu.append(importm)
        
        exit = gtk.MenuItem("Exit")
        exit.connect("activate", gtk.main_quit)
        filemenu.append(exit)
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
#PyAppBasicMenu()
PyAppMenuShortcuts()
#PyAppCheckMenu()
#PyAppSubmenu()
gtk.main()
