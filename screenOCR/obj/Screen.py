from pynput import mouse
from PIL import ImageGrab
import base64
from io import BytesIO
import time


class Screen(object):
    start_point = (0, 0)  # 起点坐标
    end_point = (0, 0)  # 终点坐标
    img_name = ''  # 图片名称

    def __init__(self):
        self.img_name = '%.0f' % time.time()


    def captureImage(self, need_save: bool = False) -> str:
        """
        获取图片
        :return:
        """

        # 开始捕捉屏幕区域
        self.__start_capture()

        # 获取图片对象
        captured_img = ImageGrab.grab((self.start_point[0], self.start_point[1], self.end_point[0], self.end_point[1]))

        if need_save is True:
            captured_img.save('../img/{}.png'.format(self.img_name))

        # 将图片转成Base64字串
        # 第一步：将Img对象转成bytes字节对象
        container = BytesIO()
        captured_img.save(container, format='PNG')
        img_bytes = container.getvalue()

        # 第二步：将字节转成Base64字串
        base64_data = base64.b64encode(img_bytes)

        return base64_data.decode()


    def __start_capture(self):
        """
        捕获屏幕区域
        :return:
        """

        print('---- 开始捕获屏幕 ------')

        with mouse.Listener(on_click=self.__my_click) as listener:
            listener.join()

        listener = mouse.Listener(on_click=self.__my_click)
        listener.start()

    def __my_click(self, x, y, button, pressed):
        """
        自定义鼠标监听事件
        :param x:
        :param y:
        :param button:
        :param pressed:
        :return:
        """
        if pressed:
            self.start_point = x, y
        else:
            self.end_point = x, y
            print('---- 结束捕获屏幕 ------')
            return False


if __name__ == '__main__':
    s = Screen()
    result = s.captureImage(need_save=True)
    print(result)
