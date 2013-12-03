'''
Created on 19/07/2011

@author: darghex
'''

class NMEA0183(object):
    '''
    classdocs
    '''
    sentence = ''


              
    def check_nmea0183(self,s):
        try:
            s = str(s).strip()
            if s[0] != '$':
                return False
            if s[-3] != '*':           
                return False
            checksum = 0
            for c in s[1:-3]:
                checksum ^= ord(c)
            if int(s[-2:],16) != checksum:
                return False
            self.sentence = s
            return True
        except:
            return False
        
    def getGPRMC(self):
        if self.sentence[1:str(self.sentence).index(',')] == 'GPRMC':
            return self.sentence
        return None
            