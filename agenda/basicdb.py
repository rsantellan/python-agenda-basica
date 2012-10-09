#! /usr/bin/python

from contacto_sqlite import ContactoSqlite
from contacto_mysql import ContactoMysql
from options import setup_options

class BasicDb(object):
    
    def __init__(self):
        if setup_options.getDatabaseType() == "sqlite":
            self.db = ContactoSqlite(setup_options.getSqliteDatabase())
        elif setup_options.getDatabaseType() == "mysql":
            self.db = ContactoMysql(setup_options.getMysqlHost(),  setup_options.getMysqlSchema(), setup_options.getMysqlUser(), setup_options.getMysqlPass())
        else:
            raise "You must define a database"
        

    def retrieveDb(self):
        return self.db
        
    """ 
    This will be a abstract class implementing the basics of db
    """
    def insert(self, element):
        raise NotImplementedError( "Should have implemented this" )

    def update(self, element):
        raise NotImplementedError( "Should have implemented this" )
        
    def delete(self, elementId):
        raise NotImplementedError( "Should have implemented this" )
        
    def selectAll(self):
        raise NotImplementedError( "Should have implemented this" )

    def findOne(self, elementId):
        raise NotImplementedError( "Should have implemented this" )
