#! /usr/bin/python
import yaml
configFile = open('options.yml')
configurationMap = yaml.load(configFile)
configFile.close()
print configurationMap

# {'program': {'run_as': 'memory'}}
start_file = "agenda_{0}".format(configurationMap['program']['run_as'])

exec ("import " + start_file)


