'''
Created on 19/07/2011

@author: darghex
'''
from sock import Sock
class Server( Sock, object):
    sock = None
    '''
    Clase para el servidor de tramas
    '''

    def __init__(self):
        self.getConfig() 
        
    '''
        Abre el socket para dar comienzo a la comunicacion
    '''
    def open(self):
        self.sock = self.getProtocol()
        print "abriendo puerto ", self.port
               
               
    def close(self):
        self.sock.close()     
    
        
    def __logger(self):
        while True:
            data,addr = self.sock.recvfrom(self.size)
            print 'Recibiendo de host : ', addr[0]
            print "Trama: ", data
