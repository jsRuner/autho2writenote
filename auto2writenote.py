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
@file: auto2writenote.py
@time: 2016/1/8 13:32
自动填写笔记。

实现自动读取多个账号。无则新建，有则编辑。




"""

#  udrl
# 驱动
# 账号
# 密码
# 方法执行，就完整的一个流程。


def selenium(url,d,username,password,content):

    if d is None:
        print(u'驱动为空')
        driver = webdriver.Firefox()
    else:
        driver = d
    driver.get(url)
    driver.implicitly_wait(20)
    # 填写表单
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    print(u'填写账号与密码')
    time.sleep(5)
    # 登录
    driver.find_element_by_css_selector(".btn-submit").click()
    print(u'登录了')
    #强制睡眠。
    time.sleep(10)
    #打开写日志的页面
    driver.get("http://web.jingoal.com/module/worklog/workLogInfo.do")
    print(u'打开日志页面')
    # 有选择性的等待5秒
    driver.implicitly_wait(5)

    # 先判断是否是新建日志。如果存在，则点击新建日志，如果不存在，则点击编辑。可以通过js返回值来判断。
    jsstr ='if($("table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)")[0].innerHTML.indexOf("新建工作小结")>0 ){return 1;}else{return 2;}';
    rs =  driver.execute_script(jsstr)
    if rs == 1:
        print(u"本次操作属于新建工作日记")

        # 执行点击新建工作日志。第一次填写。table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1)
        driver.execute_script('$("table.table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1)").click()')
    else:
        print(u"本次操作属于编辑工作日记")
        # 说明已经写过了。这里应该是进行一次编辑即可。
        driver.execute_script('$(".table > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(3) > a:nth-child(1) > i:nth-child(1)").click()')
    # 等待几秒后去填写日记
    time.sleep(5)
    # driver.execute_script('$("#cke_modalContent > div:nth-child(2)").children()[1].innerHTML ="%s"' % content)
    driver.execute_script("CKEDITOR.instances['modalContent'].setData('%s')" % content)
    # driver.execute_script('$("#cke_modalContent > div:nth-child(2)").children()[1].innerHTML ="%s"' % content)
    print(u'日记填写完毕:%s' % content)
    time.sleep(5)
    # 点击提交。
    # driver.execute_script('$("#btn_worklog_ok").click()')
    driver.find_element_by_id('btn_worklog_ok').click()
    # driver.find_element_by_id('btn_worklog_ok').click()
    time.sleep(5)
    exit()
    #操作以后。需要退出。
    driver.get(url)
    time.sleep(5)
    # 点击退出按钮 div.dialog-shadow:nth-child(6) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)
    # driver.execute_script('$("div.dialog-shadow:nth-child(6) > ul:nth-child(2) > li:nth-child(4) > a:nth-child(1)").click()')
    print(u'退出成功')
    time.sleep(5)
    #需要返回驱动。避免下一次在启动浏览器
    return driver



class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    website = 'https://sso.jingoal.com/oauth/authorize?client_id=jmbmgtweb&response_type=code&state={access_count%3A1}&redirect_uri=http%3A%2F%2Fweb.jingoal.com%2Fmgt2%2F%3Flocale%3Dzh_CN#/login'
    notecontent = u"我今天没有忘记写工作小结222222222222222222211321321321321321"

    d = selenium(website,None,'540045865@qq.com','luoding123',notecontent)

    d = selenium(website,d,'18256963312','htt199002',notecontent)

    print(u'结束了')




    pass