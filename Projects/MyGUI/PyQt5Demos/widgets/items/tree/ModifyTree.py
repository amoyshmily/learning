"""
修改节点
2019-4-21 18:47:17
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys


class ModifyTree(QWidget):

    def __init__(self, parent=None):
        super(ModifyTree, self).__init__(parent)
        self.tree = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('修改节点')
        self.resize(500, 400)

        # 添加按钮控件
        h_layout = QHBoxLayout()
        btn_add = QPushButton('添加节点')
        btn_delete = QPushButton('删除节点')
        btn_update = QPushButton('修改节点')

        # 组装按钮
        h_layout.addWidget(btn_add)
        h_layout.addWidget(btn_delete)
        h_layout.addWidget(btn_update)

        # 绑定事件
        btn_add.clicked.connect(self.addNode)
        btn_delete.clicked.connect(self.deleteNode)
        btn_update.clicked.connect(self.updateNode)

        # 创建树
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

        # 树控件的信号与槽
        self.tree.clicked.connect(self.onTreeClicked)

        # 展开所有节点
        self.tree.expandAll()

        # 设置布局
        main_layout = QVBoxLayout()
        main_layout.addLayout(h_layout)
        main_layout.addWidget(self.tree)
        self.setLayout(main_layout)

    def onTreeClicked(self, index):
        item = self.tree.currentItem()
        print(index.row())
        print('key={}, value={}'.format(item.text(0), item.text(1)))

    def addNode(self):
        print('添加子节点')
        current_item = self.tree.currentItem()

        # 动态添加节点
        new_node = QTreeWidgetItem(current_item)
        new_node.setText(0, '添加子节点')
        new_node.setText(1, '节点值')

    def deleteNode(self):
        print('删除节点')
        root = self.tree.invisibleRootItem()

        for node in self.tree.selectedItems():
            (node.parent() or root).removeChild(node)

    def updateNode(self):
        print('修改节点')
        current_node = self.tree.currentItem()
        current_node.setText(0, '此节点被修改了')
        current_node.setText(1, '修改后的值')


def main():
    app = QApplication(sys.argv)
    win = ModifyTree()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
