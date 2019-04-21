import logging
import random
from time import sleep
from common.common_fn import Common, By, NoSuchElementException


class RegisterView(Common):

    register_text = (By.ID, 'com.tal.kaoyan:id/login_register_text')

    # 头像
    userheader = (By.ID, 'com.tal.kaoyan:id/activity_register_userheader')
    iv_picture = (By.ID, 'com.tal.kaoyan:id/iv_picture')
    picture_tv_ok = (By.ID, 'com.tal.kaoyan:id/picture_tv_ok')
    menu_crop = (By.ID, 'com.tal.kaoyan:id/menu_crop')

    # 用户名/密码/邮箱
    register_username = (By.ID, 'com.tal.kaoyan:id/activity_register_username_edittext')
    register_password = (By.ID, 'com.tal.kaoyan:id/activity_register_password_edittext')
    register_email = (By.ID, 'com.tal.kaoyan:id/activity_register_email_edittext')
    register_btn = (By.ID, 'com.tal.kaoyan:id/activity_register_register_btn')

    # 完善资料
    perfectinfomation_time = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_time')
    perfectinfomation_major = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_major')
    perfectinfomation_school = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_school')

    years = (By.ID, 'android:id/text1')
    subject_titles = (By.ID, 'com.tal.kaoyan:id/major_subject_title')
    group_titles = (By.ID, 'com.tal.kaoyan:id/major_group_title')
    search_items = (By.ID, 'com.tal.kaoyan:id/major_search_item_name')

    more_forum_titles = (By.ID, 'com.tal.kaoyan:id/more_forum_title')
    university_search_items = (By.ID, 'com.tal.kaoyan:id/university_search_item_name')

    goBtn = (By.ID, 'com.tal.kaoyan:id/activity_perfectinfomation_goBtn')

    button_mysefl = (By.ID, 'com.tal.kaoyan:id/mainactivity_button_mysefl')
    username = (By.ID, 'com.tal.kaoyan:id/activity_usercenter_username')

    def register_action(self, register_username, register_password, register_email):
        self.check_cancel_btn()
        self.check_skip_btn()

        logging.info('======register_action======')
        self.find_element(*self.register_text).click()

        logging.info('...setting user icon')
        self.find_element(*self.userheader).click()
        self.find_elements(*self.iv_picture)[7].click()
        self.find_element(*self.picture_tv_ok).click()
        self.find_element(*self.menu_crop).click()

        logging.info('...typing username: %s' % register_username)
        self.find_element(*self.register_username).send_keys(register_username)

        logging.info('...typing password: %s' % register_password)
        self.find_element(*self.register_password).send_keys(register_password)

        logging.info('...typing email: %s' % register_email)
        self.find_element(*self.register_email).send_keys(register_email)

        self.find_element(*self.register_btn).click()

        try:
            self.find_element(*self.perfectinfomation_school)
        except NoSuchElementException:
            logging.error('register failed!')
            self.do_snapshot('register_action')
            return False
        else:
            self.add_school_info()

    def add_school_info(self):
        logging.info('======add_register_info======')

        logging.info('...choosing year')
        self.find_element(*self.perfectinfomation_time).click()
        self.find_elements(*self.years)[1].click()

        logging.info('...choosing major')
        self.find_element(*self.perfectinfomation_major).click()
        self.find_elements(*self.subject_titles)[1].click()
        self.find_elements(*self.group_titles)[1].click()
        self.find_elements(*self.search_items)[1].click()

        logging.info('...choosing school')
        self.find_element(*self.perfectinfomation_school).click()
        self.tap([(112, 1076), (118, 1081)], 500)
        self.find_elements(*self.more_forum_titles)[2].click()
        self.find_elements(*self.university_search_items)[2].click()
        sleep(2)
        self.tap([(670, 950), (674, 954)], 500)

        self.find_element(*self.goBtn).click()

    def assert_register_status(self):
        logging.info('...checking register status')
        self.check_market_ad()

        try:
            self.find_element(*self.button_mysefl).click()
            self.find_element(*self.username)
        except NoSuchElementException:
            logging.error('fail to register')
            self.do_snapshot('check_register_status')
            return False
        else:
            logging.info('succeed in register')
            return True

    @staticmethod
    def get_random_register_info():
        logging.info('...generating random user info')

        user_info_dict = {}
        username = 'zxww2018'+'FLY'+str(random.randint(1000, 9000))
        password = 'zxww2018'+str(random.randint(1000, 9000))
        email = username+'@163.com'

        user_info_dict['username'] = username
        user_info_dict['password'] = password
        user_info_dict['email'] = email

        return user_info_dict
