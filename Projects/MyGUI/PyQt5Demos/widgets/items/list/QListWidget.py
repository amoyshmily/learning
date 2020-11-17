"""
扩展的列表控件（QListWidget控件）
2019-4-21 17:24:06

说明：QListView子类，增加了很多api
"""
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QMessageBox, QMainWindow
import sys


class ListWidgetDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.list_widget = QListWidget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QListWidget控件')
        self.resize(500, 400)

        # 创建控件对象

        # 添加数据
        self.list_widget.addItem('item1')
        self.list_widget.addItem('item2')
        self.list_widget.addItem('item3')

        # 绑定事件
        self.list_widget.itemClicked.connect(self.clicked)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

        self.setCentralWidget(self.list_widget)

    def clicked(self, index):
        QMessageBox.information(self, 'QListWidget', '您选择了'+self.list_widget.item(self.list_widget.row(index)).text())


def main():
    app = QApplication(sys.argv)
    win = ListWidgetDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
