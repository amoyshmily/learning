import yaml
import logging.config
import os
from appium import webdriver
from time import ctime


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

# 指定已成功连接的设备识别码（可以使用adb devices获取)
device_udid_list = ['127.0.0.1:62001', '127.0.0.1:62025']


def appium_desired(udid, port):

    with open('../config/zxw_caps.yaml', 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_path = os.path.join(base_dir, 'app', data['appName'])

    desired_caps = {}
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid

    desired_caps['app'] = app_path
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('appium port on %s for %s at %s' % (port, udid, ctime()))
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub', desired_caps)
    driver.implicitly_wait(8)
    return driver
