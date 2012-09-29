#! /usr/bin/python

from contacto import Contacto
from ValidatorException import EmailValidatorException
from sys import exit

def create_contact():
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
    return aux

contactos = []

main_menu = {1 : 'Create new', 2: 'List', 3 : 'Exit'}

options = { 'main' : main_menu}
start_point = 'main'

selected = start_point
while True:
    displayed = options[selected]
    for k, v in displayed.iteritems():
        print " %s - %s " % (k , v)
        #print "La k:", k
        #print "La v:", v
    #print displayed;
    selection = raw_input("[Selection] >") 
    exit(1)
    
print "Contactos : ", contactos
new_contact = create_contact()
contactos.append(new_contact)
print "Contactos : ", contactos
