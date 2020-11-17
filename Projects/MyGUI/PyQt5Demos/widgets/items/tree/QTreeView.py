"""
树控件(QTreeView)
2019-4-21 18:48:04

适用于MVC模式，系统提供了很多可选的model
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


class QTreeViewDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTreeViewDemo, self).__init__(parent)
        self.tree = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTreeView')
        self.resize(500, 400)

        # 实例化
        self.tree = QTreeView()
        model = QDirModel()

        self.tree.setModel(model)

        self.setCentralWidget(self.tree)


def main():
    app = QApplication(sys.argv)
    win = QTreeViewDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
