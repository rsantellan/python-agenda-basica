#! /usr/bin/python

from contacto import Contacto
from ValidatorException import EmailValidatorException
from sys import exit
from basicdb import BasicDb
from options import setup_options

class AgendaDatabase(object):
    
    def __init__(self):
        self.db = BasicDb()
        print self.db
        
    def create_contact(self):
        print "========== Create a new contact ================"
        aux = Contacto()
        name = raw_input("[Name] > ")
        aux.set_name(name)
        last_name = raw_input("[Last Name] > ")
        aux.set_last_name(last_name)
        has_errors = True
        while has_errors:
            try:
                email = raw_input("[Email] > ")
                aux.set_email(email)
                has_errors = False
            except EmailValidatorException:
                print "Invalid email"
        
        mobile = raw_input("[Mobile] > ")
        aux.set_mobile(mobile)
        telephone = raw_input("[Telephone] > ")
        aux.set_telephone(telephone)
        
        aux.id = self.db.retrieveDb().insert(aux)
        
        
        

    def edit_contact(self, identifier):
        print "========== Edit a contact ================"
        print "========== In case you want to keep the value press ENTER ============ "
        aux = self.db.retrieveDb().findOne(identifier)
        if aux == None:
            print "Ups... None finded"
            return
        save_object = False
        #if test == "":
        #    print "test matchea a vacio '' "

        name = raw_input("[Name :({0})] > ".format(aux.name))
        if name != "":
            aux.set_name(name)
            save_object = True
        last_name = raw_input("[Last Name :({0})] > ".format(aux.last_name))
        if last_name != "":
            aux.set_last_name(last_name)
            save_object = True
        has_errors = True
        while has_errors:
            try:
                email = raw_input("[Email :({0})] > ".format(aux.email))
                if email != "":
                    aux.set_email(email)
                    save_object = True
                has_errors = False
            except EmailValidatorException:
                print "Invalid email"
        
        mobile = raw_input("[Mobile :({0})] > ".format(aux.mobile))
        if mobile != "":
            aux.set_mobile(mobile)
            save_object = True
        telephone = raw_input("[Telephone :({0})] > ".format(aux.telephone))
        if telephone != "":
            aux.set_telephone(telephone)
            save_object = True
        
        if save_object:
            self.db.retrieveDb().update(aux)

    def delete_contact(self, itemId):
        print "========== Deleting contact  ==============="
        option = raw_input("[Are you sure? (Y/N)] >")
        if option == "Y":
            self.db.retrieveDb().delete(itemId)
            print "The contact has been deleted"
        else:
            print "The contact will remain"

    def list_contacts(self, limit, page):
        print "========== List all contact ================"
        print "===========In case you want to delete a contact press d plus the number =========================="
        quantity_contactos = self.db.retrieveDb().retrieveAllCount();
        #print quantity_contactos
        number = 1
        while number != 0:
            contactos = self.db.retrieveDb().selectAll(limit, page)
            for contact in contactos:
                print "{0}: {1}".format(contact.id, contact)
            
            if page > 1:
                print "To go to the previous page press < "
            
            if (page * limit) < quantity_contactos:
                print "To go to the next page press > "
                
            option = raw_input("Select the number to edit or 0 to come back\n")
            try:
                if option == "<":
                    self.list_contacts(limit, page - 1)
                    number = 0
                elif option == ">":
                    self.list_contacts(limit, page + 1)
                    number = 0
                else:
                    if option != "":
                        list_option = list(option)
                        if list_option.pop(0) == "d":
                            option = "".join(list_option)
                            item_option = int(option)
                            self.delete_contact(item_option)
                            #print item_option
                            #print "".join(list_option)
                            #return
                        else:
                            number = int(option)
                            if number != 0:
                                self.edit_contact(number)
                    else:
                        print "Select an option"
                        
            except ValueError:
                print "It has to be a number"

    def close_program(self):
        print "Thank you for using contact 1.0.1"
        exit(0)

    def init_agenda(self):
        main_menu_text = {1 : 'Create new', 2: 'List', 3 : 'Exit'}
        main_menu_options = {1 : self.create_contact, 2: self.list_contacts, 3 : self.close_program}

        options = { 'main' : { 'text' : main_menu_text, 'options' : main_menu_options}}
        start_point = 'main'

        selected = start_point
        print "========== Welcome to contact 1.0.1 ================"

        while True:
            print "========== Main menu ================"
            displayed = options[selected]['text']
            sel_options = options[selected]['options']
        
            for k, v in displayed.iteritems():
                print " {0} - {1}".format(k, v)
            
            selection = raw_input("[Selection] >") 
            selection_int = 0
            try:
                #print selection
                selection_int = int(selection)
                function = sel_options[selection_int]
                if selection == 2 or selection == "2":
                    function(setup_options.getLimit() , 1)
                else:
                    function()
            except ValueError:
                print "It has to be a number"

