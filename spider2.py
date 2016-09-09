# coding:utf-8

#爬虫第二关
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import urlparse

class Spider_two(object):
    def __init__(self):
        self.parser=Parse()

    def run(self,url):
        x=0
        while x<31: 
            data={'username':1,'password':x}
            url_data=urllib.urlencode(data)
            request=urllib2.Request(url,url_data)
            content=urllib2.urlopen(request)
            text=content.read()
            self.parser.open(text,x)
            x+=1
class Parse(object):
    def open(self,text,x):
        soup=BeautifulSoup(text,'html.parser',from_encoding='utf-8')
        txt=soup.find('h3').get_text().encode('utf-8')
        p=open('spider.txt','r')
        content=p.read()
        p.close()
        if txt not in content:
            f=open('spider.txt','a+')
            f.write(txt)
            f.write(str(x))
            f.write('\n')
            f.close()


if __name__=='__main__':
    url='http://www.heibanke.com/lesson/crawler_ex01/'
    spider=Spider_two()
    spider.run(url)
