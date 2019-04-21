# -*- coding: encoding -*-
import requests
import re

host = 'http://ws.webxml.com.cn'
api_url = '/WebServices/WeatherWS.asmx'

header = {'Content-Type': 'application/soap+xml; charset=utf-8'}

body = '<?xml version="1.0" encoding="utf-8"?>' \
       '<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
       ' xmlns:xsd="http://www.w3.org/2001/XMLSchema" ' \
       'xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">' \
       '<soap12:Body><getRegionProvince xmlns="http://WebXml.com.cn/" />' \
       '</soap12:Body></soap12:Envelope>'

res = requests.post(host+api_url, data=body, headers=header)
res_str = res.content.decode()

pattern = r'<string>江西,(.*?)</string>'
val = re.findall(pattern, res_str)
print(val)
