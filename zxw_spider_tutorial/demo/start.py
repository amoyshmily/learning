from urllib import request
import re

url = 'http://www.baidu.com'

req = request.Request(url)

res = request.urlopen(req).read().decode()

pattern = r'<title>(.*?)</title>'
data = re.findall(pattern, res)

print(data)
