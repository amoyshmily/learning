import urllib
from urllib import parse
from urllib import request
import json

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
key = '我要自学网'

my_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'}

data = {
    'i': key,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15524838893979',
    'sign': '802affd75b1b1d4fccde464f3eb6c150',
    'ts': '1552483889397',
    'bv': '1331340ff40f1d556265c8cb1ced8876',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false'
    }

my_data = urllib.parse.urlencode(data).encode(encoding='utf-8')

req = request.Request(url, data=my_data, headers=my_header)
res = request.urlopen(req).read().decode()

print(res)

