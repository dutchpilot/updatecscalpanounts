# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\YandexDisk\PRODUCTION\FTX\update cscalp amounts\gui\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 441)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/data/data/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.editPath = QtWidgets.QLineEdit(self.centralwidget)
        self.editPath.setObjectName("editPath")
        self.horizontalLayout_6.addWidget(self.editPath)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.editDepo = QtWidgets.QLineEdit(self.centralwidget)
        self.editDepo.setObjectName("editDepo")
        self.horizontalLayout_2.addWidget(self.editDepo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.editLeverage = QtWidgets.QLineEdit(self.centralwidget)
        self.editLeverage.setEnabled(True)
        self.editLeverage.setMaxLength(200)
        self.editLeverage.setObjectName("editLeverage")
        self.horizontalLayout_3.addWidget(self.editLeverage)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.editCode = QtWidgets.QLineEdit(self.centralwidget)
        self.editCode.setObjectName("editCode")
        self.horizontalLayout_4.addWidget(self.editCode)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayoutCurrency = QtWidgets.QHBoxLayout()
        self.horizontalLayoutCurrency.setObjectName("horizontalLayoutCurrency")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayoutCurrency.addWidget(self.label_10)
        self.comboBoxCurrency = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxCurrency.setObjectName("comboBoxCurrency")
        self.horizontalLayoutCurrency.addWidget(self.comboBoxCurrency)
        self.verticalLayout.addLayout(self.horizontalLayoutCurrency)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editPart1 = QtWidgets.QLineEdit(self.centralwidget)
        self.editPart1.setObjectName("editPart1")
        self.horizontalLayout.addWidget(self.editPart1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.editPart2 = QtWidgets.QLineEdit(self.centralwidget)
        self.editPart2.setObjectName("editPart2")
        self.horizontalLayout.addWidget(self.editPart2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.editPart3 = QtWidgets.QLineEdit(self.centralwidget)
        self.editPart3.setObjectName("editPart3")
        self.horizontalLayout.addWidget(self.editPart3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.editPart4 = QtWidgets.QLineEdit(self.centralwidget)
        self.editPart4.setObjectName("editPart4")
        self.horizontalLayout.addWidget(self.editPart4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.editPart5 = QtWidgets.QLineEdit(self.centralwidget)
        self.editPart5.setObjectName("editPart5")
        self.horizontalLayout.addWidget(self.editPart5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(0)
        self.tableWidget.verticalHeader().setDefaultSectionSize(26)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.pushButtonAbout = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonAbout.sizePolicy().hasHeightForWidth())
        self.pushButtonAbout.setSizePolicy(sizePolicy)
        self.pushButtonAbout.setObjectName("pushButtonAbout")
        self.horizontalLayout_5.addWidget(self.pushButtonAbout)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обновление рабочих объемов в CScalp"))
        self.label_11.setText(_translate("MainWindow", "Каталог CScalp"))
        self.label_7.setText(_translate("MainWindow", "Депозит в $"))
        self.label_8.setText(_translate("MainWindow", "Плечо"))
        self.label_9.setText(_translate("MainWindow", "Код подключения CScalp"))
        self.label_10.setText(_translate("MainWindow", "Базовая валюта"))
        self.label_6.setText(_translate("MainWindow", "Доли от максимального объема в %"))
        self.label.setText(_translate("MainWindow", "1"))
        self.label_2.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "3"))
        self.label_4.setText(_translate("MainWindow", "4"))
        self.label_5.setText(_translate("MainWindow", "5"))
        self.radioButton.setText(_translate("MainWindow", "Рассчитать объемы"))
        self.radioButton_2.setText(_translate("MainWindow", "Перенастроить стаканы"))
        self.pushButton.setText(_translate("MainWindow", "Обновить объемы в стаканах"))
        self.pushButtonAbout.setText(_translate("MainWindow", "?"))
import resources_rc