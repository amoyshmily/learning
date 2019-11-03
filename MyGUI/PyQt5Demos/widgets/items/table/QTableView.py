"""
二维表（QTableView控件）
2019-5-11 18:03:28

MVC模式

"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class QTableViewDemo(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.table_view = QTableView()
        self.table_model = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableView控件')
        self.resize(500, 400)

        # 创建控件对象
        self.table_model = QStandardItemModel(4, 2)     # 数据模型对象
        self.table_model.setHorizontalHeaderLabels(['姓名', '年龄'])    # 表头

        # 将表控件与数据模型进行关联
        self.table_view.setModel(self.table_model)

        # 添加数据
        item00 = QStandardItem('张梦文')
        item01 = QStandardItem('18')
        self.table_model.setItem(0, 0, item00)
        self.table_model.setItem(0, 1, item01)

        # 绑定事件
        # self.list_widget.itemClicked.connect(self.clicked)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    win = QTableViewDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
