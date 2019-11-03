"""
树节点的响应事件
2019-4-21 18:01:09
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


class TreeEvent(QMainWindow):

    def __init__(self, parent=None):
        super(TreeEvent, self).__init__(parent)
        self.tree = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('树节点的响应事件')
        self.resize(500, 400)

        # 实例化
        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)     # 指定列数
        self.tree.setHeaderLabels(['key', 'value'])     # 指定列标签

        # 根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根')    # 设置文本
        root.setIcon(0, QIcon('./img/root.png'))  # 设置图标
        self.tree.setColumnWidth(0, 220)    # 设置列宽

        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, 'child1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, 'child2')

        child3 = QTreeWidgetItem(child2)
        child3.setText(0, 'grand_child1')
        child3.setText(1, 'grand_child1')

        # 信号与槽
        self.tree.clicked.connect(self.onTreeClicked)

        # 展开所有节点
        self.tree.expandAll()

        self.setCentralWidget(self.tree)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key={}, value={}'.format(item.text(0), item.text(1)))


def main():
    app = QApplication(sys.argv)
    win = TreeEvent()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
