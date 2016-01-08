#!/usr/bin/env python
# encoding: utf-8


"""
@version: 1.0
@author: hiphp
@license: Apache Licence 
@contact: hi_php@163.com
@site: wuwenfu.cn
@software: PyCharm Community Edition
@file: todytest.py
@time: 2016/1/7 14:14
"""

#coding=utf-8
import time
from splinter import Browser

def splinter(url):
    browser = Browser()
    # browser = Browser("chrome")
    #login 126 email websize
    browser.visit(url)
    #wait web element loading
    # time.sleep(5)
    #fill in account and password
    # browser.find_by_xpath("//i[@class='icon-user']")

    # exit()
    browser.find_by_id("email").fill('540045865@qq.com')
    browser.find_by_id("password").fill('luoding123')
    #click the button of loginu
    browser.find_by_css('a.btn-submit').first.click()
    time.sleep(8)
    browser.find_by_text(u'日志').click()

    browser.visit("http://web.jingoal.com/module/worklog/workLogInfo.do")

    time.sleep(8)

    browser.find_by_css('.mpic-pen').last.click()
    # browser.find_by_css('.mpic-pen').first.click()
    # browser.find_by_xpath("//td[@class='noleft']/a").first.click()

    time.sleep(8)
    browser.execute_script('document.getElementsByClassName("cke_wysiwyg_div cke_reset cke_editable cke_editable_themed cke_contents_ltr cke_show_borders")[1].innerHTML = "<p>Hello world!</p>"')
    # browser.find_by_css('div.cke_wysiwyg_div').last.text('111111')
    #
    time.sleep(8)
    browser.find_by_id('btn_worklog_ok').first.click()

    #close the window of brower
    # browser.quit()

if __name__ == '__main__':
    # websize3 ='http://www.126.com'
    website = 'https://sso.jingoal.com/oauth/authorize?client_id=jmbmgtweb&response_type=code&state={access_count%3A1}&redirect_uri=http%3A%2F%2Fweb.jingoal.com%2Fmgt2%2F%3Flocale%3Dzh_CN#/login'
    splinter(website)