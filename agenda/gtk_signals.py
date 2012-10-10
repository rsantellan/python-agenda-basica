#!/usr/bin/python

import gtk

import gobject

class PyAppSignals(gtk.Window):
    
    def __init__(self):
        super(PyAppSignals, self).__init__()
        
        self.set_title("Quit Button")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", self.on_destroy)
        
        fixed = gtk.Fixed()

        quit = gtk.Button("Quit")
        quit.connect("clicked", self.on_clicked)
        quit.set_size_request(80, 35)

        fixed.put(quit, 50, 50)

        self.add(fixed)
        self.show_all()
        
    def on_destroy(self, widget):
        gtk.main_quit()
        
    def on_clicked(self, widget):
        gtk.main_quit()

class Sender(gobject.GObject):
    
    def __init__(self):
        self.__gobject_init__()
        
class Reciever(gobject.GObject):
    
    def __init__(self, sender):
        self.__gobject_init__()
        
        sender.connect('z_signal', self.report_signal)
        
    def report_signal(self, sender):
        print "Receiver react to z_signal"
        
class RunSenderReciever(object):
    
    def __init__(self):
        print "Inicio"
        
        gobject.type_register(Sender)
        gobject.signal_new("z_signal", Sender, gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, ())
                   
        sender = Sender()
        receiver = Reciever(sender)
        
        sender.connect('z_signal', self.user_callback)
        sender.emit('z_signal')
        
    def user_callback(self, object):
        print "User callback reacts to z_signal"
        
class PyAppOverwriteConfigureEvent(gtk.Window):
    
    __gsignals__ = {
        "configure-event" : "override"
    }
    
    def __init__(self):
        super(PyAppOverwriteConfigureEvent, self).__init__()
        
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        self.show_all()
        
    def do_configure_event(self, event):
        
        title = "{0}, {1}".format(event.x, event.y)
        self.set_title(title)
        gtk.Window.do_configure_event(self, event)
        
        
class PyAppButtonSignals(gtk.Window):
    
    def __init__(self):
        
        super(PyAppButtonSignals, self).__init__()
        
        self.set_title("Signals")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        
        self.quit = gtk.Button("Quit")
        
        self.quit.connect("pressed", self.on_pressed)        
        self.quit.connect("released", self.on_released)        
        self.quit.connect("clicked", self.on_clicked)
        
        self.quit.set_size_request(80, 35)
        
        fixed = gtk.Fixed()
        
        fixed.put(self.quit, 50, 50)        
        
        self.add(fixed)
        self.show_all()
        self.emit_signal()
        
    def emit_signal(self):
        
        event = gtk.gdk.Event(gtk.gdk.BUTTON_RELEASE)
        event.button = 1
        event.window = self.quit.window
        event.send_event = True
        
        self.quit.emit("button-release-event", event)
        
    def on_clicked(self, widget):
        print "clicked"
        
    def on_released(self, widget):
        print "released"
        
    def on_pressed(self, widget):
        print "pressed"        

class PyAppBlockEvent(gtk.Window):
    
    def __init__(self):
        super(PyAppBlockEvent, self).__init__()
        
        self.set_title("Block event")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        
        fixed = gtk.Fixed()
        button = gtk.Button("Click")
        button.set_size_request(80, 35)
        self.id = button.connect("clicked", self.on_clicked)
        fixed.put(button, 30, 50)
        
        check = gtk.CheckButton("Connect")
        check.set_active(True)
        check.connect("clicked", self.toggle_blocking, button)
        fixed.put(check, 130, 50)
        
        self.add(fixed)
        self.show_all()
        
    def on_clicked(self, widget):
        print "Clicked"
        
    def toggle_blocking(self, checkbox, button):
        if checkbox.get_active():
            button.handler_unblock(self.id)
        else:
            button.handler_block(self.id)
        
        
        
        
        
#PyAppSignals()
#gtk.main()        

#RunSenderReciever()

#PyAppOverwriteConfigureEvent()
#gtk.main()

#PyAppButtonSignals()
#gtk.main()

PyAppBlockEvent()
gtk.main()
