# --*--  coding:utf-8  --*--
# @Time : 2020/1/4 15:27
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : movie_comment.py

"""
该脚本用来爬取豆瓣书籍的 “短评” ，用MySql来存取；
需要自己添加书籍ID，可以在打开书籍页面的URL中找到，同时建议添加登录的Cookies。
"""

import urllib.parse

import requests
import re
from bs4 import BeautifulSoup
import pymysql

def response(url, headers):
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup

def parse(soup):
    divs = soup.find('div', id='comments')
    lis = divs.find_all('li')

    for li in lis:
        author = li.find('span', class_='comment-info').find('a').string
        content = li.find('span', class_='short').string
        download(author, content)

    try:
        next_link = soup.find('div', id='paginator').find('a', string=re.compile('后页 >'))['href']
        next_link = urllib.parse.urljoin(get_movie_comment_url, next_link)
        return next_link
    except:
        return "empty"

def download(author, content):

    try:
        content = content.replace('"', '')
    except:
        pass
    sql = 'insert into {} values ("{}", "{}");'.format(book_name, author, content)
    print(sql)
    cur.execute(sql)
    conn.commit()

if __name__ == '__main__':

    book_id = ''              # 添加想要爬取书的编号
    get_movie_comment_url = 'https://book.douban.com/subject/{}/comments/'.format(book_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/87.0.4280.88 Safari/537.36',
        'Accept-Encoding': 'gzip'
        # 建议添加自己登录的Cookies
    }

    soup = response(get_movie_comment_url, headers=headers)
    book_name = soup.find('div', id='content').find('h1').string[:-3]

    sign = True
    conn = pymysql.connect()  # 连接MySQL数据库
    cur = conn.cursor()
    try:
        sql = "create table {} (title varchar(20), content text)".format(book_name)
        cur.execute(sql)
        conn.commit()
    except:
        pass

    while sign:

        soup = response(get_movie_comment_url, headers)
        next_link = parse(soup)
        print(next_link)
        if next_link == 'empty':
            break

        get_movie_comment_url = next_link
