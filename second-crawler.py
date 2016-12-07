#!/usr/bin/env python
# encoding: utf-8
from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#url = 'http://www.readnovel.com/novel/341658/2.html'
#wb_data = requests.get(url)
#soup = BeautifulSoup(wb_data.text,'lxml')
#noveltext = soup.find_all(style="color: rgb(0, 0, 0); font-size: 14px;")
#for texts in noveltext:
#    print(texts)
i=1

while i<77:
    url = 'http://www.readnovel.com/novel/341658/%d.html' % i
    i+=1
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    article_text = soup.select('body > div.readcont > div.readcontcenter > div.bannerleft > div.zhangjie > p')

    target = open('temp.txt','a')
    #target.write(article_text)
    for texts in article_text:
#        print (texts.text)
        target.write(texts.text)
        target.write('\n')
    target.close()
