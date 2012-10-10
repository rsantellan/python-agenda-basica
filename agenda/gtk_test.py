#!/usr/bin/python

# ZetCode PyGTK tutorial 
#
# This is a trivial PyGTK example
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009


import gtk
import sys

class PyApp(gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("Icon")
        self.set_size_request(250, 150)
        self.set_position(gtk.WIN_POS_CENTER)
        try:
            self.set_icon_from_file("agenda.png")
        except Exception, e:
            print e.message
            sys.exit(1)
            
        self.connect("destroy", gtk.main_quit)    
        self.show()

class PyAppButton(gtk.Window):

    def __init__(self):
        super(PyAppButton, self).__init__()
        self.set_title("Buttons")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        
        btn1 = gtk.Button("Button m1")
        btn1.set_sensitive(False)
        btn2 = gtk.Button("Button m2")
        btn3 = gtk.Button(stock=gtk.STOCK_CLOSE)
        btn4 = gtk.Button("Button m3")
        btn4.set_size_request(80, 40)

        fixed = gtk.Fixed()

        fixed.put(btn1, 20, 30)
        fixed.put(btn2, 100, 30)
        fixed.put(btn3, 20, 80)
        fixed.put(btn4, 100, 80)
        
        self.connect("destroy", gtk.main_quit)
        
        self.add(fixed)
        self.show_all()
        
class PyAppToolTip(gtk.Window):

    def __init__(self):
        super(PyAppToolTip, self).__init__()
        self.set_title("Tool tip")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        
        btn4 = gtk.Button("Button")
        btn4.set_size_request(80, 35)

        fixed = gtk.Fixed()

        fixed.put(btn4, 50, 50)
        
        self.connect("destroy", gtk.main_quit)
        
        self.set_tooltip_text("Window widget")
        btn4.set_tooltip_text("Button widget")
        
        self.add(fixed)
        self.show_all()        

# ZetCode PyGTK tutorial 
#
# This example demonstrates a Fixed
# container widget
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009

class PyAppFixed(gtk.Window):

    def __init__(self):
        super(PyAppFixed, self).__init__()
        self.set_title("Fixed")
        self.set_size_request(300, 280)
        self.set_position(gtk.WIN_POS_CENTER)
        self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
        
        try:
            self.bardejov = gtk.gdk.pixbuf_new_from_file("agenda.png")
            self.rotunda = gtk.gdk.pixbuf_new_from_file("agenda.png")
            self.mincol = gtk.gdk.pixbuf_new_from_file("agenda.png")
        except Exception, e:
            print e.message
            sys.exit(1)        
        
        image1 = gtk.Image()
        image2 = gtk.Image()
        image3 = gtk.Image()
        
        image1.set_from_pixbuf(self.bardejov)
        image2.set_from_pixbuf(self.rotunda)
        image3.set_from_pixbuf(self.mincol)
        
        fixed = gtk.Fixed()

        fixed.put(image1, 20, 20)
        fixed.put(image2, 40, 160)
        fixed.put(image3, 170, 50)
        
        self.connect("destroy", gtk.main_quit)
        
        self.add(fixed)
        self.show_all()    

# ZetCode PyGTK tutorial 
#
# This example shows how to use
# the Alignment widget
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009

class PyAppAlignment(gtk.Window):

    def __init__(self):
        super(PyAppAlignment, self).__init__()
        self.set_title("Alignment")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        
        vbox = gtk.VBox(False, 5)
        hbox = gtk.HBox(True, 3)
        valign = gtk.Alignment(0, 1, 0, 0)
        
        vbox.pack_start(valign)
        
        ok = gtk.Button("OK")
        ok.set_size_request(70,30)
        
        close = gtk.Button("Close")
        
        hbox.add(ok)
        hbox.add(close)
        
        halign = gtk.Alignment(1, 0, 0, 0)
        halign.add(hbox)
        
        vbox.pack_start(halign, False, False, 3)
        
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        
        self.show_all()   

# ZetCode PyGTK tutorial 
#
# This example shows how to use
# the Table container widget
#
# author: jan bodnar
# website: zetcode.com 
# last edited: February 2009
        
class PyAppTable(gtk.Window):
    
    def __init__(self):
        super(PyAppTable, self).__init__()
        self.set_title("Tables")
        self.set_size_request(250, 230)
        self.set_position(gtk.WIN_POS_CENTER)
        
        mb = gtk.MenuBar()
        filemenu = gtk.Menu()
        filem = gtk.MenuItem("File")
        filem.set_submenu(filemenu)
        mb.append(filem)
        
        vbox = gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        
        table = gtk.Table(5, 4, True)
        
        table.attach(gtk.Button("Cls"), 0, 1, 0, 1)
        table.attach(gtk.Button("Bck"), 1, 2, 0, 1)
        table.attach(gtk.Label(), 2, 3, 0, 1)
        table.attach(gtk.Button("Close"), 3, 4, 0, 1)
        
        table.attach(gtk.Button('7'), 0, 1, 1, 2)
        table.attach(gtk.Button('8'), 1, 2, 1, 2)
        table.attach(gtk.Button('9'), 2, 3, 1, 2)
        table.attach(gtk.Button('/'), 3, 4, 1, 2)
        
        table.attach(gtk.Button('4'), 0, 1, 2, 3)
        table.attach(gtk.Button('5'), 1, 2, 2, 3)
        table.attach(gtk.Button('6'), 2, 3, 2, 3)
        table.attach(gtk.Button('*'), 3, 4, 2, 3)
        
        table.attach(gtk.Button('3'), 0, 1, 3, 4)
        table.attach(gtk.Button('2'), 1, 2, 3, 4)
        table.attach(gtk.Button('1'), 2, 3, 3, 4)
        table.attach(gtk.Button('-'), 3, 4, 3, 4)
        
        table.attach(gtk.Button('0'), 0, 1, 4, 5)
        table.attach(gtk.Button('.'), 1, 2, 4, 5)
        table.attach(gtk.Button('='), 2, 3, 4, 5)
        table.attach(gtk.Button('+'), 3, 4, 4, 5)
        
        vbox.pack_start(gtk.Entry(), False, False, 0)
        vbox.pack_end(table, True, True, 0)
        
        self.add(vbox)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()        

class PyAppWindow(gtk.Window):
    
    def __init__(self):
        super(PyAppWindow, self).__init__()
        self.set_title("Window example")
        self.set_size_request(300, 250)
        self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        
        table = gtk.Table(8, 4, False)
        table.set_col_spacings(3)
        
        title = gtk.Label("Windows")
        
        halign = gtk.Alignment(0,0,0,0)
        halign.add(title)
        
        table.attach(halign, 0, 1, 0, 1, gtk.FILL, gtk.FILL, 0, 0)
        
        wins = gtk.TextView()
        wins.set_editable(False)
        wins.modify_fg(gtk.STATE_NORMAL, gtk.gdk.Color(5140, 5140, 5140))
        wins.set_cursor_visible(False)
        table.attach(wins, 0, 2, 1, 3, gtk.FILL | gtk.EXPAND, gtk.FILL | gtk.EXPAND, 1, 1)
        
        activate = gtk.Button("Activate")
        activate.set_size_request(50, 30)
        table.attach(activate, 3, 4, 1, 2, gtk.FILL, gtk.SHRINK, 1, 1)
        
        valing = gtk.Alignment(0, 0, 0,0 )
        close = gtk.Button("Close")
        close.set_size_request(70, 30)
        valing.add(close)
        
        table.set_row_spacing(1, 3)
        table.attach(valing, 3, 4, 2, 3, gtk.FILL, gtk.FILL | gtk.EXPAND, 1, 1 )
        
        halign2 = gtk.Alignment(0, 1, 0, 0)
        help = gtk.Button("Help")
        help.set_size_request(70, 30)
        halign2.add(help)
        
        table.set_row_spacing(3, 6)
        table.attach(halign2, 0, 1, 4, 5, gtk.FILL, gtk.FILL, 0, 0)
        
        ok = gtk.Button("Ok")
        ok.set_size_request(70, 30)
        table.attach(ok, 3, 4, 4, 5, gtk.FILL, gtk.FILL, 0, 0)
        
        self.add(table)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()
    
            
#PyApp()
#PyAppButton()
#PyAppToolTip()
#PyAppFixed()
#PyAppAlignment()
#PyAppTable()
PyAppWindow()
gtk.main()
