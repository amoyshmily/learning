from common.myunit import StartEnd
from businessView.registerView import RegisterView
import logging


class RegisterTest(StartEnd):

    def test_user_register(self):
        logging.info('test_user_register')
        re = RegisterView(self.driver)

        register_info = re.get_random_register_info()
        username = register_info['username']
        password = register_info['password']
        email = register_info['email']

        re.register_action(username, password, email)
        self.assertTrue(re.assert_register_status())
