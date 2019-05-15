import unittest
from common.desired_caps import appium_desired
import logging
from time import sleep


class StartEnd(unittest.TestCase):

    def setUp(self):
        logging.info('======SET UP======')
        self.driver = appium_desired('127.0.0.1:21503', 4725)

    def tearDown(self):
        logging.info('======TEAR DOWN======')
        sleep(5)
        self.driver.close_app()
