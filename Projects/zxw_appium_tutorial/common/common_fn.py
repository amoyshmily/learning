from baseView.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time
import os
import csv


class Common(BaseView):

    wemedia_cacel = (By.ID, 'com.tal.kaoyan:id/view_wemedia_cacel')
    cancel_btn = (By.ID, 'android:id/button2')
    skip_btn = (By.ID, 'com.tal.kaoyan:id/tv_skip')
    now_time = None

    def check_cancel_btn(self):
        logging.info('======check cancelBtn======')
        try:
            cancel_btn = self.driver.find_element(*self.cancel_btn)
        except NoSuchElementException:
            logging.info('no cancelBtn')
        else:
            cancel_btn.click()

    def check_skip_btn(self):
        logging.info('======check skipBtn======')
        try:
            skip_btn = self.driver.find_element(*self.skip_btn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skip_btn.click()

    def check_market_ad(self):
        logging.info('======check_market_ad======')
        try:
            text_cancel_ad = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            logging.info('ad not appeared')
        else:
            logging.info('close market ad')
            text_cancel_ad.click()

    def do_get_size(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return x, y

    def do_swipe_left(self):
        size = self.do_get_size()
        x1 = int(size[0] * 0.9)
        x2 = int(size[0] * 0.1)
        y = int(size[1] * 0.5)
        self.swipe(x1, y, x2, y, 1000)

    def do_get_time(self):
        self.now_time = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now_time

    def do_snapshot(self, module):
        now_time = self.do_get_time()
        base_path = os.path.dirname(os.path.dirname(__file__))
        image_file = base_path+'/screenshots/%s_%s.png' % (module, now_time)

        self.get_screenshot_as_file(image_file)

    @staticmethod
    def do_get_csv_data(csv_file, line):
        """
        获取CSV文件制定行的数据
        :param csv_file:csv文件路径
        :param line:数据所在行数
        :return:
        """
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader, 1):
                if index == line:
                    return row
