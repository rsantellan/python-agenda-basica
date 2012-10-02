#! /usr/bin/python
#Importo la clase de expresiones regulares.

import re
from ValidatorException import EmailValidatorException
"""

Class that handles all the contact information.
I add the setters for check of valid input.

"""
class Contacto(object):
    
    def __init__(self):
        self.id = 0
        self.name = ""
        self.last_name = ""
        self.email = ""
        self.mobile = ""
        self.telephone = ""
    
    def __str__(self):
        return "%s - %s - %s - %r - %r " % (self.name, self.last_name, self.email, self.mobile, self.telephone)
        
    def set_name(self, name):
        self.name = name
    
    def set_last_name(self, last_name):
        self.last_name = last_name
    
    def set_email(self, email):
        #antes de setearlo verifico que sea un mail valido.
        if(re.match("[^@]+@[^@]+\.[^@]+", email)):
            self.email = email
        else:
            raise EmailValidatorException("Invalid email")
    
    def set_mobile(self, mobile):
        self.mobile = mobile
        
    def set_telephone(self, telephone):
        self.telephone = telephone
