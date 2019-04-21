from urllib import request
import random

# 反爬虫2：判断请求来源的IP
# 对策：使用代理IP

proxy_list = [
    {"http": "116.113.27.170:47849"},
    {"http": "222.139.245.130:58424"},
    {"http": "183.148.152.173:9999"},
    {"http": "58.254.220.116:52470"},
    {"http": "61.176.223.7:58822"},
]

proxy = random.choice(proxy_list)

# 构建代理处理器对象
proxy_handler = request.ProxyHandler(proxy)

# 创建自定义的opener
my_opener = request.build_opener(proxy_handler)

# 创建请求对象
req = request.Request("http://www.baidu.com")

res = my_opener.open(req).read().decode()

print(res)

