from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys


class Demo(QMainWindow):

    def __init__(self):
        super(Demo, self).__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('test')
        self.show()


def main():
    app = QApplication(sys.argv)
    demo = Demo()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()