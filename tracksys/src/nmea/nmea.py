'''
Created on 19/07/2011

@author: darghex
'''


from twisted.protocols import gps

class NMEA(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        gps
        
    def check_nmea0183(self,s):
        if s[0] != '$':
            return False
        if s[-3] != '*':
            return False
        checksum = 0
        for c in s[1:-3]:
            checksum ^= ord(c)
        if int(s[-2:],16) != checksum:
            return False
        return True
    
        