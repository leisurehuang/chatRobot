# -*- coding: UTF-8 -*-
import types
import urllib2
import json
import string
import sys

from wxpy import *

# 设置系统语言utf8
reload(sys)
sys.setdefaultencoding('utf8')

# https://github.com/youfou/wxpy
bot = Bot()
bot.friends(update=True)
wxpy_groups = bot.groups().search('ci')
group = wxpy_groups[0]
group.send('lei\'s robot is coming!\r 回复“天气”可查询深圳天气信息')

endString = "\r[from lei\'s robot]"


@bot.register(group)
def reply_my_friend(msg):
    data = registerUrl()
    dataString = praseJsonFile(data)
    if '天气' in msg.text:
        return '深圳当前的天气情况如下:\r'+dataString + endString
    else:
        return '你可以问我“天气”'+endString


def registerUrl():
    try:
        url = "http://www.weather.com.cn/data/sk/101280601.html"
        data = urllib2.urlopen(url).read()
        return data
    except Exception, e:
        print e


def praseJsonFile(jsonData):
    value = json.loads(jsonData)
    rootlist = value.keys()
    strval = ""
    for rootkey in rootlist:
        subvalue = value[rootkey]
        for subkey in subvalue:
            strval = strval + str(subvalue[subkey]) + '\r'
    return strval


embed()
