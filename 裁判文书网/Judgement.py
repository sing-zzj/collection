# --*--  coding:utf-8  --*--
# @Time : 2021/1/26 16:21
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : third.py

import time
from selenium import webdriver
import json
from lxml import etree
from selenium.webdriver.common.action_chains import ActionChains
import logging

def getLink(text):
    html = etree.HTML(text)
    title = html.xpath('//div[@class="LM_list"]//div[@class="list_title clearfix"]/h4/a/text()')
    link = html.xpath('//div[@class="LM_list"]//div[@class="list_title clearfix"]/h4/a/@href')
    links = ["https://wenshu.court.gov.cn/website/wenshu" + i[2:] for i in link]
    return title, links

def getContent(text, title):
    html = etree.HTML(text)
    content = html.xpath('//div[@class="PDF_pox"]//text()')

    with open('d:/裁判文书网/刑事案件/'+title+'.txt', 'a', encoding='utf-8') as pf:
        pf.write(''.join(content).strip())
    print(content)

logging.basicConfig(filename='link.log', filemode='w', level=logging.DEBUG)

driver = webdriver.Chrome()
driver.get('https://wenshu.court.gov.cn/website/wenshu/181010CARHS5BS3C/index.html?https://wenshu.court.gov.cn/website/wenshu/181029BPRY8AYR1P/index.html?open=login')
time.sleep(40)

driver.get('https://wenshu.court.gov.cn/website/wenshu/181217BMTKHNT2W0/index.html?s8=04&pageId=0.006107918622198838')
time.sleep(30)

titleList, linkList = getLink(driver.page_source)
i = 0
while True:

    try:
        element = driver.find_element_by_link_text("下一页")
        ActionChains(driver).double_click(element).perform()
        time.sleep(7)
    except:
        continue

    titles, links = getLink(driver.page_source)
    titleList = titleList + titles
    linkList = links + linkList
    print(len(linkList))
    logging.debug(dict(zip(titleList, linkList)))

    i += 1
    if i == 200:
        break

print(linkList)
print(titleList)
for i in range(len(titleList)):
    driver.get(linkList[i])
    time.sleep(2)
    getContent(driver.page_source, titleList[i]+linkList[i][-4:-1])
