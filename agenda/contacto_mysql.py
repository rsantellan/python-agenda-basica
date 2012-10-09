#! /usr/bin/python

import MySQLdb
import MySQLdb.cursors

from contacto import Contacto

class ContactoMysql(object):
    
    def __init__(self, db_host, db_schema, db_user, db_pass):
        self.db_host = db_host
        self.db_schema = db_schema
        self.db_user = db_user
        self.db_pass = db_pass
    
    def insert(self, element):
        conn = None 
        lid = 0
        try:
            conn = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_schema)
            cur = conn.cursor()
            cur.execute("INSERT INTO CONTACT(name, last_name, email, mobile, telephone) VALUES (%s, %s, %s, %s, %s)",
                (element.name, element.last_name, element.email, element.mobile, element.telephone))
            conn.commit()
            lid = cur.lastrowid
        except MySQLdb.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        return lid

    def update(self, element):
        conn = None 
        try:
            conn = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_schema)
            cur = conn.cursor()
            cur.execute("UPDATE CONTACT SET name = %s, last_name = %s, email = %s, mobile = %s, telephone = %s WHERE id = %s",
                (element.name, element.last_name, element.email, element.mobile, element.telephone, element.id))
            conn.commit()
        except MySQLdb.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        
        
    def delete(self, elementId):
        sql = "DELETE FROM CONTACT WHERE id = %s"
        conn = None 
        try:
            conn = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_schema)
            cur = conn.cursor()
            cur.execute(sql, (elementId))
            conn.commit()
        except MySQLdb.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        
    def retrieveAllCount(self):
        sql = "SELECT count(id) FROM CONTACT"
        quantity = 0
        conn = None 
        try:
            conn = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_schema)
            cur = conn.cursor()
            cur.execute(sql)
            quantity = int (cur.fetchone()[0])
    
        except MySQLdb.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()     
        return quantity
        
    def selectAll(self, limit, page):
        return_list = []
        offset = (limit * page) - limit
        sql = "SELECT id, name, last_name, email, mobile, telephone FROM CONTACT ORDER BY id LIMIT %s , %s"
        conn = None 
        try:
            conn = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_schema)
            cur = conn.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(sql, (offset, limit))
            rows = cur.fetchall()
            for row in rows:
                aux = self.hidratateObject(row)
                return_list.append(aux)
        except MySQLdb.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()     
        return return_list


    def findOne(self, elementId):
        sql = "SELECT id, name, last_name, email, mobile, telephone FROM CONTACT WHERE id = %s"
        aux = None
        conn = None 
        try:
            conn = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_schema)
            cur = conn.cursor(MySQLdb.cursors.DictCursor)
            cur.execute(sql, (elementId))
            row = cur.fetchone()
            aux = self.hidratateObject(row)
        except MySQLdb.Error, e:
            print "Error %s:" % e.args[0]
        finally:
            if conn:
                conn.close()
        return aux
        
    def hidratateObject(self, row):
        aux = Contacto()
        aux.id = row["id"]
        aux.name = row["name"]
        aux.last_name = row["last_name"]
        aux.email = row["email"]
        aux.mobile = str(row["mobile"])
        aux.telephone = str(row["telephone"])
        return aux
