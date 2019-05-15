"""
二维表（QTableWidget控件）
2019-5-11 18:32:28

这是QTableView的子类
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from InvoiceTool.SumHelper.calc import getClientInfoAll


class QTableWidgetDemo(QMainWindow):

    def __init__(self, parent=None):
        super(QTableWidgetDemo, self).__init__(parent)
        self.table_widget = QTableWidget()
        self.tool_bar = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('张梦文的小助手 v1.0')
        self.setWindowIcon(QIcon('invoice.png'))
        self.resize(600, 400)

        # ------ 设置菜单栏 ------
        source_file = self.menuBar().addMenu('&文件')
        open_action = QAction(QIcon('excel.png'), '打开文件', self)
        open_action.setShortcut('Ctrl+O')
        open_action.triggered.connect(self.showOpenFileChooser)
        source_file.addAction(open_action)

        # ------ 设置工具栏 ------
        # 打开文件
        tool_open = self.addToolBar('Open')
        tool_open_action = QAction(QIcon('excel.png'), '选择数据源Excel文件', self)
        tool_open_action.triggered.connect(self.showOpenFileChooser)
        tool_open.addAction(tool_open_action)
        # 导出文件
        tool_save = self.addToolBar('Save')
        tool_save_action = QAction(QIcon('save.png'), '保存文件', self)
        tool_save_action.triggered.connect(self.showSaveFileChooser)
        tool_save.addAction(tool_save_action)

        # ------ 设置状态栏 ------
        self.statusBar().showMessage('程序已准备就绪')

        # 设置行数、列数
        self.table_widget.setRowCount(1)
        self.table_widget.setColumnCount(2)
        item_default0 = QTableWidgetItem("请选择Excel数据源文件")
        item_default1 = QTableWidgetItem("0")
        self.table_widget.setItem(0, 0, item_default0)
        self.table_widget.setItem(0, 1, item_default1)

        # 设置表头
        self.table_widget.setHorizontalHeaderLabels(['公司名称', '未开票合计'])

        # 禁止编辑
        self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 整行选中
        # self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 内容自适应
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()

        # 控制表头的显示/隐藏
        self.table_widget.horizontalHeader().setVisible(True)
        self.table_widget.verticalHeader().setVisible(True)

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        self.setLayout(layout)
        self.setCentralWidget(self.table_widget)

    def reloadData(self, excel_file_name: str):
        """
        加载数据
        :param excel_file_name:
        :return:
        """
        print('正在加载数据....')
        data = getClientInfoAll(excel_file_name)
        print(data)

        # 重新设置行数
        row_num = self.getValidRowCount(data=data)
        self.table_widget.setRowCount(row_num)

        row_offset = 0
        for k in data.keys():

            client_name = data[k]['clientName']
            undo_total = data[k]['undoTotal']

            # 添加数据
            item0 = QTableWidgetItem(client_name)
            item1 = QTableWidgetItem(str(undo_total))

            # 如果未开票金额为0则不展示
            if undo_total:
                self.table_widget.setItem(row_offset, 0, item0)
                self.table_widget.setItem(row_offset, 1, item1)
            else:
                continue
            row_offset = row_offset+1

        # 内容自适应
        self.table_widget.resizeColumnsToContents()
        self.table_widget.resizeRowsToContents()

    @staticmethod
    def getValidRowCount(data: dict) -> int:
        """
        获取有效金额的行数
        :param data:数据
        :return:
        """
        count = 0
        for k in data.keys():
            if data[k]['undoTotal']:
                count = count+1
        return count

    def showOpenFileChooser(self):
        """
        打开文件对话框
        :return:
        """
        # TODO：过滤掉非excel的文件
        file_name = QFileDialog.getOpenFileName(self, '打开文件', 'd:/')

        if file_name[0]:
            self.statusBar().showMessage('数据加载中，请耐心等候......')
            self.reloadData(file_name[0])
            self.statusBar().showMessage('数据读取完毕！')

    def showSaveFileChooser(self):
        """
        保存文件对话框
        :return:
        """
        file_name = QFileDialog.getSaveFileName(self, '保存文件', 'd:/')
        if file_name[0]:
            # TODO:将记录写入csv文件
            with open(file_name[0], 'wb') as file:
                file.write('hello world'.encode(encoding='utf-8'))
            self.statusBar().showMessage('文件保存成功！')
        else:
            self.statusBar().showMessage('文件保存失败！')


def main():
    app = QApplication(sys.argv)
    win = QTableWidgetDemo()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
