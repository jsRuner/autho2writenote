#!/usr/bin/env python
# encoding: utf-8

import urllib2,urllib,os,re,socket,requests,json,time
socket.setdefaulttimeout(50)
"""
@version: 1.0
@author: hiphp
@license: Apache Licence 
@contact: hi_php@163.com
@site: wuwenfu.cn
@software: PyCharm Community Edition
@file: today.py
@time: 2016/1/7 10:18

实现今日平台的注册。

拿到用户的数据
2016年1月7日10:53:08 测试通过，获取公司的数据




"""


def func():
    pass

def post_todydata(url):


    html = ''
    request = urllib2.Request(url)
    #这里依次添加数据。
    request.add_header('Host', 'web.jingoal.com')
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0")
    request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    request.add_header("Accept-Encoding","gzip, deflate")
    request.add_header("Referer","http://web.jingoal.com/")
    request.add_header("Cookie","JSESSIONID=2BC3A9816E13B5EFD99CBD02FB397D7B; bigDataUuid=58ad1a3d-df86-6cc5-5f0c-c7ecbcbb0acf; Hm_lvt_586f9b4035e5997f77635b13cc04984c=1452131608; Hm_lpvt_586f9b4035e5997f77635b13cc04984c=1452132229; route=2ca4056f796c8859c284e03101562e51; companyCode=5368825; companyName=%E6%9D%AD%E5%B7%9E%E5%82%B2%E4%BA%9A%E7%A7%91%E6%8A%80; iCode=609c411340492ee1bff94ad03a8801e2cf4c36c99c204ad6; _ga=GA1.2.733953241.1452131609; loginStr=luoding%405368825; password=luoding123; account=540045865%40qq.com; tip=%E6%82%A8%E5%B7%B2%E6%88%90%E5%8A%9F%E5%8A%A0%E5%85%A5; cScheme=http%3A; TOURL=http%3A%2F%2Fweb.jingoal.com%2Fwebcd%2Fplan%2Frefworklog%2FhasPlans.do; ouri=http%3A%2F%2Fweb.jingoal.com%2F%23workbench; code=mPP30K; JINSESSIONID=207643d2-8af7-4234-b5cc-4420961959b8; cid=4867362; uid=16181529; showbanners=true")
    request.add_header("Connection","keep-alive")

    response = urllib2.urlopen(request)
    html = response.read()
    html = unicode(html,'utf-8')
    print(html)


def post_todydata1(url):


    html = ''
    request = urllib2.Request(url)
    request.add_header('Host', 'web.jingoal.com')
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0")
    request.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
    request.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    request.add_header("Accept-Encoding","gzip, deflate")
    request.add_header("Referer","http://web.jingoal.com/")
    # request.add_header("Content-Type","application/json")
    # request.add_header("Content-Type","")
    #这里依次添加数据。
    request.add_header("Cookie","JSESSIONID=2BC3A9816E13B5EFD99CBD02FB397D7B; bigDataUuid=58ad1a3d-df86-6cc5-5f0c-c7ecbcbb0acf; Hm_lvt_586f9b4035e5997f77635b13cc04984c=1452131608; Hm_lpvt_586f9b4035e5997f77635b13cc04984c=1452132229; route=2ca4056f796c8859c284e03101562e51; companyCode=5368825; companyName=%E6%9D%AD%E5%B7%9E%E5%82%B2%E4%BA%9A%E7%A7%91%E6%8A%80; iCode=609c411340492ee1bff94ad03a8801e2cf4c36c99c204ad6; _ga=GA1.2.733953241.1452131609; loginStr=luoding%405368825; password=luoding123; account=540045865%40qq.com; tip=%E6%82%A8%E5%B7%B2%E6%88%90%E5%8A%9F%E5%8A%A0%E5%85%A5; cScheme=http%3A; TOURL=http%3A%2F%2Fweb.jingoal.com%2Fwebcd%2Fplan%2Frefworklog%2FhasPlans.do; ouri=http%3A%2F%2Fweb.jingoal.com%2F%23workbench; code=mPP30K; JINSESSIONID=207643d2-8af7-4234-b5cc-4420961959b8; cid=4867362; uid=16181529; showbanners=true")
    request.add_header("Connection","keep-alive")
    # workLogId=85388918&segmentId=97361405&type=3&workLogTime=0
    params = urllib.urlencode({'segmentId':97361405,'type':3,'workLogTime':0,'workLogId':1})
    response = urllib2.urlopen(request,params)
    html = response.read()
    html = unicode(html,'utf-8')
    print(html)


def post_todydata2(url):


    html = ''
    request = urllib2.Request(url)
    request.add_header('Host', 'web.jingoal.com')
    request.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0")
    # request.add_header("Accept","*/*")
    # request.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3")
    # request.add_header("Accept-Encoding","gzip, deflate")
    # request.add_header("Connection","keep-alive")
    # request.add_header("Referer","http://web.jingoal.com/module/worklog/workLogInfo.do")
    request.add_header("Content-Type","application/json; charset=UTF-8")
    # request.add_header("Cookie","JSESSIONID=5E8E3FC8ABCCA305405DFA078C7046E9.mgt45; bigDataUuid=58ad1a3d-df86-6cc5-5f0c-c7ecbcbb0acf; Hm_lvt_586f9b4035e5997f77635b13cc04984c=1452131608; Hm_lpvt_586f9b4035e5997f77635b13cc04984c=1452132229; route=bd50ed34c686b8e3cc422eab7309a75b; companyCode=5368825; companyName=%E6%9D%AD%E5%B7%9E%E5%82%B2%E4%BA%9A%E7%A7%91%E6%8A%80; iCode=609c411340492ee1bff94ad03a8801e2cf4c36c99c204ad6; _ga=GA1.2.733953241.1452131609; loginStr=luoding%405368825; password=luoding123; account=540045865%40qq.com; tip=%E6%82%A8%E5%B7%B2%E6%88%90%E5%8A%9F%E5%8A%A0%E5%85%A5; cScheme=http%3A; TOURL=http%3A%2F%2Fweb.jingoal.com%2Fmodule%2Fworklog%2FlogSegment%2FeditSegmentPre.do; ouri=http%3A%2F%2Fweb.jingoal.com%2F%23workbench; code=mPP30K; JINSESSIONID=207643d2-8af7-4234-b5cc-4420961959b8; cid=4867362; uid=16181529; showbanners=true")
    request.add_header("Cookie","JSESSIONID=5E8E3FC8ABCCA305405DFA078C7046E9.mgt45; bigDataUuid=58ad1a3d-df86-6cc5-5f0c-c7ecbcbb0acf; Hm_lvt_586f9b4035e5997f77635b13cc04984c=1452131608; Hm_lpvt_586f9b4035e5997f77635b13cc04984c=1452132229; route=bd50ed34c686b8e3cc422eab7309a75b; companyCode=5368825; companyName=%E6%9D%AD%E5%B7%9E%E5%82%B2%E4%BA%9A%E7%A7%91%E6%8A%80; iCode=609c411340492ee1bff94ad03a8801e2cf4c36c99c204ad6; _ga=GA1.2.733953241.1452131609; loginStr=luoding%405368825; password=luoding123; account=540045865%40qq.com; tip=%E6%82%A8%E5%B7%B2%E6%88%90%E5%8A%9F%E5%8A%A0%E5%85%A5; cScheme=http%3A; TOURL=http%3A%2F%2Fweb.jingoal.com%2Fmodule%2Fworklog%2FlogSegment%2FeditSegmentPre.do; ouri=http%3A%2F%2Fweb.jingoal.com%2F%23workbench; code=mPP30K; JINSESSIONID=207643d2-8af7-4234-b5cc-4420961959b8; cid=4867362; uid=16181529; showbanners=true")
    request.add_header("X-Requested-With","XMLHttpRequest")
    #这里依次添加数据。
    # request.add_header("Cookie","JSESSIONID=2BC3A9816E13B5EFD99CBD02FB397D7B; bigDataUuid=58ad1a3d-df86-6cc5-5f0c-c7ecbcbb0acf; Hm_lvt_586f9b4035e5997f77635b13cc04984c=1452131608; Hm_lpvt_586f9b4035e5997f77635b13cc04984c=1452132229; route=2ca4056f796c8859c284e03101562e51; companyCode=5368825; companyName=%E6%9D%AD%E5%B7%9E%E5%82%B2%E4%BA%9A%E7%A7%91%E6%8A%80; iCode=609c411340492ee1bff94ad03a8801e2cf4c36c99c204ad6; _ga=GA1.2.733953241.1452131609; loginStr=luoding%405368825; password=luoding123; account=540045865%40qq.com; tip=%E6%82%A8%E5%B7%B2%E6%88%90%E5%8A%9F%E5%8A%A0%E5%85%A5; cScheme=http%3A; TOURL=http%3A%2F%2Fweb.jingoal.com%2Fwebcd%2Fplan%2Frefworklog%2FhasPlans.do; ouri=http%3A%2F%2Fweb.jingoal.com%2F%23workbench; code=mPP30K; JINSESSIONID=207643d2-8af7-4234-b5cc-4420961959b8; cid=4867362; uid=16181529; showbanners=true")

    # workLogId=85388918&segmentId=97361405&type=3&workLogTime=0
    # params = urllib.urlencode({"isAttach":0,"content":"<p>fds2111111112121dsa</p>"})
    params = {'content':False,'isAttach':'111'}
    response = urllib2.urlopen(request,data=json.dumps(params))
    html = response.read()
    html = unicode(html,'utf-8')
    print(html)



class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # link = 'http://web.jingoal.com/mgt/rest/common/get_companyorg?version=1&b1452133383084=1'
    # post_todydata(link);



    #
    # link1 = "http://web.jingoal.com/module/worklog/editEndSegment.do"
    #
    #
    #
    # post_todydata1(link1)


    # link2 = "http://web.jingoal.com/module/worklog/logSegment/editSegmentPre.do"

    link3 = "http://web.jingoal.com/module/worklog/editEndSegment.do"

    post_todydata2(link3)
