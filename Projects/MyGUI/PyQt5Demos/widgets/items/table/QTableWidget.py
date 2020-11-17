"""
二维表（QTableWidget控件）
2019-5-11 18:32:28

这是QTableView的子类
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class QTableWidgetDemo(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)

        self.table_widget = QTableWidget()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('QTableWidget控件')
        self.resize(500, 400)

        # 设置行数、列数
        self.table_widget.setRowCount(3)
        self.table_widget.setColumnCount(2)

        # 设置表头
        self.table_widget.setHorizontalHeaderLabels(['公司名称', '未开票合计'])

        # 添加数据
        item00 = QTableWidgetItem('顺丰科技顺丰科技顺丰科技顺丰科技顺丰科技')
        item01 = QTableWidgetItem('6666')
        item10 = QTableWidgetItem('丰驰畅行')
        item11 = QTableWidgetItem('5555')
        self.table_widget.setItem(0, 0, item00)
        self.table_widget.setItem(0, 1, item01)
        self.table_widget.setItem(1, 0, item10)
        self.table_widget.setItem(1, 1, item11)

        # 禁止编辑
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选中
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 内容自适应
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()

        # 控制表头的显示/隐藏
        self.table_widget.horizontalHeader().setVisible(True)
        self.table_widget.verticalHeader().setVisible(True)

        # 设置列头
        self.table_widget.setVerticalHeaderLabels(['a', 'b', 'c'])

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    win = QTableWidgetDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
