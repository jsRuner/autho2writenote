#!/usr/bin/env python
# encoding: utf-8

import os,sys,md5,time,urllib2,urllib
import ConfigParser
import chardet

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
def checkfile(lasttime,notepath):
    statinfo = os.stat(r"%s" % notepath)
    filetime = statinfo.st_mtime
    status = False
    if filetime != lasttime:
        print(u'%s 文件发生变化' % time.strftime('%Y-%m-%d %H:%M:%S'))
        status = True
    #     需要去与服务器通信。传递数据

    else:
        print(u'%s 文件没有发生变化' % time.strftime('%Y-%m-%d %H:%M:%S'))
        status = False
    rs = {'filetime':filetime,'status':status}
    return rs



def post_msg(url,msg):
    data = {}
    data['msg'] = msg
    post_data = urllib.urlencode(data)

    #提交，发送数据
    req = urllib2.urlopen(url, post_data)

    #获取提交后返回的信息
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

     # 读取配置。配置文件必须正确。
    config = ConfigParser.ConfigParser()
    config.readfp(open('autowritenoteclient.ini', "rb"))
    email =  config.get("global", "email")
    password =  config.get("global", "password")
    key =  config.get("global", "key")
    notepath =  config.get("global", "notepath")
    checkfiletime =  config.get("global", "checkfiletime")


    print("http://wuwenfu.cn/?add_jin_post=luoding123&type=1&email=%s&password=%s&key=%s"% (email,password,key))

    #  发送一次请求。携带账号与密码。 后续的请求不携带账号与密码。
    f = urllib.urlopen("http://wuwenfu.cn/?add_jin_post=luoding123&type=1&email=%s&password=%s&key=%s"% (email,password,key))


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
        rs = checkfile(currenttime,notepath)
        currenttime = rs['filetime']

        if rs['status']:
            # 读取文件内容，发送过去。
            url = "http://wuwenfu.cn/?add_jin_post=luoding123&type=2&key=%s"% key
            msg = open(notepath).read()
            # print(msg.decode('utf-8'))
            # 去掉前后的空格
            post_msg(url,msg.strip())
        time.sleep(float(checkfiletime))
