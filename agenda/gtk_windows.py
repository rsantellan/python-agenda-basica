#!/usr/bin/python

import gtk

class PyAppFirstWindow(gtk.Window):
    
    def __init__(self):
        super(PyAppFirstWindow, self).__init__()
        self.set_title("PyAppFirstWindow")
        self.set_size_request(500, 400)
        #self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        button = gtk.Button("new window")
        button.connect("clicked", self.open_window)
        
        fixed = gtk.Fixed()
        fixed.put(button, 20, 20)
        
        self.add(fixed)
        self.show_all()
        
    def open_window(self, widget):
        PyAppSecondWindow()

class PyAppSecondWindow(gtk.Window):
    
    def __init__(self):
        super(PyAppSecondWindow, self).__init__()
        self.set_title("PyAppSecondWindow")
        self.set_size_request(250, 100)
        #self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER_ON_PARENT)
        
        self.connect("destroy", self.close_window)
        
        self.show_all()
        
    def close_window(self, widget):
        self.destroy()

PyAppFirstWindow()
gtk.main()
