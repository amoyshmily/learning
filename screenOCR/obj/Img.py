import base64


class Img(object):

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.content = self.trans64()

    def trans64(self) -> str:
        """
        将本地图片进行Base64编码
        :return:Base64解码串
        """
        with open(self.file_name, 'rb') as f:
            base64_data = base64.b64encode(f.read())

        return base64_data.decode()


if __name__ == '__main__':
    img = Img('../img/1572512335.png')
    print(img.trans64())
