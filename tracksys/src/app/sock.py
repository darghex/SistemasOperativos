'''
Created on Jul 20, 2011

@author: darghex
'''

import sys, app
from socket import socket,AF_INET,SOCK_DGRAM
from socket import socket,AF_INET,SOCK_STREAM

class Sock(object):
    protocol = 'UDP'
    host = '127.0.0.1'
    port = 11019
    size = 1024
    
    def getConfig(self):
        import ConfigParser   
        cfg = ConfigParser.ConfigParser()
        if not cfg.read(app.FILE_CONF):
            print "El archivo de configuracion se pudo leer."
            print "Verifique que exista ",app.FILE_CONF
            sys.exit()  
        self.__read(cfg)
    
    
    def __read(self, cfg):        
        
        if cfg.has_option("SERVER", "host"):
            self.host = str( cfg.get("SERVER", "host") )
                      
        if cfg.has_option("SERVER", "port"):
            self.port = int( cfg.get("SERVER", "port" ) )
                   
        if cfg.has_option("SERVER", "protocol"):
            self.protocol = str( cfg.get("SERVER", "protocol" ) )
            
            if str(cfg.get("SERVER", "protocol") ) == 'TCP':
                self.size = int( cfg.get("TCP", "buffer"))
            elif str(cfg.get("SERVER", "protocol") ) == 'UDP':
                self.size = int( cfg.get("UDP", "datagram"))
        
        
          
        if cfg.has_option("LOG", "display"):
            self.log = bool( cfg.get("LOG", "display" ) )
     
    def __openUDPProcotol(self):  
                  
        UDPSock =    socket(AF_INET,SOCK_DGRAM)        
        UDPSock.bind((self.host, self.port))
        return UDPSock
            
    def __openTCPProcotol(self):        
        TCPSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPSock.bind((self.host,self.port))
        return TCPSock
    
    def getProtocol(self):
        if self.protocol == "UDP":
            return self.__openUDPProcotol()
        elif self.protocol == "TCP":
            return self.__openTCPProcotol()
        else:
            print "Protocolo no valido . verifique ", app.FILE_CONF
            sys.exit()  