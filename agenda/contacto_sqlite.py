#! /usr/bin/python

import sqlite3
from contacto import Contacto

class ContactoSqlite(object):
    
    def __init__(self, database):
        self.db = database
    
    def insert(self, element):
        conn = None 
        lid = 0
        try:
            conn = sqlite3.connect(self.db)
            cur = conn.cursor()
            cur.execute("INSERT INTO CONTACT(name, last_name, email, mobile, telephone) VALUES (:name, :last_name, :email, :mobile, :telephone)",
                {'name' : element.name, 'last_name': element.last_name, 'email' : element.email, 'mobile' : element.mobile, 'telephone': element.telephone})
            conn.commit()
            lid = cur.lastrowid
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        return lid

    def update(self, element):
        raise NotImplementedError( "Should have implemented this" )
        
    def delete(self, elementId):
        raise NotImplementedError( "Should have implemented this" )
        
    def retrieveAllCount(self):
        sql = "SELECT count(id) FROM CONTACT"
        quantity = 0
        conn = None 
        try:
            conn = sqlite3.connect(self.db)
            cur = conn.cursor()
            cur.execute(sql)
            quantity = int (cur.fetchone()[0])
    
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()     
        return quantity
        
    def selectAll(self, limit, page):
        return_list = []
        offset = (limit * page) - limit
        sql = "SELECT id, name, last_name, email, mobile, telephone FROM CONTACT ORDER BY id LIMIT :limit OFFSET :offset"
        
        conn = None 
        try:
            conn = sqlite3.connect(self.db)
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(sql, {'limit' : limit, 'offset' : offset})
            rows = cur.fetchall()
            for row in rows:
                aux = Contacto()
                aux.id = row["id"]
                aux.name = row["name"]
                aux.last_name = row["last_name"]
                aux.email = row["email"]
                aux.mobile = row["mobile"]
                aux.telephone = row["telephone"]
                print aux
                return_list.append(aux)
        except sqlite3.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()     
        return return_list


    def findOne(self, elementId):
        raise NotImplementedError( "Should have implemented this" )    
