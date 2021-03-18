# --*--  coding:utf-8  --*--
# @Time : 2020/8/12 11:22
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : project4.py

import requests
import re
from lxml import etree

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

    url = "https://context.reverso.net/translation/english-arabic/" + word
    formdata = {'type': 'index',
                'npage': 1
                }
    response = requests.post(url, data=formdata, headers=headers)
    #html = response.text
    #print(html)
    html = get_html(url,formdata)
    patten = r'(?<=data-exact=")[0-9]+'
    regix = re.search(patten,html)
    try:
        num = regix.group()
        num = int(int(num) / 20)
        if num > 100:
            num = 100
        return num
    except:
        return 30
    
def get_words(html):

    # url = "https://context.reverso.net/translation/english-japanese/people"
    # formdata = {'type': 'index',
    #             'npage': 2
    #             }
    # response = requests.post(url, data=formdata, headers=headers)
    # html = response.text
    # print(html)
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
    english = html.xpath('//span[@lang="ar"]')
    for element in english:
        info = str(element.xpath('string(.)'))
        info = info.lstrip()
        Japanese.append(info)

    return English,Japanese

def download(English,Japanese):

    with open("demo1/English.txt",'a',encoding="utf-8") as fp:
        fp.write('\n'.join(English))
        fp.write('\n')
    with open("demo1/Japanese.txt",'a',encoding="utf-8") as f:
        f.write('\n'.join(Japanese))
        f.write('\n')

def main(words):
    for word in words:
        total = get_total(word)
        if total == 0:
            continue
        for i in range(1,total + 1):
            formdata = {'type': 'index',
                        'npage': i
                        }
            url = "https://context.reverso.net/translation/english-arabic/" + word
            html = get_html(url,formdata)
            if isinstance(html,str):
                English,Japanese = get_words(html)
            else:
                continue
            print(i,English)
            if len(English) == len(Japanese):
                download(English,Japanese)
        print(word,"下载完成")

if __name__ == '__main__':
    words = words()
    main(words())
