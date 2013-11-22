#!/usr/bin/python
'''
Created on 21/11/2013

@author: darghex
'''
import sys
import socket              
 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    
 
port = 11111 
bufferSize = 1024         
data = raw_input("Ingrese el mensaje > ")
ip = '127.0.0.1'
s.sendto( data, (ip, port) )