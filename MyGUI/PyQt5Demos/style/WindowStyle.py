"""
窗口风格
2019-4-21 23:25:27
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class WindowStyle(QWidget):

    def __init__(self, parent=None):
        super(WindowStyle, self).__init__(parent)
        self.style_label = QLabel()
        self.style_combobox = QComboBox()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('窗口风格')
        self.resize(500, 200)

        # 实例化控件
        h_layout = QHBoxLayout()
        self.style_label = QLabel('设置窗口风格：')
        self.style_combobox.addItems(QStyleFactory.keys())

        # 获取当前窗口风格
        current_style = QApplication.style().objectName()
        print(current_style)

        index = self.style_combobox.findText(QApplication.style().objectName(), Qt.MatchFixedString)
        self.style_combobox.setCurrentIndex(index)

        # 绑定槽
        self.style_combobox.activated[str].connect(self.handleStyleChanged)

        # 设置布局
        h_layout.addWidget(self.style_label)
        h_layout.addWidget(self.style_combobox)
        self.setLayout(h_layout)

    def handleStyleChanged(self, style):
        QApplication.setStyle(style)
        print('当前选择的风格是：'+self.style_combobox.currentText())


def main():
    app = QApplication(sys.argv)
    win = WindowStyle()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
