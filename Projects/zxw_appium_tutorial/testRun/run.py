import unittest
from BSTestRunner import BSTestRunner
import logging
import time
import sys


def cifer_run(test_pattern):
    """
    用例执行
    :param test_pattern:用例对象，支持模糊匹配，如*.py
    :return:
    """

    # CI集成时必须配置工程目录添加到系统环境中
    project_path = 'e:\\pyScript\\cifer'
    sys.path.append(project_path)

    test_dir = '../testCase'
    report_dir = '../reports'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern=test_pattern)

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + ' test_report.html'

    with open(report_name, 'wb') as file:
        runner = BSTestRunner(stream=file, title='kyb test report', description='kyb app test')
        logging.info('start test case')
        runner.run(discover)


if __name__ == '__main__':
    cifer_run('testLogin.py')
