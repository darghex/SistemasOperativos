#!/usr/bin/python
'''
Created on 21/11/2013

@author: darghex
Servidor TCP
'''

import socket              
 
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       
port = 11111               
s.bind(('', port))

bufferSize = 1024  
               
while True:
    data, addr = s.recvfrom(bufferSize)
    if data == 'quit' :
        s.sendto('El Servidor se ha apagado', addr)
        print ''
        break
    print 'Direccion del cliente: %s , puerto: %s , trama: %s' % ( addr[0], addr[1], data) 