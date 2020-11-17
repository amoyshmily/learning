import json
import requests
from utils.utils import anti_https_warnings
import yaml


class Admin(object):
    api_provider = '百度'
    ak = ''
    sk = ''

    @anti_https_warnings
    def accessToken(self, from_config: bool = True) -> str:
        """
        获取调用百度OCR api所必需的token
        :return:token
        """

        # 走本地配置
        if from_config is True:
            with open('../config/admin.yml', 'rb') as f:
                data = yaml.load(f)
                if data:
                    self.ak = data.get('api_key')
                    self.sk = data.get('secret_key')


        url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'
        res = requests.get(url=url.format(self.ak, self.sk), verify=False, timeout=10)

        return res.json().get('access_token')

    def __repr__(self):
        obj_data = {'aip_provider': self.api_provider, 'api_ak': self.ak, 'api_sk': self.sk}
        return json.dumps(obj_data, ensure_ascii=False)


if __name__ == '__main__':
    admin = Admin()
    print(admin.accessToken())
