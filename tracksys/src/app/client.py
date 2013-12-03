'''
Created on 19/07/2011

@author: darghex
'''
from sock import Sock
import app, sys

class Client( Sock, object):
    '''
    Clase para el servidor de tramas
    '''

    def __init__(self):
        self.getConfig()
         
    
    
        
    def readFile(self, file):
        from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
        import time
        if ( self.protocol == 'UDP'):
            sock = socket(AF_INET,SOCK_DGRAM)
        elif ( self.protocol == 'TCP'):
            sock = socket(AF_INET,SOCK_STREAM)
        else:
            sys.exit()
        
        f = open(file)
        print "enviando tramas"
        while True: 
            trama =  f.readline()
            sys.exc_clear()
            time.sleep(0.05)
            
            if not trama: break;
            sock.sendto(trama,(self.host, self.port))           
            
        sock.close()            
        f.close()
        print "teminado."
        