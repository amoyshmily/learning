# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MengWen.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(653, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 601, 481))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 70, 81, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(140, 70, 231, 22))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(410, 40, 51, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("excel.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 120, 501, 261))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(20, 30, 451, 211))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtWidgets.QLabel(self.widget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.widget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 4, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 3, 4, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.widget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.widget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout.addWidget(self.comboBox_6, 4, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.widget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.widget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 1, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.widget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 2, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.widget)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 3, 2, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.widget)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 4, 2, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.widget)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 1, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.widget)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 2, 3, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.widget)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 3, 3, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.widget)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 4, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.widget)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 0, 5, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.widget)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 1, 5, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.widget)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 2, 5, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.widget)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 3, 5, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.widget)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 4, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setGeometry(QtCore.QRect(40, 30, 101, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_18.setGeometry(QtCore.QRect(140, 30, 231, 21))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 400, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 511, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_2.addWidget(self.lineEdit_11, 2, 1, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_2.addWidget(self.lineEdit_12, 2, 3, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_2.addWidget(self.lineEdit_10, 1, 3, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_2.addWidget(self.lineEdit_14, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 3, 2, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_2.addWidget(self.lineEdit_13, 3, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_2.addWidget(self.lineEdit_8, 0, 1, 1, 3)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_2.addWidget(self.lineEdit_16, 4, 1, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_2.addWidget(self.lineEdit_15, 4, 3, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 4, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 4, 2, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.layoutWidget)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 5, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_2.addWidget(self.lineEdit_19, 5, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.layoutWidget)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 5, 2, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_2.addWidget(self.lineEdit_17, 5, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(440, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 510, 601, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "公司名称"))
        self.groupBox.setTitle(_translate("MainWindow", "选择产品"))
        self.label_22.setText(_translate("MainWindow", "未开票总数"))
        self.label_19.setText(_translate("MainWindow", "应配："))
        self.label_4.setText(_translate("MainWindow", "产品1"))
        self.label_5.setText(_translate("MainWindow", "应配："))
        self.label_15.setText(_translate("MainWindow", "应配："))
        self.label_7.setText(_translate("MainWindow", "应配："))
        self.label_16.setText(_translate("MainWindow", "产品3"))
        self.label_6.setText(_translate("MainWindow", "产品2"))
        self.label_17.setText(_translate("MainWindow", "应配："))
        self.label_20.setText(_translate("MainWindow", "产品5"))
        self.label_18.setText(_translate("MainWindow", "产品4"))
        self.label_23.setText(_translate("MainWindow", "单价"))
        self.label_24.setText(_translate("MainWindow", "未开票总数"))
        self.label_25.setText(_translate("MainWindow", "未开票总数"))
        self.label_26.setText(_translate("MainWindow", "未开票总数"))
        self.label_28.setText(_translate("MainWindow", "未开票总数"))
        self.label_29.setText(_translate("MainWindow", "单价"))
        self.label_30.setText(_translate("MainWindow", "单价"))
        self.label_31.setText(_translate("MainWindow", "单价"))
        self.label_32.setText(_translate("MainWindow", "单价"))
        self.label_33.setText(_translate("MainWindow", "配数数量"))
        self.label_35.setText(_translate("MainWindow", "配数数量"))
        self.label_36.setText(_translate("MainWindow", "配数数量"))
        self.label_38.setText(_translate("MainWindow", "配数数量"))
        self.label_37.setText(_translate("MainWindow", "配数数量"))
        self.label_21.setText(_translate("MainWindow", "开票金额"))
        self.pushButton_2.setText(_translate("MainWindow", "开始匹配"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "导入匹配"))
        self.label_8.setText(_translate("MainWindow", "开票金额"))
        self.label_10.setText(_translate("MainWindow", "单价"))
        self.label_13.setText(_translate("MainWindow", "产品名称"))
        self.label_11.setText(_translate("MainWindow", "产品名称"))
        self.label_12.setText(_translate("MainWindow", "单价"))
        self.label_9.setText(_translate("MainWindow", "产品名称"))
        self.label_14.setText(_translate("MainWindow", "单价"))
        self.label_34.setText(_translate("MainWindow", "产品名称"))
        self.label_27.setText(_translate("MainWindow", "单价"))
        self.label_40.setText(_translate("MainWindow", "产品名称"))
        self.label_39.setText(_translate("MainWindow", "单价"))
        self.pushButton.setText(_translate("MainWindow", "开始计算"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "手工计算"))


