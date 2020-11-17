from common.myunit import StartEnd
from businessView.loginView import LoginView
import logging
import unittest


class LoginTest(StartEnd):

    csv_file = '../data/account.csv'

    @unittest.skip('skip test_login_success_one')
    def test_login_success_one(self):
        logging.info('test_login_one')
        lo = LoginView(self.driver)

        user = lo.do_get_csv_data(self.csv_file, 1)
        lo.login_action(user[0], user[1])
        self.assertTrue(lo.assert_login_status())

    # @unittest.skip('skip test_login_failure')
    def test_login_failure(self):
        logging.info('test_login_failure')
        lo = LoginView(self.driver)

        user = lo.do_get_csv_data(self.csv_file, 2)
        lo.login_action(user[0], user[1])
        self.assertFalse(lo.assert_login_status(), msg='expect failure')
