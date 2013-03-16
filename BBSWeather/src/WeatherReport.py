'''
Created on 2013-3-16

@author: wander
'''
bbs = BBS()
bbs.loadFile()
bbs.doLogin()

weather = Weather()
weather.loadFile()
weather.getWeatherJson()
test = weather.getWeather()
print weather.toString()
bbs.sendMail('jjlssm', 'hello', test)
#bbs.publishArticle(BBS.TAIZHOU, 'test', 'content-test')