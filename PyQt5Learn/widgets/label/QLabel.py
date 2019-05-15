"""
标签（QLabel控件）
2019-4-23 00:08:13

常用方法：
setText():设置文本内容
setAlignment():设置文本对齐方式
setBuddy():设置伙伴关系
text():获取文本内容
selectedText():返回所选文字

常用的信号：
（1）鼠标飘过：linkHovered
（2）鼠标单击：linkActivated
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys


class QLabelDemo(QWidget):

    def __init__(self, parent=None):
        super(QLabelDemo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel控件')
        self.resize(500, 400)

        # 创建控件对象
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签</font>')    # 设置文本
        label1.setAutoFillBackground(True)  # 设置背景填充
        palette = QPalette()    # 调色板
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)     # 设置对齐方式

        label2.setText('<a href="#">欢迎使用PyQt</a>')

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')   # 设置提示信息
        label3.setPixmap(QPixmap('./img/python.png'))   # 设置图片

        label4.setText('<a href="www.baidu.com">百度一下</a>')
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')
        label4.setOpenExternalLinks(True)   # True表示使用浏览器打开链接，False表示调用槽函数

        # 绑定事件
        label2.linkHovered.connect(self.onHover)
        label4.linkActivated.connect(self.onClick)

        # 设置布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        self.setLayout(vbox)

    def onHover(self):
        print('当鼠标飘过label2时触发')

    def onClick(self):
        print('当鼠标单击label4时触发')


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = QLabelDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
