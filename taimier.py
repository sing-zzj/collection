# --*--  coding:utf-8  --*--
# @Time : 2020/12/8 9:25
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : taimier.py

from urllib.parse import urlencode

import requests
from lxml import etree

base = "https://en.glosbe.com/en/ta/{}/fragment/tmem?page={}&mode=MUST&stem=true&includedAuthors=&excludedAuthors="
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/86.0.4240.198 Safari/537.36'
}

def words():
    '''
    处理单词
    :return:
    '''
    with open('C:/Users/Administrator/Desktop/dicts/dicts_s.txt', encoding='utf-8') as fp:
        words = fp.read()
    all_words = words.split('\n')
    all_words[0] = 'ABC'

    return all_words

def get_sign(url):

    html = get_html(url)
    try:
        html.xpath('//p/text()')[0].strip()
    # if sign == "No examples found, consider adding one please.":
        return True
    # else:
    except:
        return False

def get_html(url):
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)

    return html

def parse(html):

    ens = html.xpath("//div[@class='w-1/2 pr-2 ']")
    ens = list(map(lambda i: ''.join(i.xpath(".//text()")).strip(), ens))
    tas = html.xpath("//div[@lang='ta']")
    tas = list(map(lambda i: ''.join(i.xpath(".//text()")), tas))

    print(ens)
    print(tas)
    download(ens, tas)

def download(ens, tas):
    pass

def main(word):

    for i in range(1, 10):
        url = base.format(word, i)
        if get_sign(url):
            break

        html = get_html(url)
        parse(html)


if __name__ == "__main__":
    get_words = words()

    main("this")
