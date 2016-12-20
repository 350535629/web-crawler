#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import requests
import time
import sys
reload(sys)
print(sys.getdefaultencoding())
sys.setdefaultencoding('utf-8')

#url = 'http://www.readnovel.com/novel/341658/2.html'
#wb_data = requests.get(url)
#soup = BeautifulSoup(wb_data.text,'lxml')
#noveltext = soup.find_all(style="color: rgb(0, 0, 0); font-size: 14px;")
#for texts in noveltext:
#    print(texts)
headers = {
    "Host": "www.bxwx8.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    #Referer:http://www.readnovel.com/novel/341658.html
}

url = 'http://www.bxwx8.org/text/185/185082.html'
print(url)
        #print('test0')

wb_data = requests.get(url,headers = headers)
        #print('test1')
wb_data.encoding = 'gbk'
print(wb_data.encoding)
soup = BeautifulSoup(wb_data.text,'lxml')
print(soup)
        #print('test2')
#print(soup)
article_text = soup.select('body ')
        #print('testover')
#print(article_text)
headers["Referer"] = url
        #target.write(article_text)
wendang = 'temp-third.txt'
target = open(wendang,'w')
for texts in article_text:
    #        print (texts.text)
    target.write(texts.text)
    target.write('\n')
    target.close()
print("over")