from urllib import request
import urllib

# 处理GET请求

wd = {'wd': '北京'}

url = 'http://www.baidu.com'
param = urllib.parse.urlencode(wd)
