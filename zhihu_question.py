# --*--  coding:utf-8  --*--
# @Time : 2020/12/8 14:52
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : zhihu_question.py

from selenium import webdriver
import time
from lxml import etree
import pymysql
import os

conn = pymysql.connect('localhost', 'root', 'root', 'zhuhu_question')  # 连接数据库
cursor = conn.cursor()  # 获取游标
driver = webdriver.Chrome()

driver.get('https://www.zhihu.com/question/294701927/answer/1615170394')
driver.find_element_by_xpath("//button[@class='Button Modal-closeButton Button--plain']").click()
try:
    driver.find_element_by_xpath("//a[@class='QuestionMainAction ViewAll-QuestionMainAction']").click()
except:
    pass

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)

for i in range(0, 200000, 1500):
    driver.execute_script('window.scrollBy(0, {})'.format(i))
    try:
        driver.find_element_by_xpath('//a[@class="QuestionMainAction ViewAll-QuestionMainAction"]').click()
    except:
        pass
        # driver.execute_script('window.scrollBy(0, {})'.format(-(i-1000)))
    time.sleep(3)

html = etree.HTML(driver.page_source)
contents = html.xpath('//div[@class="List-item"]')

driver.quit()
for i in contents:

    try:
        author_name = i.xpath('.//a[@class="UserLink-link"]/text()')[0]
    except:
        author_name = i.xpath('.//span[@class="UserLink AuthorInfo-name"]/text()')[0]
    content = i.xpath('.//span[@itemprop="text"]//text()')
    content = '\n'.join(content)

    sql = "INSERT INTO 你觉得大学期间最恶心的事是什么 values('{}','{}')".format(author_name, content)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
        continue

    print("作者："+author_name+':')

cursor.close()
conn.close()  # 关闭数据库连接