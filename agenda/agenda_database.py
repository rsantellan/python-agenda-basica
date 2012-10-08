#! /usr/bin/python

from contacto import Contacto
from ValidatorException import EmailValidatorException
from sys import exit
from basicdb import BasicDb

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
        
        
        

    def edit_contact(self, aux):
        print "========== Edit a contact ================"
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
        salida = []
        for contact in self.contactos:
            if contact.id == aux.id:
                salida.append(aux)
            else:
                salida.append(contact)
        self.contactos = salida

    def list_contacts(self, limit, page):
        print "========== List all contact ================"
        quantity_contactos = self.db.retrieveDb().retrieveAllCount();
        #print quantity_contactos
        contactos = self.db.retrieveDb().selectAll(limit, page);
        number = 1
        while number != 0:
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
                    number = int(option)
                    element = None
                    for contact in contactos:
                        if contact.id == number:
                            element = contact
                    if number != 0:
                        if element == None:
                            print "Ups there has been an error...."
                        else:
                            self.edit_contact(element)
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
                    function(1 , 2)
                else:
                    function()
            except ValueError:
                print "It has to be a number"

