#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup
import requests
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    "Host": "www.readnovel.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    #Referer:http://www.readnovel.com/novel/341658.html
}
k = 342531
while k < 342800:
    i = 1
    while i :
        print k
        url = 'http://www.readnovel.com/novel/{0}/{1}.html'.format(k,i)
        i+=1
        print(url)
        #print('test0')
        wb_data = requests.get(url,headers = headers)
        #print('test1')
        soup = BeautifulSoup(wb_data.text,'lxml')
        #print('test2')
        article_text = soup.select('body > div.readcont > div.readcontcenter > div.bannerleft > div.zhangjie > p')
        #print('testover')
        if len(article_text) == 0:
            break
        print("yeah")
        headers["Referer"] = url
        #target.write(article_text)
        wendang = './text/%d.txt' % k
        target = open(wendang,'a')
        for texts in article_text:
    #        print (texts.text)
            target.write(texts.text)
            target.write('\n')
        target.close()
        if i - 10 == 0:
            time.sleep(1)
        if i % 50 == 0:
            time.sleep(1)
    k+=1
    if k%5 == 0:
        time.sleep(1)
print("over")