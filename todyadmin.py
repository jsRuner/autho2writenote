#!/usr/bin/env python
# encoding: utf-8

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

"""
@version: 1.0
@author: hiphp
@license: Apache Licence 
@contact: hi_php@163.com
@site: wuwenfu.cn
@software: PyCharm Community Edition
@file: todyselenium.py
@time: 2016/1/8 8:23
"""


def selenium(url):
    driver = webdriver.Firefox()
    driver.get(url)
    driver.implicitly_wait(20)
    # 定位元素
    driver.find_element_by_id("email").send_keys('540045865@qq.com')
    driver.find_element_by_id("password").send_keys('luoding123')
    # exit()
    driver.find_element_by_css_selector(".btn-submit").click()

    time.sleep(10)

    # driver.implicitly_wait(10)

    driver.get("http://web.jingoal.com/module/worklog/workLogInfo.do")
    driver.implicitly_wait(10)

    # 先判断是否是新建日志。如果存在，则点击新建日志，如果不存在，则不执行。可以通过js返回值来判断。
    # $("table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)")[0].innerHTML.indexOf("新建工作小结")

    jsstr ='if($("table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)")[0].innerHTML.indexOf("新建工作小结")>0 ){return 1;}else{return 2;}';

    rs =  driver.execute_script(jsstr)

    if rs == 1:
        print 'rs = %s' % rs

        # 执行点击新建工作日志。第一次填写。table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1)
        # table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1)
        driver.execute_script('$("table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1)").click()')
        pass
    else:
        print 'rs = %s' % rs

        # 说明已经写过了。这里应该是进行一次编辑即可。
        # 执行编辑的js代码。.table > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(3) > a:nth-child(1)
        driver.execute_script('$(".table > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(3) > a:nth-child(1) > i:nth-child(1)").click()')

        # exit()
        pass






    # driver.execute_script('$(".table > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(3) > a:nth-child(1) > i:nth-child(1)").click()')

    time.sleep(5)
    # 如果不存在。则直接退出。说明写过了。
    # driver.find_element_by_css_selector(".mpic-pen").click()
    # driver.execute_script('document.getElementById("myModal").childNodes[3].childNodes[1].childNodes[3].childNodes[1].childNodes[2].childNodes[1].childNodes[1].innerHTML = "hfajkjfkdsfds"')
    driver.execute_script('$("#cke_modalContent > div:nth-child(2)").children()[1].innerHTML =1')
    time.sleep(5)
    driver.execute_script('$("#cke_modalContent > div:nth-child(2)").children()[1].innerHTML =2')

    time.sleep(5)
    driver.execute_script('$("#cke_modalContent > div:nth-child(2)").children()[1].innerHTML =3')

    time.sleep(5)
    driver.execute_script('$("#cke_modalContent > div:nth-child(2)").children()[1].innerHTML =4')





    # driver.find_element_by_id('btn_worklog_ok').click()


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    website = 'https://sso.jingoal.com/oauth/authorize?client_id=jmbmgtweb&response_type=code&state={access_count%3A1}&redirect_uri=http%3A%2F%2Fweb.jingoal.com%2Fmgt2%2F%3Flocale%3Dzh_CN#/login'
    selenium(website)
    pass