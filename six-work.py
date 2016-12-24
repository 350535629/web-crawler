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


def shudan_name(texts,target):
    target.write(texts)
    target.write('\n')
    return

def shudan_goal(texts,target):
    target.write(texts)
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
    target = open('./%s/test'%dirname,'w')
    i=0
    while i<25:
        shudan_name(soup.select('tr.item > td > div.pl2 > a')[i].get('title'),target)
        shudan_goal(soup.select('tr.item > td > div.star.clearfix > span.rating_nums')[i].text,target)
        shudan_sketch(soup.select('tr.item > td > p.quote > span.inq')[i].text,target)
        i+=1
    target.close()
    return



shudan_PageGet('https://book.douban.com/top250?start=0')

