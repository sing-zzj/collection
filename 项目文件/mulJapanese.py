# --*--  coding:utf-8  --*--
# @Time : 2020/8/13 16:22
# @Author : 啊。懋勋

import requests
import re
from lxml import etree
from queue import Queue
from threading import Thread,Lock
import time

headers = {
    'Cookie': 'JSESSIONID=O4afUQe4O7sROC4y09FTo1Uy.bst-web12; context.lastpair=en-ja; '
              'CTXTNODEID=bstweb12; _ga=GA1.2.555009732.1597197153; _gid=GA1.2.1886347100.1597197153; '
              'experiment_context_H5bY9vKoU=0; __gads=ID=901027c450ad5a62:T=1597197163:S=ALNI_MYZhjP3aF_JNBMKmIlJDTAPk418KQ; '
              'didomi_token=eyJ1c2VyX2lkIjoiMTczZTA1ZTktZTVjZS02Njc0LTgyMjYtODRkN2JlZTliZjIxIiwiY3JlYXRlZCI6IjIwMjAtMDg'
              'tMTJUMDE6NTI6NDQuMTQ5WiIsInVwZGF0ZWQiOiIyMDIwLTA4LTEyVDAxOjUyOjQ0LjE0OVoiLCJ2ZXJzaW9uIjpudWxsfQ==; '
              '__qca=P0-608366657-1597197161795; _fbp=fb.1.1597197188052.1703047724; '
              'reverso.net.ReversoRefreshToken=3ea673a19a4292557007ba5c5f52823f3edba31bb019856df9a0d3b3825713a5; '
              'history_entry=people]#[chinese; history_pair=en-ja]#[en-ja; reverso.net.DeviceId=7406a944-a0b9-4f88-894d-'
              '1899afc97bda; '
              'reverso.net.ReversoAccessToken=eyJhbGciOiJSUzI1NiIsImtpZCI6IjNGMjREMUJENTAxNTUxQ0Q3QkFBNEI2MzU5MUFENT'
              'Y4MjUzQUY2N0MiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJQeVRSdlZBVlVjMTdxa3RqV1JyVmFDVTY5bncifQ.eyJuYmYiOjE1OTcyMDIy'
              'MDIsImV4cCI6MTU5NzIwNDAwMiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50LnJldmVyc28ubmV0IiwiYXVkIjpbImh0dHBzOi8vYWNjb'
              '3VudC5yZXZlcnNvLm5ldC9yZXNvdXJjZXMiLCJJZGVudGl0eVNlcnZlckFwaSJdLCJjbGllbnRfaWQiOiJjb250ZXh0d2ViIiwic3'
              'ViIjoiOGM0Mjk0NzMtZDQ0ZS00NjAxLTgyNDctNmM4NDJlZDc5MDI4IiwiYXV0aF90aW1lIjoxNTk3MTk3NzM1LCJpZHAiOiJsb2Nh'
              'bCIsInNjb3BlIjpbIm9wZW5pZCIsInByb2ZpbGUiLCJlbWFpbCIsInJvbGUiLCJJZGVudGl0eVNlcnZlckFwaSIsIm9mZmxpbmVfY'
              'WNjZXNzIl0sImFtciI6WyJsZWdhY3lfdXNlcl9hdXRoIl19.oMQ9QH7-4uEJk_ZWgA0o_t9WQrr1aiErtYe7PRsQgVnbVeM_MKJdo'
              'I8mxvkYZ8SFBqJFAkNH5KVnOEQthwS7NIWZy_55uD1xcW9j63FhfdeD_KLhSBUUP09n9B99e9_VmBX6s8-tX0fgIuG3Xd29imCBw77S'
              '9qS0VJvL4rvZAfnEkVcaQkZvN23z34QelM-XFHmtmoWF7UwB9_EFE2nsDX0hC98hfHVVdiOLcdNR-0cKdWpScXkF-CYgZunz8aT_u_e'
              '04qT_ZYbqZwBg3eBwrqmrUkqBmTD2Hj7_fTZGrmPjsSfSphWCLjE_cJtlI1Lg1QTpoa8kNWjk2DAoKS7YoQGCuizh7DxL-7Veotav'
              'depywzbzefxjpaSP40ihRdvDdmHq5Jtu9L-IQTZdqSKDzDMw01uaYogGge8_eYt6fKY933i31v0lHCx3cQ_SlrPsTNamWqCD0R1gE'
              'UoPi12PVujkRHo5NEFDB9Rvm8pj2Iah9PSQbdTXzOhDygCtHbblwlBf-gh-duaUiMJhGwC1K8rJSCmxQRrM1_tFM5xHexSgV3Iz-Spz6'
              'JbFPEpT2ESY0jYLHxXiF6KobGSUtrslK2CwDbST_nh4FZl7O6fLRhiHIT5U2FFtdlp3A676irbBb-HZq1GGozqdLnhF1GmHq679tTMkK6'
              'XQ0-uL3kVXOA4; reverso.net.LanguageInterface=en; experiment_translator_gws5LzeuR=1; reverso.net.entrday='
              '0; reverso.net.lastDir_en=english-definition; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}


def words():
    '''
    处理单词
    :return:
    '''
    with open("en.txt") as fp:
        content = fp.read()
    words = content.split("\n")
    words[0] = "Africa"
    words_ = []
    for value in range(len(words)):
        if value == len(words) - 1:
            words_.append(words[value])
            break
        else:
            if words[value] != words[value + 1]:
                words_.append(words[value])

    return words_

def get_html(url,formdata):
    i = 0;
    while i < 5:
        try:
            response = requests.post(url,data = formdata,headers = headers,timeout = 5)
            return response.text
        except requests.exceptions.RequestException:
            i += 1

def get_total(word):

    url = "https://context.reverso.net/translation/english-japanese/" + word
    formdata = {'type': 'index',
                'npage': 1
                }
    response = requests.post(url, data=formdata, headers=headers)
    html = get_html(url,formdata)
    #html = response.text
    #print(html)
    if isinstance(html,str):
        patten = r'(?<=data-exact=")[0-9]+'
        regix = re.search(patten,html)
        num = regix.group()
        num = int(int(num) / 20)
        if num > 200:
            num = 200
        return num

def get_words(html):

    html = etree.HTML(html)
    '''
    匹配英文
    '''
    English = []
    english = html.xpath('//*[@class="example" or @class="example blocked"]/div[1]/span')
    for element in english:
        info = str(element.xpath('string(.)'))
        info = info.lstrip()
        English.append(info)
    '''
    匹配日文
    '''
    Japanese = []
    english = html.xpath('//span[@lang="ja"]')
    for element in english:
        info = str(element.xpath('string(.)'))
        info = info.lstrip()
        Japanese.append(info)

    return English,Japanese

def download(English,Japanese):

    with open("demo3/English.txt",'a',encoding="utf-8") as fp:
        fp.write('\n'.join(English))
    with open("demo3/Japanese.txt",'a',encoding="utf-8") as f:
        f.write('\n'.join(Japanese))

def product_html(words,url_queue):
    for word in words:
        total = get_total(word)
        if total == 0:
            continue
        for i in range(1,total + 1):
            formdata = {'type': 'index',
                        'npage': i
                        }
            url = "https://context.reverso.net/translation/english-japanese/" + word
            sums = {'formdata':formdata,'url':url}
            url_queue.put(sums)
    
def consume(url_queue,html_queue):
    
    while url_queue.empty is not True:
        urls = url_queue.get()
        formdata = urls['formdata']
        url = urls['url']
        html = get_html(url,formdata)
        print(html)
        if html != 'None':
            html_queue.put(html)
        url_queue.task_done()

def con2(html_queue):
    while html_queue is not True:
        html = html_queue.get()
        try:
            English,Japanese = get_words(html)
            if len(English) == len(Japanese):
                download(English,Japanese)
                print('下载中..')
        except:
            print('sorry!')
        html_queue.task_done()

def main(words):
    url_queue = Queue()
    html_queue = Queue()
    
    t1 = Thread(target = product_html,args = (words,url_queue,))
    t1.daemon = True
    t1.start()

    for value in range(3):
        t2 = Thread(target = consume,args = (url_queue,html_queue,))
        t2.daemon = True
        t2.start()

    for i in range(3):
        t3 = Thread(target = con2,args = (html_queue,))
        t3.daemon = True
        t3.start()

    t1.join()
    print('t1:success')
    
if __name__ == '__main__':
    words = words()
    main(words)
