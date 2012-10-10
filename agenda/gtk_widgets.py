#!/usr/bin/python

import gtk
import sys

lyrics = """Meet you downstairs in the bar and heard
your rolled up sleeves and your skull t-shirt
You say why did you do it with him today?
and sniff me out like I was Tanqueray

cause you're my fella, my guy
hand me your stella and fly
by the time I'm out the door
you tear men down like Roger Moore

I cheated myself
like I knew I would
I told ya, I was trouble
you know that I'm no good"""


class PyAppWidgetLabel(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetLabel, self).__init__()
        
        self.set_title("Label")
        #self.set_size_request(350, 400)
        self.set_border_width(8)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        label = gtk.Label(lyrics)
        self.add(label)
        self.show_all()

class PyAppWidgetCheckButton(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetCheckButton, self).__init__()
        
        self.set_title("Check button")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        
        fixed = gtk.Fixed()
        
        button = gtk.CheckButton("Show title")
        button.set_active(True)
        button.unset_flags(gtk.CAN_FOCUS)
        button.connect("clicked", self.on_clicked)
        
        fixed.put(button, 50, 50)
        
        self.add(fixed)
        self.show_all()
        
    def on_clicked(self, widget):
        if widget.get_active():
            self.set_title("Check Button")
        else:
            self.set_title(" ")

class PyAppWidgetCombo(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetCombo, self).__init__()
        
        self.set_title("Combo")
        self.set_size_request(250, 200)
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect("destroy", gtk.main_quit)
        
        cb = gtk.combo_box_new_text()
        cb.connect("changed", self.on_changed)
        
        cb.append_text("Ubuntu")
        cb.append_text("Mint")
        cb.append_text("Gentoo")
        cb.append_text("Redhat")
        
        self.label = gtk.Label("-")
        
        fixed = gtk.Fixed()
        fixed.put(cb, 20, 30)
        fixed.put(self.label, 50, 60)
        
        
        self.add(fixed)
        self.show_all()
    
    def on_changed(self, widget):
        self.label.set_label(widget.get_active_text())


class PyAppWidgetImage(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetImage, self).__init__()
        
        self.set_title("- Image -")
        #self.set_size_request(350, 400)
        self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        image = gtk.Image()
        image.set_from_file("agenda.png")
        self.add(image)
        self.show_all()

class PyAppWidgetEntry(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetEntry, self).__init__()
        
        self.set_title("- Entry -")
        self.set_size_request(250, 200)
        #self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        self.label = gtk.Label(" ... ")
        
        entry = gtk.Entry()
        entry.add_events(gtk.gdk.KEY_RELEASE_MASK)
        entry.connect("key-release-event", self.on_key_release)
        
        fixed = gtk.Fixed()
        fixed.put(self.label, 20, 20)
        
        fixed.put(entry, 20, 60)
        
        self.add(fixed)
        self.show_all()
        
    def on_key_release(self, widget, event):
        self.label.set_label(widget.get_text())
        
class PyAppWidgetHScale(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetHScale, self).__init__()
        
        self.set_title("- HScale -")
        self.set_size_request(250, 200)
        #self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)
        
        #self.connect("destroy", gtk.main_quit)
        self.connect("destroy", lambda w: gtk.main_quit())
        
        scale = gtk.HScale()
        scale.set_range(0, 100)
        scale.set_increments(1, 10)
        scale.set_digits(0)
        scale.set_size_request(160, 35)
        scale.connect("value-changed", self.on_changed)
        
        self.load_pixbufs()
        
        self.image = gtk.Image()
        self.image.set_from_pixbuf(self.mutp)
        
        fix = gtk.Fixed()
        fix.put(scale, 20, 40)
        fix.put(self.image, 219, 50)
        
        self.add(fix)
        self.show_all()        
        
    def load_pixbufs(self):
    
        try:
            self.mutp = gtk.gdk.pixbuf_new_from_file("mute.png")
            self.minp = gtk.gdk.pixbuf_new_from_file("min.png")
            self.medp = gtk.gdk.pixbuf_new_from_file("med.png")
            self.maxp = gtk.gdk.pixbuf_new_from_file("max.png")
            
        except Exception, e: 
            print "Error reading Pixbufs"
            print e.message
            sys.exit(1)
            
    def on_changed(self, widget):
        val = widget.get_value()

        if val == 0:
            self.image.set_from_pixbuf(self.mutp)
        elif val > 0 and val <= 30:
            self.image.set_from_pixbuf(self.minp)
        elif val > 30 and val < 80:
            self.image.set_from_pixbuf(self.medp)
        else: 
            self.image.set_from_pixbuf(self.maxp)                    
                        
#PyAppWidgetLabel()
#PyAppWidgetCheckButton()
#PyAppWidgetCombo()
#PyAppWidgetImage()
#PyAppWidgetEntry()
PyAppWidgetHScale()
gtk.main()
