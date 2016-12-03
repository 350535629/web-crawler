#!/usr/bin/env python
# encoding: utf-8

from bs4 import BeautifulSoup
import requests

url = 'https://www.qidian.com'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
title = soup.select('div.book-list-wrap:nth-child(1) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > strong:nth-child(2) > a:nth-child(1)')
print(title)
