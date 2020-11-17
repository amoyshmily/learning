"""
标签伙伴关系（QLabel控件）
2019-4-23 00:40:08

"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys


class QLabelBuddy(QDialog):

    def __init__(self, parent=None):
        super(QLabelBuddy, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel伙伴关系')
        self.resize(400, 200)

        # 创建控件对象
        name_label = QLabel('&Name', self)
        name_input = QLineEdit(self)
        password_label = QLabel('&Password', self)
        password_input = QLineEdit(self)
        btn_ok = QPushButton('&Ok')
        btn_cancel = QPushButton('&Cancel')

        # 设置伙伴关系
        name_label.setBuddy(name_input)
        password_label.setBuddy(password_input)

        # 设置布局
        layout = QGridLayout()
        layout.addWidget(name_label, 0, 0)
        layout.addWidget(name_input, 0, 1, 1, 2)    # （第几行，第几列，占几行，占几列）
        layout.addWidget(password_label, 1, 0)
        layout.addWidget(password_input, 1, 1, 1, 2)
        layout.addWidget(btn_ok, 2, 1)
        layout.addWidget(btn_cancel, 2, 2)

        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = QLabelBuddy()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
