# --*--  coding:utf-8  --*--
# @Time : 2020/12/8 14:52
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : zhihu_question.py

"""
使用selenium 爬取动态知乎问题答案
爬取的结果通过 MySql存取
"""

from selenium import webdriver
import time
from lxml import etree
import pymysql

conn = pymysql.connect('localhost', 'root', 'root', 'zhuhu_question')  # 连接数据库
cursor = conn.cursor()  # 获取游标
driver = webdriver.Chrome()

driver.get('https://www.zhihu.com/question/318487461')  # 问题网页
driver.find_element_by_xpath("//button[@class='Button Modal-closeButton Button--plain']").click()
try:
    driver.find_element_by_xpath("//a[@class='QuestionMainAction ViewAll-QuestionMainAction']").click()
except:
    pass

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

for i in range(0, 200000, 1500):
    """
    控制爬取的内容的多少，如果回答数比较少，可以把总数（200000）变小一点
    """
    driver.execute_script('window.scrollBy(0, {})'.format(i))
    time.sleep(2)

html = etree.HTML(driver.page_source)
contents = html.xpath('//div[@class="List-item"]')
title = html.xpath('//div[@class="QuestionHeader-main"]/h1/text()')[0]

driver.quit()

sql = "create table {}(作者 varchar(50), 内容 text)".format(title)
cursor.execute(sql)
conn.commit()

for i in contents:
    try:
        author_name = i.xpath('.//a[@class="UserLink-link"]/text()')[0]
    except:
        author_name = i.xpath('.//span[@class="UserLink AuthorInfo-name"]/text()')[0]
    content = i.xpath('.//span[@itemprop="text"]//text()')
    content = '\n'.join(content)

    sql = "INSERT INTO {} values('{}','{}')".format(title, author_name, content)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        continue

    print("作者："+author_name+':')

cursor.close()
conn.close()  # 关闭数据库连接
