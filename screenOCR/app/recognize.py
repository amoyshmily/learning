import requests
import jsonpath
from screenOCR.obj.Admin import Admin
from screenOCR.obj.Screen import Screen


def recognizeWords(api_token: str, img_64_str: str) -> list:
    """
    识别图片内容文本
    :param api_token:api鉴权令牌
    :param img_64_str:图片字串
    :return:
    """

    # 调用百度OCR进行识别
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token={}'.format(api_token)
    body = {'image': img_64_str}
    res = requests.post(url=url, data=body, verify=False)

    # 返回识别结果
    words = jsonpath.jsonpath(obj=res.json(), expr='$..words')
    return words if words else list()


if __name__ == '__main__':

    # 获取图片
    img_str = Screen().captureImage(need_save=True)

    # 鉴权（获取token)
    token = Admin().accessToken()

    print(recognizeWords(token, img_str))
