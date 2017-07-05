#!/bin/python2.7
#coding=utf-8
'''
刷新下所有的保险产品页面
当前刷新功能需要暂时关闭帝国后台hash验证，暂时没有解决跳过hash验证(后台来源认证码)的方案
'''
import urllib2, cookielib, urllib
ehash = '1iDC05VJEXhgSCH6ZaAs'
rhash = 'HOeGLOyvrahB'
authUrl = 'http://ecms.bx361.cn/e/admin/ecmsadmin.php'
url = 'http://ecms.bx361.cn/e/admin/ecmschtml.php?enews=ReSingleInfo&classid=9&id[]=%s&ehash_3htS=%s&rhash_GxyG=%s'
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
urllib2.install_opener(opener=opener)
data = {
    "enews"    : "login",
    "username" : "root",
    "password" : "123456",
    "loginauth": "7232275",
    "equestion": 0,
    "eanswer"  : "",
    "adminwindow" : 0,
    "imageField.x" : 0,
    "imageField.y" : 0,
    "empirecmskey1" : "",
    "empirecmskey2" : "",
    "empirecmskey3" : "",
    "empirecmskey4" : "",
    "empirecmskey5" : ""
}
postData = urllib.urlencode(data)
headers ={
    "Host":"ecms.bx361.cn",
    "Referer": "http://ecms.bx361.cn/e/admin/index.php"
}

for i in range(14884, 1, -1):
    print "----------------%s-------------------\n" % i
    newUrl = url % (i, ehash, rhash)
    req = urllib2.Request(authUrl, postData, headers=headers)
    result = opener.open(req)
    print result.read()
    result = opener.open(newUrl)
    print result.read()
