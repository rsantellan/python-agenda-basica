#! /usr/bin/python

from contacto import Contacto
from ValidatorException import EmailValidatorException
from sys import exit

def create_contact(contactos):
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
    aux.id = len(contactos) + 1
    contactos.append(aux)
    return contactos
    #return aux

def edit_contact(contactos, aux):
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
    for contact in contactos:
        if contact.id == aux.id:
            salida.append(aux)
        else:
            salida.append(contact)
    return salida
    #contactos.append(aux)
    #return contactos
    #return aux

def list_contacts(contactos):
    print "========== List all contact ================"
    number = 1
    while number != 0:
        for contact in contactos:
            print "{0}: {1}".format(contact.id, contact)
        option = raw_input("Select the number to edit or 0 to come back\n")
        try:
            number = int(option)
            element = None
            #print number
            #print element
            for contact in contactos:
                #print contact.id
                if contact.id == number:
                    #print "estoy aca??"
                    element = contact
            #print element
            if number != 0:
                if element == None:
                    print "Ups there has been an error...."
                else:
                    contactos = edit_contact(contactos, element)
                
            #function = sel_options[selection_int] 
            #contactos = function(contactos)
        except ValueError:
            print "It has to be a number"
    
    return contactos

def close_program(contactos):
    print "Thank you for using contact 1.0.0"
    exit(0)

def init_agenda():
    contactos = []
    pepe = Contacto()
    pepe.set_name('pepe')
    pepe.set_last_name('perez')
    pepe.set_email('pepe@perez.com')
    pepe.set_mobile('312312')
    pepe.set_telephone('132312312')
    pepe.id = len(contactos) + 1
    contactos.append(pepe)

    main_menu_text = {1 : 'Create new', 2: 'List', 3 : 'Exit'}
    main_menu_options = {1 : create_contact, 2: list_contacts, 3 : close_program}

    options = { 'main' : { 'text' : main_menu_text, 'options' : main_menu_options}}
    start_point = 'main'

    selected = start_point
    print "========== Welcome to contact 1.0.0 ================"

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
            contactos = function(contactos)
        except ValueError:
            print "It has to be a number"

    
#print "Contactos : ", contactos
init_agenda()
