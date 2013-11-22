#!/usr/bin/python
'''
Created on 21/11/2013

@author: darghex
'''
import sys
import socket              
     
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
port = 11111 
bufferSize = 1024         
ip_server = '127.0.0.1'
s.connect((ip_server, port))
data = raw_input("Ingrese el mensaje a enviar > ")
s.send( data )
print s.recv(bufferSize)
s.close()    