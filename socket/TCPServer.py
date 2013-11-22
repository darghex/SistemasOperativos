#!/usr/bin/python
'''
Created on 21/11/2013

@author: darghex
Servidor TCP
'''

import socket              
 
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )       
port = 11111               
s.bind( ('', port) )
print "abriendo servidor en puerto %s" % port

delay = 1
s.listen( delay )

bufferSize = 1024  
               
while True:
    c, addr = s.accept()
    data = c.recv(bufferSize)
    if data == 'quit' :
        c.send('El Servidor se ha apagado')
        print ''
        break
    print 'Direccion del cliente: %s , puerto: %s , trama: %s' % ( addr[0], addr[1], data)  
    c.close()
