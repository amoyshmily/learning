
import requests
import re
from WebService.demo.getRegionProvince import getProvinceCode


def getCityCode(prov_name, city_name):

       host = 'http://ws.webxml.com.cn'
       api_url = '/WebServices/WeatherWS.asmx'

       header = {'Content-Type': 'application/soap+xml; charset=utf-8'}

       body = '<?xml version="1.0" encoding="utf-8"?><soap12:Envelope' \
              ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
              ' xmlns:xsd="http://www.w3.org/2001/XMLSchema"' \
              ' xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">' \
              '<soap12:Body><getSupportCityString xmlns="http://WebXml.com.cn/">' \
              '<theRegionCode>{}</theRegionCode></getSupportCityString>' \
              '</soap12:Body></soap12:Envelope>'

       # 省份名称
       prov_code = getProvinceCode(prov_name)
       if prov_code:
              body = body.format('31120')
       else:
              return None

       res = requests.post(host+api_url, data=body, headers=header)
       res_str = res.content.decode()
       print(res_str)

       pattern = r'<string>{},(.*?)</string>'.format(city_name)
       city_list = re.findall(pattern, res_str)

       if city_list:
              print(city_list[0])
              return city_list[0]
       else:
              return None


if __name__ == '__main__':
    prov = '江西'
    city = '九江'
    getCityCode(prov, city)
