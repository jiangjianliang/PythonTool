'''
Created on 2013-3-14

@author: wander
'''
import urllib
import urllib2
import random

class BBS(object):
    '''
    bbs main
    '''
    BBS_URL = "http://bbs.nju.edu.cn"
    FOOT_URL = "/bbsfoot"
    LOGIN_URL = "/bbslogin?type=2"
    PUBLISH_URL = "/bbssnd?board="
    MAIL_URL = "/bbssndmail?pid=0&userid="
    
    TAIZHOU = "TaiZhou";

    def __init__(self):
        '''
        Constructor
        '''
        self.__userlist={}
        self.__headers = {}
        self.__headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.__randPath = '/vd' + str(random.randint(1,5000))
        self.login_data=''
    
    def loadFile(self):
        fileHandler = open('bbs.ini', 'r')
        content = fileHandler.read()
        self.__userlist = content.split('|')
        fileHandler.close()
    
    def doLogin(self):
        values = {'id':self.__userlist[0], 'pw':self.__userlist[1], 'lasturl':''}
        self.login_data = urllib.urlencode(values)
        login_page = self.fetchLoginPage()
        
        self.extractCookieFromPage(login_page)
    
    def fetchLoginPage(self):
        login_url = BBS.BBS_URL + self.__randPath +BBS.LOGIN_URL
        
        login_req = urllib2.Request(login_url, self.login_data, self.__headers)
        login_res = urllib2.urlopen(login_req)
        login_page = login_res.read()
        print login_page.decode("gb2312")
        return login_page
    
    #extract Cookies from login page
    def extractCookieFromPage(self, login_page):
        cookie_begin = login_page.find("Net.BBS.setCookie('")
        cookie_end = login_page.find("')</script>")
        imp = login_page[cookie_begin+len("Net.BBS.setCookie('"):cookie_end]
        print "login ", imp
        arr1 = imp.split('+', 2)
        arr2 = arr1[0].split('N', 2)
        print arr1, arr2
        self.__headers['Cookie'] = "_U_NUM="+ str(int(arr2[0]) + 2)+"; _U_UID="+arr2[1]+"; _U_KEY="+str(int(arr1[1]) - 2)
    
    #publish articles with previous cookies
    def publishArticle(self, board, title, content):
        publish_url = BBS.BBS_URL + self.__randPath + BBS.PUBLISH_URL + board
        
        publish_value = {}
        publish_value['title']= title.encode('gb2312')
        publish_value['pid']=0
        publish_value['reid']=0
        publish_value['signature']=1
        publish_value['autocr']='on'
        publish_value['text']= content.encode('gb2312')
        publish_data = urllib.urlencode(publish_value)
        
        publish_req = urllib2.Request(publish_url, publish_data, self.__headers)
        publish_res = urllib2.urlopen(publish_req)
        print publish_res.read().decode('gb2312')
    
    #send mail to receiver
    def sendMail(self, receiver, title, content):
        mail_url = BBS.BBS_URL + self.__randPath + BBS.MAIL_URL
        
        mail_value = {}
        mail_value['title'] = title.encode('gb2312')
        mail_value['userid'] = receiver
        mail_value['signature'] = 1
        mail_value['text'] = content.encode('gb2312')
        mail_data = urllib.urlencode(mail_value)
        
        mail_req = urllib2.Request(mail_url, mail_data, self.__headers)
        mail_res = urllib2.urlopen(mail_req)
        print mail_res.read().decode('gb2312')
        
