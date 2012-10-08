#! /usr/bin/python
import yaml

class AgendaOptions(object):
    
    def __init__(self):
        configFile = open('options.yml')
        self.moptions = yaml.load(configFile)
        configFile.close()
        
    def getDatabaseType(self):
        return self.moptions['databases']['type']
        
    def getRunAs(self):
        return self.moptions['program']['run_as']
        
    def getSqliteDatabase(self):
        return self.moptions['databases']['sqlite3']['name']

setup_options = AgendaOptions()

