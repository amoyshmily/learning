"""
显示列表数据（QListView控件）
2019-4-21 17:24:01
"""
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys


class BasicTreeWidgetDemo(QMainWindow):

    def __init__(self, parent=None):
        super(BasicTreeWidgetDemo, self).__init__(parent)
        self.tree = QTreeWidget()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTreeWidget控件')
        self.resize(500, 400)

        # 指定列数
        self.tree.setColumnCount(2)

        # 指定列标签
        self.tree.setHeaderLabels(['key', 'value'])

        # 绑定事件
        self.tree.clicked.connect(self.clicked)

        # 根节点
        root = QTreeWidgetItem(self.tree)
        root.setText(0, '根')    # 设置文本
        root.setIcon(0, QIcon('root.png'))  # 设置图标
        self.tree.setColumnWidth(0, 220)    # 设置列宽

        # 添加子节点
        child1 = QTreeWidgetItem(root)
        child1.setText(0, '子节点1')
        child1.setText(1, '这是子节点1')
        child1.setIcon(0, QIcon('child1.png'))
        child1.setCheckState(0, Qt.Checked)     # 设置复选框

        # 添加子节点
        child2 = QTreeWidgetItem(root)
        child2.setText(0, '子节点2')
        child2.setText(1, '这是子节点2')
        child2.setIcon(0, QIcon('child2.png'))

        # 添加孙节点
        g_child = QTreeWidgetItem(child2)
        g_child.setText(0, '孙节点1')
        g_child.setText(1, '孙节点1的值')
        g_child.setIcon(0, QIcon('gChild.png'))

        # 展开所有节点
        self.tree.expandAll()

        self.setCentralWidget(self.tree)

    def clicked(self, item):
        pass


def main():
    app = QApplication(sys.argv)
    win = BasicTreeWidgetDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
