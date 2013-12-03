'''
Created on 19/07/2011

@author: darghex
'''


class GPGGA(object):
    '''
    Clase que parsea una trama NMEA formato GGA
    '''
    
    def __init__(self, sentence):
        import logging
        
        logging.debug("GGAParser iniciado")
        logging.debug("Trying a persear: "+sentence)
        self.__explodeData(sentence)
        self.__process()
        logging.debug("GGAParser finished")



    def __explodeData(self, sentence):
        (self.__format,
         self.__utc,
         self.__latitude, 
         self.__northsouth, 
         self.__longitude, 
         self.__eastwest, 
         self.__quality, 
         self.__number_of_satellites_in_use, 
         self.__horizontal_dilution, 
         self.__altitude, 
         self.__above_sea_unit, 
         self.__geoidal_separation, 
         self.__geoidal_separation_unit, 
         self.__data_age, 
         self.__sdiff_ref_stationID) = sentence.split(",")


    def __process(self):
        import time
        latitude_in=float(self.__latitude)
        longitude_in=float(self.__longitude)
        if self.northsouth == 'S':
            latitude_in = -latitude_in
        if self.eastwest == 'W':
            longitude_in = -longitude_in

        latitude_degrees = int(latitude_in/100)
        latitude_minutes = latitude_in - latitude_degrees*100
        
        longitude_degrees = int(longitude_in/100)
        longitude_minutes = longitude_in - longitude_degrees*100
        
        self.__latitude = latitude_degrees + (latitude_minutes/60)
        self.__longitude = longitude_degrees + (longitude_minutes/60)
        
        self.__timeOfFix = time.strftime("%H:%M:%S", time.strptime(self.__utc.split(".")[0],"%H%M%S"))
        self.__altitude = float(self.__altitude)
        
        
    def getLatitude(self):
        return self.__latitude;
    
    def getLongitude(self):
        return self.__longitude;
    
    def getAltitude(self):
        return self.__latitude;