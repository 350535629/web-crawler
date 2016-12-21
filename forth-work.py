
# encoding: utf-8

#This file is aimed to find some finished novel in www.zongheng.com

from bs4 import BeautifulSoup
import requests
import sys
import time
import re
reload(sys)
sys.setdefaultencoding('utf-8')

headers = {
    "Host": "book.zongheng.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    #Referer:http://www.readnovel.com/novel/341658.html
}

def novelget(str_url,page):
    url = str_url.get('href')
    title = str_url.get('title')
    if  re.search('zongheng',url,re.I):
        print 'OK'
        headers["Referer"] = url
        wb_novel = requests.get(url, headers=headers)
        soup = BeautifulSoup(wb_novel.text,'lxml')
        novel_text = soup.select('div.book_btn > a#readRecord')
        for novelurl in novel_text:
            url = novelurl.get('href')
            headers["Referer"] = url
            wb_novel = requests.get(url, headers=headers)
            soup = BeautifulSoup(wb_novel.text, 'lxml')
            novel_title = soup.select('div.tc.txt > h1')
            if novel_title[0]:
                novel_text =  soup.select('div#chapterContent > p')
                wendang = './forth-text/{0}/{1}.txt'.format(page, title)
                target = open(wendang,'a')
                target.write(novel_title[0].text)
                target.write('\n')
                for texts in novel_text:
                    target.write(texts.text)
                    target.write('\n')
                target.close()
            return
    else:
        print 'error'
    return

page = 1
while page < 2:
    print page
    url = 'http://book.zongheng.com/quanben/c0/c0/b9/u0/p%d/v9/s1/t0/ALL.html' % page
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
