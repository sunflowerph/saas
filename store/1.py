
#coding=utf-8
import requests
import json
import datetime
# start='2020-03-26'
# end='2020-05-01'
#
# datestart=datetime.datetime.strptime(start,'%Y-%m-%d')
# dateend=datetime.datetime.strptime(end,'%Y-%m-%d')
# a=[]
# while datestart<dateend:
#     datestart+=datetime.timedelta(days=1)
#     b=datestart.strftime('%Y-%m-%d')
#     #print datestart.strftime('%Y-%m-%d')
#     a.append(b)
#
# print a
# for i in a:
#     print i
#

# nowtime=datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
# nowtime1=datetime.datetime.strptime(nowtime,'%Y-%m-%d  %H:%M:%S' )
# nexttime=nowtime1+datetime.timedelta(hours=2,seconds=1)
#
# print nowtime,nexttime



#
# from selenium import  webdriver
# import os
#
# driver=webdriver.Chrome(executable_path=os.path.abspath('../file/chromedriver')) #使用chorme浏览器驱动
# driver.get("http://www.baidu.com")
# data = driver.execute_script("return window.performance.getEntries();")
# data1=data[0]["connectEnd"]
#
# import time
# import datetime.datetime
# def cal_time(stamp1,stamp2):
#     t1=time.localtime(stamp1)
#     t2 = time.localtime(stamp2)
#     t1=time.strftime("%Y-%m-%d %H:%M:%S",t1)
#     t2 = time.strftime("%Y-%m-%d %H:%M:%S", t2)
#     time1=datetime.datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
#     time2 = datetime.datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")
#     return (time2-time1).seconds
#
#
#
# print data1

# import PyChromeDevTools
# import time
# import os
# os.chdir(r"/Applications/Google Chrome.app")
# cmd = "chrome.dmg --remote-debugging-port=9222"
# os.popen(cmd)
# chrome = PyChromeDevTools.ChromeInterface()
# chrome.Network.enable()
# chrome.Page.enable()
# chrome.Page.reload(ignoreCache=True) # 不带缓存
# start_time=time.time()
# chrome.Page.navigate(url="http://www.baidu.com/")
# chrome.wait_event("Page.loadEventFired", timeout=60)
# end_time = time.time()
# print("Page Loading Time:", end_time-start_time)
# chrome.close()



print "i am seccuess"

