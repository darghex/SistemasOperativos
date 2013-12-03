#!/usr/bin/python
'''
Created on 19/07/2011

@author: darghex
'''
import app.server
from nmea.nmea0183 import NMEA0183
from nmea.gprmc import GPRMC


if __name__ == '__main__':
    srv = app.server.Server()
    srv.open()
    sentence = NMEA0183()

    while True:
        data,addr = srv.sock.recvfrom(srv.size)
   
        if sentence.check_nmea0183(data):
            line = sentence.getGPRMC()
       
            if not line is None:
                trama = GPRMC(line) 
                if trama.getStatus() == 'V': continue;               
                print "Fecha : ",trama.getDate() , "Hora : ",trama.getHour()
                print "Latitud : ",trama.getLatitude() , "longitud : ",trama.getLongitude(), "velocidad : ",trama.getSpeed()                            
            
    srv.close()