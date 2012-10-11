#!/usr/bin/python

# ZetCode PyGTK tutorial 
#
# This example shows a toolbar
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009

import gtk

class PyAppToolbar(gtk.Window):
    
    def __init__(self):
        super(PyAppToolbar, self).__init__()
        
        self.set_title("Toolbar")
        self.set_size_request(250, 200)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        
        toolbar = gtk.Toolbar()
        
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        
        newtb = gtk.ToolButton(gtk.STOCK_NEW)
        opentb = gtk.ToolButton(gtk.STOCK_OPEN)
        savetb = gtk.ToolButton(gtk.STOCK_SAVE)
        sep = gtk.SeparatorToolItem()
        quittb = gtk.ToolButton(gtk.STOCK_QUIT)
        
        toolbar.insert(newtb, 0)
        toolbar.insert(opentb, 1)
        toolbar.insert(savetb, 2)
        toolbar.insert(sep, 3)
        toolbar.insert(quittb, 4)
        
        quittb.connect("clicked", gtk.main_quit)
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(toolbar, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()

class PyAppDoubleToolbar(gtk.Window):
    
    def __init__(self):
        super(PyAppDoubleToolbar, self).__init__()
        
        self.set_title("Toolbar")
        self.set_size_request(350, 300)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        
        toolbar = gtk.Toolbar()
        
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        
        newtb = gtk.ToolButton(gtk.STOCK_NEW)
        opentb = gtk.ToolButton(gtk.STOCK_OPEN)
        savetb = gtk.ToolButton(gtk.STOCK_SAVE)
        
        
        toolbar.insert(newtb, 0)
        toolbar.insert(opentb, 1)
        toolbar.insert(savetb, 2)
        
        lower = gtk.Toolbar()
        lower.set_style(gtk.TOOLBAR_ICONS)
        
        quittb = gtk.ToolButton(gtk.STOCK_QUIT)
        lower.insert(quittb, 0)
        
        quittb.connect("clicked", gtk.main_quit)
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(toolbar, False, False, 0)
        vbox.pack_start(lower, False, False, 0)

        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
class PyAppUndoRedoToolbar(gtk.Window):
    
    def __init__(self):
        super(PyAppUndoRedoToolbar, self).__init__()
        self.set_title("Undo and Redo")
        self.set_size_request(350, 300)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.count = 2
        
        toolbar = gtk.Toolbar()
        
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        
        self.undo = gtk.ToolButton(gtk.STOCK_UNDO)
        self.redo = gtk.ToolButton(gtk.STOCK_REDO)
        
        sep = gtk.SeparatorToolItem()
        quittb = gtk.ToolButton(gtk.STOCK_QUIT)
        
        toolbar.insert(self.undo, 0)
        toolbar.insert(self.redo, 1)
        toolbar.insert(sep, 2)
        toolbar.insert(quittb, 3)
        
        self.undo.connect("clicked", self.on_undo)
        self.redo.connect("clicked", self.on_redo)
        quittb.connect("clicked", gtk.main_quit)
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(toolbar, False, False, 0)
        
        self.add(vbox)

        self.connect("destroy", gtk.main_quit)
        self.show_all()
        
    def on_undo(self, widget):
        self.count = self.count - 1
        
        if self.count <= 0:
            self.undo.set_sensitive(False)
            self.redo.set_sensitive(True)
        
    def on_redo(self, widget):
        self.count = self.count + 1
        
        if self.count >= 5:
            self.undo.set_sensitive(True)
            self.redo.set_sensitive(False)
        
        
        
                
        
PyAppToolbar()
#PyAppDoubleToolbar()
#PyAppUndoRedoToolbar()
gtk.main()
