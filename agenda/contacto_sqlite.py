#! /usr/bin/python

import sqlite3
import yaml

class ContactoSqlite(BasicDb):
    
    def __init__(self):
        configFile = open('options.yml')
        configurationMap = yaml.load(configFile)
        configFile.close()
        self.db = configurationMap['databases']['sqlite']['name'];
    
    def insert(self, element):
        conn = sqlite3.connect(self.db)
        lid = 0
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO CONTACT(name, last_name, email, mobile, telephone) VALUES (:name, :last_name, :email, :mobile, :telephone)",
                {':name' : element.name, 'last_name': element.last_name, 'email' : element.email, 'mobile' : element.mobile, 'telephone': element.telephone})
            conn.commit()
            lid = cur.lastrowid
        return lid

    def update(self, element):
        raise NotImplementedError( "Should have implemented this" )
        
    def delete(self, elementId):
        raise NotImplementedError( "Should have implemented this" )
        
    def selectAll(self):
        raise NotImplementedError( "Should have implemented this" )

    def findOne(self, elementId):
        raise NotImplementedError( "Should have implemented this" )    
