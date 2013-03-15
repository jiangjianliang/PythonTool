'''
Created on 2013-3-14

@author: wander
'''

class MyClass(object):
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
    def buildHttpHeader(self):
        header ={"Cache-Control":"max-age=0", "Connection":"keep-alive",
                 "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                 "Accept-Language":"zh-CN,zh;q=0.8", "Accept-Charset":"GBK,utf-8;q=0.7,*;q=0.3"}
        return header
    
    def login(self):
        getFootKey(self)
        loadFile(self)
        doLogin(self)
    
    def getFootKey(self):
        
