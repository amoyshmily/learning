from selenium import webdriver
import time


def test():

    # 获取驱动对象
    driver = webdriver.Chrome('D:\Programs\ChromePortable\App\Google Chrome\chromedriver.exe')
    # 打开页面
    driver.get('E:\index.html')

    # xpath路径
    xpath_syntax = '//tbody[@id="busAssignmentDetailedList"]/tr'

    # 获取元素集合
    elements = driver.find_elements_by_xpath(xpath_syntax)
    for ele in elements:
        print("目标元素的id是："+ele.get_attribute("id"))  # 打印元素的id属性


if __name__ == '__main__':
    test()
