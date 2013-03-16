'''
Created on 2013-3-16

@author: wander
'''

import urllib2
import json

class Weather:
    '''
    classdocs
    '''

    WEATHER_URL = 'http://m.weather.com.cn/data/'

    def __init__(self):
        '''
        Constructor
        '''
        self.__city_code = {}
        self.__weather_json = []
        self.__weather_list = []
       
    def loadFile(self):
        fileHandler = open('weather.ini', 'r')
        content = fileHandler.read()
        self.__city_code = content.split('|')
    
    def getWeatherJson(self):
    
        for i in range(1, len(self.__city_code)+1):
            code = self.__city_code[i-1]
            url = self.WEATHER_URL + code + '.html'
            #data = 
            req = urllib2.Request(url)
            res = urllib2.urlopen(req)
            page = res.read()
            #in case the response is wrong!!!
            self.__weather_json.append(page)
        #print self.__weather_json
    
    def getWeather(self):
        for value in self.__weather_json:
            print '-------------'
            print value
            weather_dict = json.loads(value)
            print weather_dict
            #self.__weather_list.append(weather_dict['weatherinfo'])
        return self.__weather_list
    
    def getWeatherList(self):
        return self.__weather_list
    
    def toString(self):
        str = ''
        
        return str


weather = Weather()
weather.loadFile()
weather.getWeatherJson()
test = weather.getWeather()
