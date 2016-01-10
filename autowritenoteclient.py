#!/usr/bin/env python
# encoding: utf-8

import os, sys, md5, time, urllib2, urllib
import ConfigParser
import chardet
import re

"""
@version: 1.0
@author: hiphp
@license: Apache Licence
@contact: hi_php@163.com
@site: wuwenfu.cn
@software: PyCharm Community Edition
@file: autowritenoteclient.py
@time: 2016/1/9 15:21

2016年1月9日 自动读取本地文件，作为日志内容。

需要配置参数。配置ok。才能运行。

配置里，需要填写账号与密码。




"""


def checkfile(lasttime, notepath):
    statinfo = os.stat(r"%s" % notepath)
    filetime = statinfo.st_mtime
    status = False
    if filetime != lasttime:
        print(u'%s 文件发生变化' % time.strftime('%Y-%m-%d %H:%M:%S'))
        status = True
    # 需要去与服务器通信。传递数据

    else:
        print(u'%s 文件没有发生变化' % time.strftime('%Y-%m-%d %H:%M:%S'))
        status = False
    rs = {'filetime': filetime, 'status': status}
    return rs


def post_msg(url, msg):
    data = {}
    data['msg'] = msg
    post_data = urllib.urlencode(data)

    # 提交，发送数据
    req = urllib2.urlopen(url, post_data)

    # 获取提交后返回的信息
    content = req.read()
    if content == 'success':
        print(u'%s 发送日志成功,同步到今目标需要4-5分钟' % time.strftime('%Y-%m-%d %H:%M:%S'))
    else:
        print(u'%s 发送日志失败' % time.strftime('%Y-%m-%d %H:%M:%S'))
        exit()


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':

    readme = u"######################################################################\r\n" \
             u"本软件支持同步本地txt文本内容到指定的今目标账号中。可以扩展增加其他的同步。" \
             u"需要注意，txt文件必须是utf-8编码，直接创建的txt是ascii编码。" \
             u"\r\n#####################################################################"
    print(readme)

    # 先检查必备的文件，一个是日志文件，一个是配置文件
    if not os.path.exists('autowritenoteclient.ini'):
        print(u'配置文件不存在')
        time.sleep(5)
        exit()

        # 读取配置。配置文件必须正确。
    config = ConfigParser.ConfigParser()
    config.readfp(open('autowritenoteclient.ini', "rb"))
    email = config.get("global", "email")
    password = config.get("global", "password")
    key = config.get("global", "key")
    notepath = config.get("global", "notepath")
    checkfiletime = config.get("global", "checkfiletime")


    print(u"当前你的配置如下\r\n账号:%s \r\n"
          u"密码:%s\r\n"
          u"日志路径：%s\r\n"
          u"请确认没有错误，选择回车继续..." % (email,password,notepath))
    try:
        raw_input()
        input = raw_input
    except:
        input()
        # print("http://wuwenfu.cn/?add_jin_post=luoding123&type=1&email=%s&password=%s&key=%s"% (email,password,key))

#  发送一次请求。携带账号与密码。 后续的请求不携带账号与密码。
f = urllib.urlopen(
    "http://wuwenfu.cn/?add_jin_post=luoding123&type=1&email=%s&password=%s&key=%s" % (email, password, key))

info = f.read()

if info == 'success':
    print(u'与服务器通信成功')
else:
    print(u'配置错误,5秒后关闭')
    print(u'配置错误,5秒后关闭')
    print(u'配置错误,5秒后关闭')
    time.sleep(5)

currenttime = time.time()

while True:
    rs = checkfile(currenttime, notepath)
    currenttime = rs['filetime']


    if rs['status']:
        # 读取文件内容，发送过去。
        url = "http://wuwenfu.cn/?add_jin_post=luoding123&type=2&key=%s" % key
        msg = open(notepath).read()
        # print(msg.decode('utf-8'))
        # 正则去掉内容
        p = re.compile('\s+')
        new_string = re.sub(p, '', msg)
        post_msg(url, new_string)
    time.sleep(float(checkfiletime))
