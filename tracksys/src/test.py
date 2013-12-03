#!/usr/bin/python
'''
Created on 19/07/2011

@author: darghex
'''
import app.client
FILE="examples/nmea.log"

if __name__ == '__main__':
    app.client.Client().readFile(FILE)
