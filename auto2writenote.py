#!/usr/bin/env python
# encoding: utf-8

import time
import urllib
import urllib2
import json
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
需要从数据库读取账号。读取要填写的日志。
账号表：id email password addtime updatetime 配置参数（何时发布日志，是否接受邮件通知，邮件地址），是否通过审核，
日志内容表：关联的账号id,日志内容。

操作的日志记录：id addtime msg

python不操作数据库。通过发送htt请求来实现。

接口：获取账号列表。
接口:发送日志记录。

"""

#  udrl
# 驱动
# 账号
# 密码
# 方法执行，就完整的一个流程。
# todo：暂时未能解决退出的问题，目前是通过关闭浏览器，再开一个解决的


def selenium(url,d,username,password,content):

    if d is None:
        print(u'驱动为空')
        driver = webdriver.Firefox()
    else:
        driver = d
    driver.get(url)
    driver.implicitly_wait(10)
    # 填写表单
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    print(u'填写账号与密码')
    time.sleep(5)
    # 登录
    driver.find_element_by_css_selector(".btn-submit").click()

    #这里要进行判断是否登录成功。如果不成功。则关闭浏览器。
    time.sleep(10)
    currenturl = driver.execute_script("return window.location.href;")
    if currenturl == url:
        print(u"登录失败")
        driver.close()
        return ''

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
        # 等待几秒后去填写日记
        time.sleep(5)
        # 这里容易出异常
        driver.execute_script("CKEDITOR.instances['modalContent'].setData('%s')" % content)
        print(u'日记填写完毕:%s' % content)
        time.sleep(5)
        # 点击提交。
        driver.find_element_by_id('btn_worklog_ok').click()

    else:
        print(u"本次操作属于编辑工作日记,开始退出浏览器")
    time.sleep(5)
    #关闭浏览器
    driver.close()
    print(u'退出成功')
    return ''

def get_info():
    f=urllib.urlopen("http://wuwenfu.cn/?get_jin_post=luoding123")

    s=f.read()
    d = json.loads(s)

    return d



    pass

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    website = 'https://sso.jingoal.com/oauth/authorize?client_id=jmbmgtweb&response_type=code&state={access_count%3A1}&redirect_uri=http%3A%2F%2Fweb.jingoal.com%2Fmgt2%2F%3Flocale%3Dzh_CN#/login'

    # 测试是否能正常运行。挂机一夜。
    requestsecond = 10
    # 10秒执行一次。请求php。请求获取账号信息。向博客发送请求api。
    count = 0

    while True:
        l = get_info()
        for item in l:
            print(item['email'])
            print(item['password'])
            print(item['msg'])
            count = count + 1

            start = time.time()
            selenium(website,None,item['email'],item['password'],item['msg'])
            spend = time.time() - start

            print('执行第%d次,花费时间:%d'% (count,spend))

        time.sleep(requestsecond)


