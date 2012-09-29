#! /usr/bin/python
class EmailValidatorException(Exception):
    """ 
    The model from the same came from:
    http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
    """
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)
        # Now for your custom code...
        # self.Errors = Errors
