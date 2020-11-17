import logging
from common.common_fn import Common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginView(Common):

    username_type = (By.ID, 'com.tal.kaoyan:id/login_email_edittext')
    password_type = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    loginBtn = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    tip_commit = (By.ID, 'com.tal.kaoyan:id/tip_commit')
    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenter_username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    right_button = (By.ID, 'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logout_btn = (By.ID, 'com.tal.kaoyan:id/setting_logout_text')

    def login_action(self, username, password):
        self.check_cancel_btn()
        self.check_skip_btn()

        logging.info('======login_action======')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('======login finished!======')

    def check_account_alert(self):
        # 异地登录提醒弹窗
        logging.info('======check_account_alert======')
        try:
            element = self.driver.find_element(*self.tip_commit)
        except NoSuchElementException:
            pass
        else:
            logging.info('close tip_commit')
            element.click()

    def assert_login_status(self):
        logging.info('======check_login_status======')
        self.check_market_ad()
        self.check_account_alert()

        try:
            self.find_element(*self.button_mysefl).click()
            self.find_element(*self.usercenter_username)
        except NoSuchElementException:
            logging.error('login failed')
            self.do_snapshot('login failed')
            return False
        else:
            logging.info('login success!')
            return True

    def logout_action(self):
        logging.info('======logout_action======')
        self.find_element(*self.right_button).click()
        self.find_element(*self.logout_btn).click()
        self.find_element(*self.tip_commit).click()
