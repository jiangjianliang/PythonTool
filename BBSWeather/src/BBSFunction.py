'''
Created on 2013-3-14

@author: wander
'''

import urllib
import urllib2
import random

BBS_URL = 'http://bbs.nju.edu.cn'
FOOT_URL = '/bbsfoot'
LOGIN_URL = '/bbslogin?type=2'
PUBLISH_URL = '/bbssnd?board='
MAIL_URL = '/bbssndmail?pid=0&userid='

TAIZHOU = 'TaiZhou'

#loadFile
fileHandler = open('bbs.ini', 'r');
content = fileHandler.read();
userlist = content.split('|')
fileHandler.close();

#buildLoginPostField
values = {'id':userlist[0], 'pw':userlist[1], 'lasturl':''}
data = urllib.urlencode(values)

#buildLoginCookie
headers = {}
headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#doLogin
#fetchLoginPage
randPath = '/vd' + str(random.randint(1,5000))
login_url = BBS_URL + randPath +LOGIN_URL
login_req = urllib2.Request(login_url, data, headers)
login_res = urllib2.urlopen(login_req)
login_page = login_res.read()
print login_page.decode("gb2312")
#extractCookieFromPage
cookie_begin = login_page.find("Net.BBS.setCookie('")
cookie_end = login_page.find("')</script>")
imp = login_page[cookie_begin+len("Net.BBS.setCookie('"):cookie_end]
print "login ", imp
arr1 = imp.split('+', 2)
arr2 = arr1[0].split('N', 2)
print arr1, arr2

#buildPublishCookie
headers['Cookie'] = "_U_NUM="+ str(int(arr2[0]) + 2)+"; _U_UID="+arr2[1]+"; _U_KEY="+str(int(arr1[1]) - 2)
print headers

#buildPublishUrl
board = TAIZHOU
publish_url = BBS_URL + randPath + PUBLISH_URL + board
print publish_url

#buildPublishPostField
title = 'title-test'
content = 'content-test'
publish_value = {}
publish_value['title']= title.encode('gb2312')
publish_value['pid']=0
publish_value['reid']=0
publish_value['signature']=1
publish_value['autocr']='on'
publish_value['text']= content.encode('gb2312')
publish_data = urllib.urlencode(publish_value)

#publishArticle
publish_req = urllib2.Request(publish_url, publish_data, headers)
publish_res = urllib2.urlopen(publish_req)
print publish_res.read().decode('gb2312')