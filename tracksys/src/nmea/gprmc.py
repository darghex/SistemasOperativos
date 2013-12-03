'''
Created on 19/07/2011

@author: darghex
'''
import time
class GPRMC(object):
    '''
    CLASE NMEA FORMATO GPRMC 
    Minimo de Datos GPS/TRANSIT Especificos Recomendados.

    '''
    
    def __init__(self, sentence):
 
          
        self.__explodeData(sentence)
        if self.getStatus() == 'A':
            self.__process()
  


    def __explodeData(self, sentence):
        (self.__format, # Cabecera Protocolo RMC
         self.__hour, # Hora UTC en formato hh:mm:ss 
         self.__status, # Estado de los datos ( A: Valido, V: No Valido)
         self.__latitude, # latitud actual en formato de ggmm.mm
         self.__northsouth, #hemisferio de latitud N o S
         self.__longitude, # Longitud actual en formato de ggmm.mm
         self.__eastwest, # hemisferio de longitud E o W
         self.__speed, # Velocidad en Nudos
         self.__course_true, # Curso verdadero en grados
         self.__date, # Fecha en formato ddmmaa 
         self.__var_magnetic, # variacion magnetica en grados
         self.__dm_eastwest, checksum) = sentence.split(",") 


    def __process(self):
   
        latitude_in=float(self.__latitude)
        longitude_in=float(self.__longitude)
        if self.__northsouth == 'S':
            latitude_in = -latitude_in
        if self.__eastwest == 'W':
            longitude_in = -longitude_in

        latitude_degrees = int(latitude_in/100)
        latitude_minutes = latitude_in - latitude_degrees*100
        
        longitude_degrees = int(longitude_in/100)
        longitude_minutes = longitude_in - longitude_degrees*100
        
        self.__latitude = latitude_degrees + (latitude_minutes/60)
        self.__longitude = longitude_degrees + (longitude_minutes/60)
        
        self.__speed = float(self.__speed) * 1.852;
        self.__hour = time.strftime("%H:%M:%S", time.strptime(self.__hour.split(".")[0],"%H%M%S"))
        self.__date = time.strftime("%Y-%m-%d", time.strptime(self.__date.split(".")[0],"%d%m%y"))
    
        
        
    def getLatitude(self):
        return self.__latitude;
    
    def getLongitude(self):
        return self.__longitude;
    
    def getSpeed(self):
        return self.__speed;
    
    def getHour(self):
        return self.__hour;
    
    def getDate(self):
        return self.__date;
    
    def getCourseTrue(self):
        return self.__course_true;
    
    def getStatus(self):
        return self.__status;        