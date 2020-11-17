import requests
from Projects.WebService.demo.getSupportCity import getCityCode

def getCityWeatherInfo(prov_name, city_name):


       host = 'http://ws.webxml.com.cn'
       api_url = '/WebServices/WeatherWS.asmx'

       header = {'Content-Type': 'application/soap+xml; charset=utf-8'}

       body = '<?xml version="1.0" encoding="utf-8"?>' \
              '<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
              ' xmlns:xsd="http://www.w3.org/2001/XMLSchema"' \
              ' xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"><soap12:Body>' \
              '<getWeather xmlns="http://WebXml.com.cn/"><theCityCode>{}</theCityCode>' \
              '<theUserID>{}</theUserID></getWeather></soap12:Body></soap12:Envelope>'

       user_id = ''
       city_code = getCityCode(prov_name, city_name)

       if city_code:
              body = body.format(city_code, user_id)

              res = requests.post(host+api_url, data=body, headers=header)
              res_str = res.content.decode()

              print(res_str)
       else:
              return None

       # doc = dom.parse('./weather.xml')
       # doc = dom.parseString(res_str)
       #
       # root = doc.documentElement
       #
       # result = root.getElementsByTagName('getWeatherResult')[0]
       # fields = result.getElementsByTagName('string')
       #
       # for field in fields:
       #     val = field.childNodes[0].data
       #     print(val)
       #
       # for i in range(3):
       #     print(3)


if __name__ == '__main__':
    getCityWeatherInfo('江西', '九江')
