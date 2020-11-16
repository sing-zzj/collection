# --*--  coding:utf-8  --*--
# @Time : 2020/11/16 8:56
# @Author : 啊。懋勋
# @version: Python 3.7
# @File : jobs.py

'''
目标：使用selenium, 爬取拉勾网
第三方库：Beautiful, selenium
注意：
    1.程序使用了selenium, 来调动Chrome来启动, 需要提前安装
    2.需要提前注册
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time
import csv

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=')  # 爬取拉钩网Python工作职位介绍

    driver.implicitly_wait(5)
    try:
        driver.find_element_by_class_name('body-btn').click()
    except:
        pass

    '''
    模拟登陆，需要自己操作打码或者找第三方平台
    '''
    driver.find_element_by_class_name('login').click()

    driver.find_element_by_xpath("//form/div[1]/div").click()
    username = driver.find_element_by_xpath("//form/div[1]/div/input")
    username.send_keys('输入自己创建的账户')

    driver.find_element_by_xpath("//form/div[2]/div").click()
    passward = driver.find_element_by_xpath("//form/div[2]/div/input")
    passward.send_keys('输入自己密码')

    driver.find_element_by_xpath('//div[@class="login-btn login-password sense_login_password btn-green"]').click()

    print("打码中，请等待！")
    time.sleep(20)
    print('打~码~完~成！')

    # 创建存储
    pf = open('python_jobs.csv', 'w', encoding='utf-8')
    writer = csv.writer(pf)
    writer.writerow(['职位', '地点', '公司名称', '薪水', '要求'])
    pf.close()

    # 开始爬取
    while True:

        driver.implicitly_wait(2)
        try:
            driver.find_element_by_class_name('body-btn').click()
        except:
            pass

        # 解析页面
        text = driver.page_source
        soup = BeautifulSoup(text, 'lxml')
        div = soup.find('div', class_='s_position_list')
        lis = div.find('ul', 'item_con_list').find_all('li', 'con_list_item')

        for li in lis:
            company = li['data-company']
            position = li['data-positionname']
            address = li.find('span', 'add').find('em').get_text()
            salary = li.find('span', 'money').get_text()
            requirment = li.find('div', class_='li_b_l').get_text().strip()[8:].strip()

            # 存储到csv中
            with open('python_jobs.csv', 'a', encoding='utf-8') as pf:
                writer = csv.writer(pf)
                writer.writerow([position, address, company, salary, requirment])

        # 实现翻页
        try:
            driver.find_element_by_xpath('//*[@class="pager_container"]/span[@class="pager_next "]').click()
        except:
            driver.find_element_by_xpath('//*[@class="pager_container"]/span[@class="pager_next pager_next_disabled"]')\
                .click()
            break
