# --*--  coding:utf-8  --*--
# @Time : 2021/1/19 8:57
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : youDao.py

'''
获取有道翻译接口
使用自己的 headers
'''

import time
import random
import hashlib
import requests

word = input('Please enter word of insert: ')


lts = str(int(time.time()*1000))
salt = lts + str(random.randint(0, 9))

str_sign = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
hl = hashlib.md5()
hl.update(str_sign.encode())
sign = hl.hexdigest()

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers = {
    # 填写自己的headers,包含全部信息，要不然请求不下来
}

datafrom = {
            'i': word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': lts,
            'bv': 'e65e8e5642f3c2d719d32db0b5eff1f9',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
           ' action': 'FY_BY_REALTlME'
}

resp = requests.post(url, data=datafrom, headers=headers)

query = resp.json()
# for i in query['smartResult']['entries']:
#     print(i)
print(query)