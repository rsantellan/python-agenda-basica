#! /usr/bin/python
from nose.tools import *
from agenda.contacto import Contacto
from agenda.ValidatorException import EmailValidatorException

def test_contacto_create():
    aux = Contacto()
    assert_equals(aux.__class__.__name__, "Contacto")
    assert_equals(aux.name, "")
    assert_equals(aux.last_name, "")
    assert_equals(aux.email, "")
    assert_equals(aux.mobile, "")
    assert_equals(aux.telephone, "")

def test_contacto_setters():
    aux = Contacto()
    aux.set_name("Juan")
    aux.set_last_name("Perez")
    aux.set_email("juan@perez.com")
    aux.set_mobile("099123123")
    aux.set_telephone("1231231")
    assert_equals(aux.name, "Juan")
    assert_equals(aux.last_name, "Perez")
    assert_equals(aux.email, "juan@perez.com")
    assert_equals(aux.mobile, "099123123")
    assert_equals(aux.telephone, "1231231")

@raises(EmailValidatorException)
""" This test validate that the raise above is launch """    
def test_contacto_setters_email_con_errores():
    aux = Contacto()
    aux.set_email("juanperez.com")


