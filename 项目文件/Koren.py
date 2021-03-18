import requests
import re
from queue import Queue
from threading import Thread

headers = {
    'cookie': 'vnac_reword=false; DICT_CT="(null)"; DICT_BLOCALE=zh_CN; DICT_DD=enth; '
              '_ga=GA1.2.1397969609.1595382192; NNB=DVLOYEFRTELV6; DICT_HC=0; DICT_LOCALE2=zh_CN; '
              'IS_PLATFORM_ENKODICT_USER=true; JSESSIONID=B9D7648DDCDCB2B8C51672D4163B4EC7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/84.0.4147.89 Safari/537.36'	

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

def total(word):
    '''
    get number of word
    :param word:
    :return total:
    '''
    word_url = "https://en.dict.naver.com/api3/enko/search?query=" + word + \
                "&m=pc&range=example&page=1&lang=ko&shouldSearchVlive=false"

    response = requests.get(word_url,headers = headers)
    html = response.text
    #print(html)
    patten = r'(?<="total":)[0-9]+'
    regix = re.search(patten, html)
    number = int(regix.group())
    if number > 2010:
        number = 2010
    if number % 15 == 0:
        total = number / 15
    else:
        total = number / 15 + 1

    print(int(total),word)
    return int(total)

def list_word(html):
    '''
    get finall words list
    :param html:
    :return:
    '''
    patten = r'"expExample1":".+?"'
    sects = re.findall(patten, html)
    EnglishWords = []
    for word in sects:
        word = word[15:-1]
        word = word.replace("<strong>", '')
        word = word.replace("</strong>", '')
        word = word.replace("&quot;", '')
        EnglishWords.append(word)

    patten = r'"expExample2":".+?"'
    sects = re.findall(patten, html)
    Korean = []
    for word in sects:
        word = word[15:-1]
        word = word.replace("<strong>", '')
        word = word.replace("</strong>", '')
        word = word.replace("&quot;", '')
        Korean.append(word)

    return Korean,EnglishWords

def download(Korean,EnglishWords):
    '''
    :param Korean:
    :param EnglishWords:
    :return:
    '''
    with open("C:/Users/Administrator/Desktop/Project3/韩语2/Korean.txt", 'a',
              encoding='utf-8') as f:
        f.write("\n".join(Korean))
    with open("C:/Users/Administrator/Desktop/Project3/韩语2/English.txt", 'a',
              encoding='utf-8') as fp:
        fp.write("\n".join(EnglishWords))

def pro_urls(queue,words):
    for word in words:
        totals = total(word)
        if totals == 0:
            continue
        for value in range(1,totals + 1):
            word_url = "https://en.dict.naver.com/api3/enko/search?query="+ word + \
                       "&m=pc&range=example&page=" + str(value) + \
                       "&lang=ko&shouldSearchVlive=false"
            queue.put(word_url)

def con_urls(queue):
    while queue.empty is not True:
        url = queue.get()
        response = requests.get(url = url,headers = headers)
        html = response.text
        Korean,EnglishWords = list_word(html)
        print(len(Korean),len(EnglishWords))
        if len(Korean) == len(EnglishWords):
            download(Korean,EnglishWords)
        queue.task_done()

def main(words):
    queue = Queue(maxsize = 50)

    t1 = Thread(target = pro_urls,args = (queue,words,))
    t1.daemon = True
    t1.start()

    thread = []
    for i in range(5):
        t2 = Thread(target = con_urls,args = (queue,),daemon = True)
        thread.append(t2)

    for value in range(5):
        thread[value].start()

    t1.join()
    
    print("-- SUCCESS --")

if __name__ == '__main__':
    words = words()	
    main(words)
