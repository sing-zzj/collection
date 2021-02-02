# --*--  coding:utf-8  --*--
# @Time : 2021/2/1 9:20
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : 图标.py

'''
说明：下载网站上的图标，并没有下载全部，只是网站更新上的
网址：https://www.easyicon.net/update/
需要添加自己的ua和cookie
'''

import requests
from lxml import etree
import os
import time
from concurrent import futures


start = time.time()
url = "https://www.easyicon.net/update/"
headers = {
    # 填写自己的ua和cookie
}

def parse(name, link):
    resp = requests.get(link, headers=headers)
    html = etree.HTML(resp.text)
    imgs = html.xpath('//div[@class="icon_img"]/a/img/@src')
    names = html.xpath('//div[@class="icon_img"]/a/@title')
    for img in zip(imgs, names):

        download(name, img)


def download(name, img):

    resp = requests.get(img[0])
    url = 'D:/图标2/' + name + '/' + img[1] + '-' +img[0][-8:-4] + '.png'
    with open (url, 'wb') as fp:
        fp.write(resp.content)

def main(icon):
    iconFolder = icon[44:-1]
    icon = icon + '{}/?m=yes&f=iconsetid&s='
    try:
        os.makedirs('D:/图标2/' + iconFolder)
    except Exception as erros:
        print(erros)
        pass
    for i in range(1, 20):
        link = icon.format(i)
        if len(requests.get(link).text) <= 30000:
            break
        parse(iconFolder, icon.format(i))


if __name__ == "__main__":

    resp = requests.get(url, headers=headers)

    html = etree.HTML(resp.text)
    icons = html.xpath('//li//a[@class="more"]/@href')
    icons = ["https://www.easyicon.net" + i for i in icons]
    max_work = 10

    with futures.ThreadPoolExecutor(max_work) as executor:
        res = executor.map(main, icons)


    end = time.time()
    print("run_time: " + str("%.1f" % (end - start)))
