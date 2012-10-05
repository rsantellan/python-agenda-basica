#! /usr/bin/python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : "Contacts project",
    'author' : "Rodrigo Santellan",
    'url' : "https://github.com/rsantellan/python-agenda-basica",
    'download_url' : 'https://github.com/rsantellan/python-agenda-basica',
    'author_email' : 'rsantellan@gmail.com',
    'version' : '0.0.1',
    'install_requieres' : ['nose', 'yaml', 'sqlite3'],
    'packages' : ['agenda'],
    'scripts' : [],
    'name' : 'My simple contacts'
}

setup(**config)
