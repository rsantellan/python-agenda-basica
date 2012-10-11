#!/usr/bin/python

import gtk
import sys

#This is needed for the Icon View

import os

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

class PyAppWidgetToggle(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetToggle, self).__init__()
        
        self.set_title("- Toggle -")
        self.set_size_request(350, 240)
        #self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        self.color = [0, 0, 0]
        
        red = gtk.ToggleButton("Red")
        red.set_size_request(80, 35)
        red.connect("clicked", self.onred)
        
        green = gtk.ToggleButton("Green")
        green.set_size_request(80, 35)
        green.connect("clicked", self.ongreen)
        
        blue = gtk.ToggleButton("Blue")
        blue.set_size_request(80, 35)
        blue.connect("clicked", self.onblue)
        
        self.darea = gtk.DrawingArea()
        self.darea.set_size_request(150, 150)
        self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.color_parse("black"))
        
        fixed = gtk.Fixed()
        fixed.put(red, 30, 30)
        fixed.put(green, 30, 80)
        fixed.put(blue, 30, 130)
        fixed.put(self.darea, 130, 30)
        
        self.add(fixed)
        
        self.show_all()
        
    def onred(self, widget):
        if widget.get_active():
            self.color[0] = 65535
        else:
            self.color[0] = 0
        self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(self.color[0], self.color[1], self.color[2]))
        
    def ongreen(self, widget):
        if widget.get_active():
            self.color[1] = 65535
        else:
            self.color[1] = 0
        self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(self.color[0], self.color[1], self.color[2]))
        
    def onblue(self, widget):
        if widget.get_active():
            self.color[2] = 65535
        else:
            self.color[2] = 0
        self.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(self.color[0], self.color[1], self.color[2]))

class PyAppWidgetCalendar(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetCalendar, self).__init__()
        
        self.set_title("- Calendar -")
        self.set_size_request(300, 270)
        #self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        self.label = gtk.Label(" ... ")
        
        calendar = gtk.Calendar()
        calendar.connect("day_selected", self.on_day_selected)
        
        fixed = gtk.Fixed()
        fixed.put(self.label, 20, 20)
        
        fixed.put(calendar, 20, 60)
        
        self.add(fixed)
        self.show_all()
        
    def on_day_selected(self, widget):
        (year, month, day) = widget.get_date()
        self.label.set_label("{0} - {1} - {2}".format(day, month, year))
        
class PyAppWidgetIconView(gtk.Window):
    
    def __init__(self):
        
        super(PyAppWidgetIconView, self).__init__()
        self.set_title("- Icon view -")
        self.set_size_request(650, 400)
        #self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)        
        self.connect("destroy", gtk.main_quit)
        
        self.col_path = 0
        self.col_pixbuf = 1
        self.col_is_directory = 2
        
        self.current_directory = "/"
        
        vbox = gtk.VBox(False, 0)
        
        toolbar = gtk.Toolbar()
        vbox.pack_start(toolbar, False, False, 0)
        
        self.upButton = gtk.ToolButton(gtk.STOCK_GO_UP)
        self.upButton.set_is_important(True)
        self.upButton.set_sensitive(False)
        toolbar.insert(self.upButton, -1)
        
        homeButton = gtk.ToolButton(gtk.STOCK_HOME)
        homeButton.set_is_important(True)
        toolbar.insert(homeButton, -1)
        
        self.fileIcon = self.get_icon(gtk.STOCK_FILE)
        self.dirIcon = self.get_icon(gtk.STOCK_DIRECTORY)
        
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        vbox.pack_start(sw, True, True, 0)
        
        self.store = self.create_store()
        self.fill_store()
        
        iconView = gtk.IconView(self.store)
        iconView.set_selection_mode(gtk.SELECTION_MULTIPLE)
        
        self.upButton.connect("clicked", self.on_up_clicked)
        homeButton.connect("clicked", self.on_home_clicked)
        
        iconView.set_text_column(self.col_path)
        iconView.set_pixbuf_column(self.col_pixbuf)
        
        iconView.connect("item-activated", self.on_item_activated)
        
        sw.add(iconView)
        iconView.grab_focus()
        
        self.add(vbox)
        self.show_all()
        
    def get_icon(self, name):
        theme = gtk.icon_theme_get_default()
        return theme.load_icon(name, 48, 0)
        
    def create_store(self):
        store = gtk.ListStore(str, gtk.gdk.Pixbuf, bool)
        store.set_sort_column_id(self.col_path, gtk.SORT_ASCENDING)
        return store
        
    def fill_store(self):
        self.store.clear()
        
        if self.current_directory == None:
            return
        
        for fl in os.listdir(self.current_directory):
            if not fl[0] == ".":
                if os.path.isdir(os.path.join(self.current_directory, fl)):
                    self.store.append([fl, self.dirIcon, True])
                else:
                    self.store.append([fl, self.fileIcon, True])
                    
    def on_up_clicked(self, widget):
        self.current_directory = os.path.dirname(self.current_directory)
        print self.current_directory
        self.fill_store()
        sensitive = True
        if self.current_directory == "/": 
            sensitive = False
        self.upButton.set_sensitive(sensitive)
        
    def on_home_clicked(self, widget):
        self.current_directory = os.path.realpath(os.path.expanduser('~'))
        self.fill_store()
        self.upButton.set_sensitive(True)
    
    def on_item_activated(self, widget, item):
        model = widget.get_model()
        path = model[item][self.col_path]
        isDir = model[item][self.col_is_directory]

        if not isDir:
            return
        
        aux_path = ""
        if self.current_directory != "/":
                aux_path = self.current_directory
        self.current_directory = aux_path + os.path.sep + path
        self.fill_store()
        self.upButton.set_sensitive(True)
    
    
class PyAppListView(gtk.Window):
    
    def __init__(self):
        super(PyAppListView, self).__init__()
        self.set_title("- List view -")
        self.set_size_request(350, 150)
        #self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)        
        self.connect("destroy", gtk.main_quit)
        
        self.actresses = [('jessica alba', 'pomona', '1981'), ('sigourney weaver', 'new york', '1949'),
    ('angelina jolie', 'los angeles', '1975'), ('natalie portman', 'jerusalem', '1981'),
    ('rachel weiss', 'london', '1971'), ('scarlett johansson', 'new york', '1984' )]
    
        vbox = gtk.VBox(False, 8)
        
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        vbox.pack_start(sw, True, True, 0)
        
        store = self.create_model()
        
        treeView = gtk.TreeView(store)
        treeView.connect("row-activated", self.on_activated)
        treeView.set_rules_hint(True)
        sw.add(treeView)
        
        self.create_columns(treeView)
        
        self.statusbar = gtk.Statusbar()
        
        vbox.pack_start(self.statusbar, False, False, 0)
        
        self.add(vbox)
        self.show_all()
        
    def create_model(self):
        store = gtk.ListStore(str, str, str)
        
        for act in self.actresses:
            store.append([act[0], act[1], act[2]])
            
        return store
        
    def create_columns(self, treeView):
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Name", renderText, text = 0)
        column.set_sort_column_id(0)
        treeView.append_column(column)
        
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Place", renderText, text = 1)
        column.set_sort_column_id(1)
        treeView.append_column(column)
        
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Year", renderText, text = 2)
        column.set_sort_column_id(2)
        treeView.append_column(column)
        
    def on_activated(self, widget, row, col):
        model = widget.get_model()
        text = model[row][0] + ", " + model[row][1] + ", " + model[row][2]
        self.statusbar.push(0, text)
        
        
class PyAppWidgetTreeView(gtk.Window):
    
    def __init__(self):
        super(PyAppWidgetTreeView, self).__init__()
        self.set_title("- Tree view -")
        self.set_size_request(400, 300)
        #self.set_border_width(2)
        self.set_position(gtk.WIN_POS_CENTER)        
        self.connect("destroy", gtk.main_quit)
        
        tree = gtk.TreeView()
        
        languages = gtk.TreeViewColumn()
        languages.set_title("Programming languages")
        
        cell = gtk.CellRendererText()
        languages.pack_start(cell, True)
        languages.add_attribute(cell, "text", 0)
        
        treeStore = gtk.TreeStore(str)
        
        it = treeStore.append(None, ["Scripting Languages"])
        treeStore.append(it, ["Python"])
        treeStore.append(it, ["PHP"])
        treeStore.append(it, ["Perl"])
        treeStore.append(it, ["Ruby"])
        
        it = treeStore.append(None, ["Compiling Languages"])
        treeStore.append(it, ["C#"])
        treeStore.append(it, ["Java"])
        treeStore.append(it, ["C"])
        treeStore.append(it, ["C++"])
        
        tree.append_column(languages)
        
        tree.set_model(treeStore)
        
        self.add(tree)
        
        
        self.show_all()
        
    
        
        
                                
#PyAppWidgetLabel()
#PyAppWidgetCheckButton()
#PyAppWidgetCombo()
#PyAppWidgetImage()
#PyAppWidgetEntry()
#PyAppWidgetHScale()
#PyAppWidgetToggle()
#PyAppWidgetCalendar()
#PyAppWidgetIconView()
#PyAppListView()
PyAppWidgetTreeView()
gtk.main()
