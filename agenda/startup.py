#! /usr/bin/python

from options import AgendaOptions
from options import setup_options
from agenda_memory import AgendaMemory
from agenda_database import AgendaDatabase
import agenda_gtk


#print setup_options.moptions

if setup_options.getRunAs() == "memory":
    agendaMemory = AgendaMemory()
    agendaMemory.init_agenda()
elif setup_options.getRunAs() == "database":
    agendaDatabase = AgendaDatabase()
    agendaDatabase.init_agenda()
elif setup_options.getRunAs() == "gtk":
    print "Using gtk "    
else:
    print "There is none run as option available"

