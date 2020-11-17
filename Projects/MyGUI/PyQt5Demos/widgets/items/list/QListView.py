"""
显示列表数据（QListView控件）
2019-4-21 17:24:01
"""
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
import sys


class ListViewDemo(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.list = ['item1', 'item2', 'item3']
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QListView控件')
        self.resize(300, 200)

        # 创建控件对象
        list_view = QListView()
        list_model = QStringListModel()

        # 设置数据模型
        list_model.setStringList(self.list)
        list_view.setModel(list_model)

        # 绑定事件
        list_view.clicked.connect(self.clicked)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(list_view)
        self.setLayout(layout)

    def clicked(self, item):
        QMessageBox.information(self, 'QListView', '您选择了'+self.list[item.row()])


def main():
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
