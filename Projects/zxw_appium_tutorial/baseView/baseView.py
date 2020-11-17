
class BaseView(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        return self.driver.get_window_size()

    def swipe(self, start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def backward(self):
        return self.driver.press_keycode(4)

    def tap(self, positions, duration):
        return self.driver.tap(positions, duration)

    def get_screenshot_as_file(self, path):
        return self.driver.get_screenshot_as_file(path)





