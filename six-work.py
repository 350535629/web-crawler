#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import re
import threading
import os
import time
import requests
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

dirname = str(time.time())
print dirname
os.mkdir('./%s'%dirname)

headers = {
#    "Host":""
#    "User-Agent":""
}


def TextWrite(texts,documentename):
    documentename.write(texts)
    target.write('\n\n')

def shudan_name(texts,target):
    target.write(texts)
    print texts
    target.write('\n')
    return

def shudan_goal(texts,target):
    target.write(texts)
    print texts
    target.write('\n')
    return

def shudan_sketch(texts,target):
    target.write(texts)
    target.write('\n')
    return

def shudan_PageGet(url):
    headers["Referer"] = url
    shudan_page = requests.get(url)
    soup = BeautifulSoup(shudan_page.text,'lxml')

    shudanBlock = soup.select('tr.item')
    target = open('./%s/test'%dirname,'a')
    i=0
    while i<25:
        shudan_name(soup.select('tr.item > td > div.pl2 > a')[i].get('title'),target)
        shudan_goal(soup.select('tr.item > td > div.star.clearfix > span.rating_nums')[i].text,target)
        shudan_sketch(soup.select('tr.item > td > p.quote > span.inq')[i].text,target)
        i+=1
    target.close()
    return

class mythread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("start thread:" + self.name)
        shudan_PageGet('https://book.douban.com/top250?start=%d'%self.counter*25)
        print("End thread" + self.name)

thread1 = mythread(1,"Crawler-1",0)
#thread2 = mythread(2,"Crawler-2",1)
#thread3 = mythread(3,"Crawler-3",2)
#thread4 = mythread(4,"Crawler-4",3)
#thread5 = mythread(5,"Crawler-5",4)

thread1.start()
#thread2.start()
#thread3.start()
#thread4.start()
#thread5.start()

thread1.join()
#thread2.join()
#thread3.join()
#thread4.join()
#thread5.join()

print("The program is over")

