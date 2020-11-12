# --*--  coding:utf-8  --*--
# @Time : 2020/11/11 14:24
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : novels.py

'''
爬取笔趣阁上所有的完结书籍
'''

import requests
from bs4 import BeautifulSoup

def get_content(bookname, cheapter_link):
    resp = requests.get(cheapter_link)
    soup = BeautifulSoup(resp.text, 'lxml')
    cheapter_name = soup.find('div', class_="bookname").find('h1').get_text()
    content = soup.find('div', id='content')
    with open('D:/笔趣阁/'+bookname+'.txt', 'a', encoding='utf-8') as pf:
        pf.write("\t\t\t" + cheapter_name + '\n\n')
        pf.write('\n\n'.join(content.get_text().split()))
        pf.write('\n\n\n')

url = 'https://www.biquge.com.cn/quanben/'
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')
title = soup.find('div', class_='novelslist2')
lis = title.find_all('li')
book_info = {}
books = []
for li in lis[14:]:
    title = li.find('span', class_='s2').get_text()
    cat = li.find('span', class_='s1').find('a').get_text()
    link = 'https://www.biquge.com.cn' + li.find('span', class_='s2').find('a')['href']
    book_info['title'] = cat + '--' + title
    book_info['link'] = link

    books.append(book_info)
    book_info = {}

for book in books[1:]:
    bookname = book['title']
    booklink = book['link']
    resp = requests.get(booklink)
    soup = BeautifulSoup(resp.text, 'lxml')
    dds = soup.find('div', id='list')
    dd = dds.find_all('dd')
    for i in dd:
        title = i.get_text()
        link = 'https://www.biquge.com.cn' + i.find('a')['href']
        get_content(bookname, link)
        print(title, link)
