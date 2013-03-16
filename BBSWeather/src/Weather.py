'''
Created on 2013-3-16

@author: wander
'''

import urllib2
import json
from datetime import *

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
            print type(weather_dict)
            print weather_dict['weatherinfo']
            self.__weather_list.append(weather_dict['weatherinfo'])
        #return self.__weather_list
    
    def getWeatherList(self):
        return self.__weather_list
    
    def toString(self):
        des_str = ''
        date_list = []
        date_list.append(date.today())
        
        for j in range(1, 6):
            prev_date = date_list[j-1]
            new_date = prev_date + timedelta(days=1)
            date_list.append(new_date)
        
        for info in self.__weather_list:
            des_str += '['+info['city']+']'+info['date_y']+'\r\n'
            des_str += '======================================================\r\n'
            for i in range(1,7):
                des_str += '======================================================\r\n'
                des_str += '------------------------------------------------------\r\n'
                info_key = 'temp' + str(i)
                temp_list = info[info_key].split('~')
                des_str += str(date_list[i-1]) + '\tDay\t' + info['img_title'+str(2*i-1)]+ '\t' +temp_list[0]+'\t'+ info['wind'+str(i)]+'\r\n'
                des_str += '        Night\t' + info['img_title'+str(2*i)]+ '\t' +temp_list[1]+'\t'+'\r\n'
            
            des_str += '======================================================\r\n'
            des_str += '\r\n\r\n'
        
        return des_str


weather = Weather()
weather.loadFile()
weather.getWeatherJson()
test = weather.getWeather()
print weather.toString()