
import requests
import re


def getProvinceCode(province_name):

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
       print(res_str)

       pattern = r'<string>{},(.*?)</string>'.format(province_name)
       prov_code_list = re.findall(pattern, res_str)

       if prov_code_list:
              print(prov_code_list[0])
              return prov_code_list[0]
       else:
              print('查无信息，请确认所输入的省份名称是否正确')
              return None


if __name__ == '__main__':
    name = '江'
    getProvinceCode(name)
