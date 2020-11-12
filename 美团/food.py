# --*--  coding:utf-8  --*--
# @Time : 2020/11/12 10:08
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : food.py

import requests
from tqdm import tqdm
import re
import csv
import os

class Food(object):
    '''
    爬取美团美食信息（店名称，地址，评分，人均消费，链接）
    '''
    def __init__(self, baseurl, headers):
        self.baseurl = baseurl
        self.headers = headers

    def resp(self, url):
        '''
        下载数据
        :param url:
        :return:
        '''
        resquests = requests.get(url, headers=self.headers)
        return resquests.text

    def parse(self, j):
        '''
        解析页面
        :return:
        '''
        # for i in range(68):
        url = self.baseurl.format(j)
        text = self.resp(url)

        title_patten = r'(?<="title":").+?(?=",)'
        title = re.compile(title_patten).findall(text)

        score_patten = r'(?<="avgScore":).+?(?=,")'
        score = re.compile(score_patten).findall(text)

        address_patten = r'(?<="address":").+?(?=",)'
        address = re.compile(address_patten).findall(text)

        price_patten = r'(?<="avgPrice":).+?(?=,)'
        price = re.compile(price_patten).findall(text)

        link_patten = r'(?<="poiId":).+?(?=,)'
        link = re.compile(link_patten).findall(text)

        return title[-15:], score[-15:], address[-15:], price[-15:], link[-15:]

    def download(self, j):

        address = 'D:/food.csv'
        fload = os.path.exists(address)
        if not fload:
            f = open('D:/food.csv', 'a')
            food_info = csv.writer(f)
            food_info.writerow(['Title', 'Score', 'Address', 'Avg_mongey', 'Link'])
            f.close()

        title, score, address, price, link = self.parse(j)
        for i in range(15):
            with open('D:/food.csv', 'a', encoding='utf-8') as pf:
                food_info = csv.writer(pf)
                food_info.writerow([title[i], score[i], address[i], price[i], 'https://www.meituan.com/meishi/' + link[i] + '/'])


if __name__ == '__main__':

    #爬虫配置
    baseurl = 'https://hf.meituan.com/meishi/pn{}/'   #合肥美团美食信息，可以根据自己的需要添加
    headers = {
        'Cookie': 'uuid=195a74603db04122aa85.1605143715.1.0.0; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_cuid=175ba056759c8-0f9ec5ca1c01a7-230346d-1fa400-175ba056759c8; ci=56; rvct=56; __mta=251589561.1605143733138.1605143733138.1605143733138.1; client-id=4af19a72-963f-44c2-99c1-0662a99e6a1a; _lxsdk=175ba056759c8-0f9ec5ca1c01a7-230346d-1fa400-175ba056759c8; _hc.v=db163679-1a7b-d911-57a3-89988f1eaef0.1605143780; lat=31.855394; lng=117.256028; _lxsdk_s=175ba05675b-005-bdf-12e%7C%7C14',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    for i in tqdm(range(1, 68)): #定义爬取的页数，可以根据自己的需要定义，默认的是美团显示的所有
        food = Food(baseurl, headers)
        food.download(i)
