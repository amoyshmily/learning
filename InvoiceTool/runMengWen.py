from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from InvoiceTool import MengWen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()

    ui = MengWen.Ui_MainWindow()
    ui.setupUi(mw)

    mw.show()
    sys.exit(app.exec_())
