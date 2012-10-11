#!/usr/bin/python

import gtk

# For font visualization

import pango 

class PyAppDialogSimple(gtk.Window):
    
    def __init__(self):
        super(PyAppDialogSimple, self).__init__()
        self.set_title("Dialog")
        self.set_size_request(250, 100)
        #self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        
        table = gtk.Table(2, 2, True)
        
        info = gtk.Button("Info")
        warn = gtk.Button("Warning")
        error = gtk.Button("Error")
        question = gtk.Button("Question")
        
        info.connect("clicked", self.on_info)
        warn.connect("clicked", self.on_warn)
        error.connect("clicked", self.on_error)
        question.connect("clicked", self.on_question)
        
        table.attach(info, 0, 1, 0, 1)
        table.attach(warn, 1, 2, 0, 1)
        table.attach(error, 0, 1, 1, 2)
        table.attach(question, 1, 2, 1, 2)
        
        self.add(table)
        
        self.show_all()
        
    def on_info(self, widget):
        md = gtk.MessageDialog(self, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, 
            gtk.BUTTONS_CLOSE, "Download completed")
        md.run()
        md.destroy()
        
    def on_warn(self, widget):
        md = gtk.MessageDialog(self, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_WARNING, 
            gtk.BUTTONS_CLOSE, "Unallowed operation")
        md.run()
        md.destroy()
        
    def on_error(self, widget):
        md = gtk.MessageDialog(self, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, 
            gtk.BUTTONS_CLOSE, "Error loading file")
        md.run()
        md.destroy()
        
    def on_question(self, widget):
        md = gtk.MessageDialog(self, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION, 
            gtk.BUTTONS_CLOSE, "Are you sure to quit?")
        md.run()
        md.destroy()
        
class PyAppDialogAbout(gtk.Window):
    
    def __init__(self):
        super(PyAppDialogAbout, self).__init__()
        self.set_title("Dialog About")
        self.set_size_request(250, 100)
        #self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        button = gtk.Button("About")
        button.set_size_request(80, 30)
        button.connect("clicked", self.on_clicked)
        
        fix = gtk.Fixed()
        fix.put(button, 20, 20)
        self.add(fix)
        self.show_all()
        
    def on_clicked(self, widget):
        about = gtk.AboutDialog()
        about.set_program_name("Battery")
        about.set_version("0.1")
        about.set_copyright("(c) Jan Bodnar")
        about.set_comments("Battery is a simple tool for battery checking")
        about.set_website("http://www.zetcode.com")
        about.set_logo(gtk.gdk.pixbuf_new_from_file("battery.png"))
        about.run()
        about.destroy()
        
class PyAppDialogFontSelection(gtk.Window):
    
    def __init__(self):
        super(PyAppDialogFontSelection, self).__init__()
        self.set_title("Dialog Font Selection")
        self.set_size_request(300, 150)
        #self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        
        self.label = gtk.Label("This is a example text")
        
        button = gtk.Button("Select font")
        button.connect("clicked", self.on_clicked)
        
        fix = gtk.Fixed()
        fix.put(button, 100, 30)
        fix.put(self.label, 30, 90)
        self.add(fix)
        
        self.show_all()
        
    def on_clicked(self, widget):
        fdia = gtk.FontSelectionDialog("Select Font Name")
        
        response = fdia.run()
        
        if response == gtk.RESPONSE_OK:
            font_desc = pango.FontDescription(fdia.get_font_name())
            if font_desc:
                self.label.modify_font(font_desc)
            
        fdia.destroy()
        
class PyAppDialogColorSelection(gtk.Window):
    
    def __init__(self):
        super(PyAppDialogColorSelection, self).__init__()
        self.set_title("Dialog Color Selection")
        self.set_size_request(300, 150)
        #self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        
        self.label = gtk.Label("This is a example text")
        
        button = gtk.Button("Select Color")
        button.connect("clicked", self.on_clicked)
        
        fix = gtk.Fixed()
        fix.put(button, 100, 30)
        fix.put(self.label, 30, 90)
        self.add(fix)
        
        self.show_all()
        
    def on_clicked(self, widget):
        cdia = gtk.ColorSelectionDialog("Select Color")
        
        response = cdia.run()
        
        if response == gtk.RESPONSE_OK:
            colorsel = cdia.colorsel
            color = colorsel.get_current_color()
            self.label.modify_fg(gtk.STATE_NORMAL, color)
            
        cdia.destroy()        


#PyAppDialogSimple()
#PyAppDialogAbout()
#PyAppDialogFontSelection()
PyAppDialogColorSelection()
gtk.main()
