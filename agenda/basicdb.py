#! /usr/bin/python

class BasicDb(object):
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
