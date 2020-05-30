# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weatherwin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.okbth = QtWidgets.QPushButton(Form)
        self.okbth.setGeometry(QtCore.QRect(90, 320, 75, 23))
        self.okbth.setObjectName("okbth")
        self.querybth = QtWidgets.QPushButton(Form)
        self.querybth.setGeometry(QtCore.QRect(290, 320, 75, 23))
        self.querybth.setObjectName("querybth")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 221, 21))
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(100, 60, 258, 220))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.weatherComboBox = QtWidgets.QComboBox(self.widget)
        self.weatherComboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.weatherComboBox.setObjectName("weatherComboBox")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.weatherComboBox.addItem("")
        self.gridLayout.addWidget(self.weatherComboBox, 0, 1, 1, 1)
        self.resultText = QtWidgets.QTextBrowser(self.widget)
        self.resultText.setObjectName("resultText")
        self.gridLayout.addWidget(self.resultText, 1, 0, 1, 2)

        self.retranslateUi(Form)
        self.okbth.clicked.connect(Form.queryWeather)
        self.querybth.clicked.connect(Form.clearResult)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.okbth.setText(_translate("Form", "查询"))
        self.querybth.setText(_translate("Form", "清空"))
        self.label_2.setText(_translate("Form", "天气查询系统"))
        self.label.setText(_translate("Form", "城市"))
        self.weatherComboBox.setItemText(0, _translate("Form", "北京"))
        self.weatherComboBox.setItemText(1, _translate("Form", "上海"))
        self.weatherComboBox.setItemText(2, _translate("Form", "南阳"))
        self.weatherComboBox.setItemText(3, _translate("Form", "淅川"))
