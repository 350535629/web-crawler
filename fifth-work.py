#!/usr/bin/python
# -*- coding: UTF-8 -*-

#This file is done for merge the crawler and thread.

from bs4 import BeautifulSoup
import requests
import sys
import threading
import time
import re

reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    "Host" : "book.zongheng.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
}

#class Novelget:
#        """这是一个运用爬虫，对网上小说进行自动获取的。
#          暂时只能对纵横中文网的全本小说库进行一些爬取"""

def novel_other_chapterget(chapter_url,filename,page):
    url = chapter_url
    t = 0
    while url:
        t = t+1
        if t%30 == 0:
            time.sleep(2)
        if re.search('zongheng', url, re.I):
            headers["Referer"] = url
            wb_novel = requests.get(url, headers=headers)
            soup = BeautifulSoup(wb_novel.text, 'lxml')
            novel_text = soup.select('div#chapterContent > p')
            novel_title = soup.select('div.tc.txt > h1')
            print 'crawler is running',t,' and this is thread',page
            if  novel_title:
                filename.write(novel_title[0].text)
                filename.write('\n')
                for texts in novel_text:
                    filename.write(texts.text)
                    filename.write('\n')
                novel_next = soup.select('a#nextChapterButton')
                url = novel_next[0].get('href')
            else:
                return
        else:
            return
    return

def novelget(str_url,page):
    url = str_url.get('href')
    title = str_url.get('title')
    if  re.search('zongheng',url,re.I):#正则匹配，如果是纵横中文网的小说，则开始获取
        print 'OK'
        headers["Referer"] = url
        wb_novel = requests.get(url, headers=headers)
        soup = BeautifulSoup(wb_novel.text,'lxml')#开始解析
        novel_text = soup.select('div.book_btn > a#readRecord')#对解析后的网页开始删选，获取开始阅读的界面
        for novelurl in novel_text:
            url = novelurl.get('href')
            headers["Referer"] = url
            wb_novel = requests.get(url, headers=headers)
            soup = BeautifulSoup(wb_novel.text, 'lxml')
            novel_title = soup.select('div.tc.txt > h1')#对小说名进行获取
            if novel_title[0]:#如果小说存在
                chinesetitle = title.encode(encoding='gbk ',errors='strict')#将获取的小说名转码变为GBK中文码
                wendang = './forth-novel/{0}/{1}.txt'.format(page, chinesetitle)
                target = open(wendang,'a')#打开用来存取小说的文档
                target.write(novel_title[0].text)#将小说名字存入
                target.write('\n')
                novel_other_chapterget(url,target,page)#调用函数，对小说其他章节进行爬取
                target.close()
            return
    else:
        print 'error'
    return

def crawler(k):
    page = k
    if page:
        print page
        url = 'http://book.zongheng.com/quanben/c0/c0/b0/u1/p%d/v0/s1/t0/ALL.html' % page
        headers["Referer"] = url
        wb_ku = requests.get(url,headers = headers)
        soup = BeautifulSoup(wb_ku.text,'lxml')
        article_text = soup.select('ul.main_con > li > span.chap > a.fs14')

        for texts in article_text:
            print texts.get('title')
            print texts.get('href')
            novelget(texts,page)

        page+=1
        time.sleep(3)
    print("over")
    return

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        crawler(self.counter)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if 0:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

thread1 = myThread(1, "Crawler-1", 1)
thread2 = myThread(2, "Crawler-2", 2)
thread3 = myThread(3, "Crawler-3", 3)
thread4 = myThread(4, "Crawler-4", 4)
thread5 = myThread(5, "Crawler-5", 5)
# 开启新线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
print ("退出主线程")