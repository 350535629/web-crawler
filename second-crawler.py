#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup
import requests
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

#url = 'http://www.readnovel.com/novel/341658/2.html'
#wb_data = requests.get(url)
#soup = BeautifulSoup(wb_data.text,'lxml')
#noveltext = soup.find_all(style="color: rgb(0, 0, 0); font-size: 14px;")
#for texts in noveltext:
#    print(texts)
headers = {
    "Host": "hm.baidu.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    #Referer:http://www.readnovel.com/novel/341658.html
}
k=1
while k < 200:
    i = k*1000;
    while i<k*1001:
        print k
        url = 'http://www.bxwx8.org/text/{0}/{1}.html'.format(k,i)
        i+=1
        print(url)
        #print('test0')
        wb_data = requests.get(url,headers = headers)
        #print('test1')
        soup = BeautifulSoup(wb_data.text,'lxml')
        #print('test2')
        article_text = soup.select('body > div:nth-child(12)')
        #print('testover')
        if len(article_text) == 0:
            break
        print("yeah")
        headers["Referer"] = url
        #target.write(article_text)
        wendang = 'temp%d.txt' % i
        target = open(wendang,'w')
        for texts in article_text:
    #        print (texts.text)
            target.write(texts.text)
            target.write('\n')
        target.close()
        if i%10 == 0:
            time.sleep(3)
    k+=1
    if k%5 == 0:
        time.sleep(3)
print("over")