# coding:utf-8

#爬虫第一关
from bs4 import BeautifulSoup
import urllib2
import re
import urlparse

class Spider(object):
    def __init__(self):
        self.root_url='http://www.heibanke.com/lesson/crawler_ex00/'
    def run(self,root_url):
        web=urllib2.Request(root_url)
        content=urllib2.urlopen(web)
        soup=BeautifulSoup(content,'html.parser',from_encoding='utf-8')
        target=soup.find('h3').get_text()
        number=re.search(r'\d+',target).group()
        new_url=self.root_url+number
        return self.output(target,new_url,number)
    def output(self,tar,url,num):
        f=file('spider.txt','a+')
        f.write(tar.encode('utf-8'))
        f.write('\n')   
        f.close()
        #print tar.encode('utf-8')
        if num !=None:
            self.run(url)
        

if __name__=='__main__':
    root_url='http://www.heibanke.com/lesson/crawler_ex00/'#爬虫入口
    spiderman=Spider()
    spiderman.run(root_url)
