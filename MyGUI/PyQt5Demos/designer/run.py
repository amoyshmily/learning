from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import test

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()

    ui = test.Ui_MainWindow()
    ui.setupUi(mw)

    mw.show()
    sys.exit(app.exec_())
