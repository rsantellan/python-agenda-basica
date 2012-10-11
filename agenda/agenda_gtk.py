#!/usr/bin/python

import gtk
from options import setup_options
from basicdb import BasicDb
from contacto import Contacto
from ValidatorException import EmailValidatorException

class AgendaWindow(gtk.Window):
    
    def __init__(self):
        super(AgendaWindow, self).__init__()
        
        self.set_title("Agenda")
        self.set_size_request(500, 400)
        self.set_position(gtk.WIN_POS_CENTER)
        
        self.connect("destroy", gtk.main_quit)
        
        # Database parameters
        self.page_limit = setup_options.getLimit()
        self.current_page = 1
        self.items_quantity = 0
        self.db = BasicDb()
        
        #Contact id
        self.contact_id = 0
        
        # Menu bar
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
        
        sep = gtk.SeparatorMenuItem()
        filemenu.append(sep)
        
        exit = gtk.ImageMenuItem(gtk.STOCK_QUIT, agr)
        key, mod = gtk.accelerator_parse("<Control>Q")
        exit.add_accelerator("activate", agr, key, mod, gtk.ACCEL_VISIBLE)
        
        exit.connect("activate", gtk.main_quit)
        newi.connect("activate", self.add_contact)
        
        filemenu.append(exit)
        
        mb.append(filem)
        
        
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        
        toolbar = gtk.Toolbar()
        
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        
        newtb = gtk.ToolButton(gtk.STOCK_NEW)
        self.back = gtk.ToolButton(gtk.STOCK_GO_BACK)
        self.back.set_sensitive(False)
        self.next = gtk.ToolButton(gtk.STOCK_GO_FORWARD)
        self.next.set_sensitive(False)
        
        sep = gtk.SeparatorToolItem()
        quittb = gtk.ToolButton(gtk.STOCK_QUIT)
        
        toolbar.insert(newtb, 0)
        toolbar.insert(self.back, 1)
        toolbar.insert(self.next, 2)
        toolbar.insert(sep, 3)
        toolbar.insert(quittb, 4)
        
        newtb.connect("clicked", self.add_contact)
        quittb.connect("clicked", gtk.main_quit)
        self.back.connect("clicked", self.previous_page)
        self.next.connect("clicked", self.next_page)
        
        vbox = gtk.VBox(False, 3)
        
        vbox.pack_start(mb, False, False, 0)
        vbox.pack_start(toolbar, False, False, 0)
        vbox.pack_start(sw, True, True, 0)
        
        self.store = self.create_model()
        
        
        
        self.treeView = gtk.TreeView(self.store)
        self.treeView.connect("row-activated", self.on_activated)
        self.treeView.set_rules_hint(True)
        
        self.populate_model()
        
        self.selected = self.treeView.get_selection()
        self.selected.connect("changed", self.on_changed)
        
        sw.add(self.treeView)
        
        self.create_columns(self.treeView)
        
        hbox = gtk.HBox(True, 3)
        self.edit = gtk.Button("Edit")
        self.edit.set_size_request(70,30)
        self.edit.set_sensitive(False)
        self.edit.connect("clicked", self.edit_contact)
        self.label = gtk.Label(" - ")
        
        self.delete = gtk.Button("Delete")
        self.delete.set_size_request(70,30)
        self.delete.set_sensitive(False)
        self.delete.connect("clicked", self.delete_contact)
        
        hbox.add(self.label)
        hbox.add(self.edit)
        hbox.add(self.delete)
        
        halign = gtk.Alignment(1, 0, 0, 0)
        halign.add(hbox)
        vbox.pack_start(halign, False, False, 3)
        
        self.add(vbox)
        
        self.show_all()
        
        
    def on_changed(self, selection):
        
        # get the model and the iterator that points at the data in the model
        (model, iter) = selection.get_selected()
         # set the label to a new value depending on the selection, if there is one
        if iter is not None:
            name = model[iter][1]
            last_name = model[iter][2]
            self.contact_id = int(model[iter][0])
            self.label.set_text("{0} - {1}".format(name, last_name))
            self.edit.set_sensitive(True)
            self.delete.set_sensitive(True)
        else:
            self.label.set_text(" - ")
            self.edit.set_sensitive(False)
            self.delete.set_sensitive(False)
        return True
    
    def previous_page(self, widget):
        if self.current_page > 1:
            self.current_page = self.current_page - 1
            self.populate_model()
        self.enable_next_previous()

    def next_page(self, widget):
        self.current_page = self.current_page + 1
        self.populate_model()
        self.enable_next_previous()
        
    def enable_next_previous(self):
        if self.current_page > 1:
            self.back.set_sensitive(True)
        else:
           self.back.set_sensitive(False)
            
        if (self.current_page * self.page_limit) < self.items_quantity:
            self.next.set_sensitive(True)
        else:
           self.next.set_sensitive(False)
            
    def create_model(self):
        store = gtk.ListStore(str, str, str, str, str, str)
        return store
        
    def populate_model(self):
        self.store.clear()
        self.items_quantity = self.db.retrieveDb().retrieveAllCount()
        contactos = self.db.retrieveDb().selectAll(self.page_limit, self.current_page)
        for contacto in contactos:
            self.store.append([contacto.id, contacto.name, contacto.last_name, contacto.email, contacto.mobile, contacto.telephone])
    
    def on_activated(self, widget,  row, col):
        
        print 'activated'
        
    def create_columns(self, treeView):
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Id", renderText, text = 0)
        column.set_sort_column_id(0)
        treeView.append_column(column)
        
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Name", renderText, text = 1)
        column.set_sort_column_id(1)
        treeView.append_column(column)
        
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Last Name", renderText, text = 2)
        column.set_sort_column_id(2)
        treeView.append_column(column)
        
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Email", renderText, text = 3)
        column.set_sort_column_id(3)
        treeView.append_column(column)
        
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Mobile", renderText, text = 4)
        column.set_sort_column_id(4)
        treeView.append_column(column)
        
        renderText = gtk.CellRendererText()
        column = gtk.TreeViewColumn("Telephone", renderText, text = 5)
        column.set_sort_column_id(5)
        treeView.append_column(column)
        
    def edit_contact(self, widget):
        cont = ContactWindow(self.contact_id)
        cont.connect("destroy", self.contact_destroyed)
        
    def delete_contact(self, widget):
        md = gtk.MessageDialog(self, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_QUESTION, 
            gtk.BUTTONS_YES_NO, "Are you sure to delete?")
        response = md.run()
        md.destroy()
        if response == gtk.RESPONSE_YES:
            self.db.retrieveDb().delete(self.contact_id)
            self.populate_model()
        
    def add_contact(self, widget):
        cont = ContactWindow()
        cont.connect("destroy", self.contact_destroyed)
        
    def contact_destroyed(self, widget):
        self.populate_model()
        
    def start_up(self):
        gtk.main()
        
class ContactWindow(gtk.Window):
    
    def __init__(self, identifier = 0):
        super(ContactWindow, self).__init__()
        
        self.aux_contact = None
        
        #Database parameter
        self.db = BasicDb()
        
        is_new = True
        if identifier == 0:
            self.set_title("Add Contact")
            self.aux_contact = Contacto()
        else:
            self.set_title("Edit Contact")
            self.aux_contact = self.db.retrieveDb().findOne(identifier)
            is_new = False
            
        self.set_size_request(400, 400)
        
        self.set_position(gtk.WIN_POS_CENTER_ON_PARENT)
        
        self.connect("destroy", self.close_window)
        
        table = gtk.Table(6, 2, True)
        
        self.name_entry = gtk.Entry()
        self.last_name_entry = gtk.Entry()
        self.email_entry = gtk.Entry()
        self.mobile_entry = gtk.Entry()
        self.telephone_entry = gtk.Entry()
        
        if not is_new:
            self.name_entry.set_text(self.aux_contact.name)
            self.last_name_entry.set_text(self.aux_contact.last_name)
            self.email_entry.set_text(self.aux_contact.email)
            self.mobile_entry.set_text(self.aux_contact.mobile)
            self.telephone_entry.set_text(self.aux_contact.telephone)
        
        table.attach(gtk.Label("Name"), 0, 1, 0 ,1 )
        table.attach(self.name_entry, 1, 2, 0 ,1 )
        table.attach(gtk.Label("Last Name"), 0, 1, 1 , 2)
        table.attach(self.last_name_entry, 1, 2, 1 ,2 )
        
        table.attach(gtk.Label("Email"), 0, 1, 2 ,3 )
        table.attach(self.email_entry, 1, 2, 2 ,3 )
        table.attach(gtk.Label("Mobile"), 0, 1, 3 ,4 )
        table.attach(self.mobile_entry, 1, 2, 3 ,4 )
        
        table.attach(gtk.Label("Telephone"), 0, 1, 4 ,5 )
        table.attach(self.telephone_entry, 1, 2, 4 ,5 )
        
        button_save = gtk.Button("Save")
        button_cancel = gtk.Button("Cancel")
        
        button_save.set_size_request(60, 60)
        button_cancel.set_size_request(60, 60)
        
        button_save.connect("clicked", self.save_contacto)
        button_cancel.connect("clicked", self.close_window)
        
        table.attach(button_save, 0, 1, 5 ,6 )
        table.attach(button_cancel, 1, 2, 5 ,6 )
        
        
        self.add(table)
        
        
        self.show_all()
        
    def save_contacto(self, widget):
        try:
            self.aux_contact.set_name(self.name_entry.get_text())
            self.aux_contact.set_last_name(self.last_name_entry.get_text())
            self.aux_contact.set_email(self.email_entry.get_text())
            self.aux_contact.set_mobile(self.mobile_entry.get_text())
            self.aux_contact.set_telephone(self.telephone_entry.get_text())
            if self.aux_contact.id > 0:
                self.db.retrieveDb().update(self.aux_contact)
            else:
                self.db.retrieveDb().insert(self.aux_contact)
            self.destroy()   
        except EmailValidatorException, e:
            md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, e.args[0])
            md.run()
            md.destroy()
        
        
        
    def close_window(self, widget):
        self.destroy()
