# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'osdagpage.ui'
#
# Created: Wed Jun 17 15:52:50 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1352, 761)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.myListWidget = QtGui.QListWidget(self.centralwidget)
        self.myListWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.myListWidget.setStyleSheet(_fromUtf8("QListWidget::item {\n"
"  color:#00ff00;\n"
" background-color:#5930ac;\n"
"  }\n"
"QListWidget{background-color:#83AC30;\n"
"}\n"
" QListWidget:item:selected:active {\n"
"                                     background: #000000;}"))
        self.myListWidget.setFrameShape(QtGui.QFrame.Box)
        self.myListWidget.setFrameShadow(QtGui.QFrame.Raised)
        self.myListWidget.setLineWidth(5)
        self.myListWidget.setMidLineWidth(2)
        self.myListWidget.setIconSize(QtCore.QSize(48, 48))
        self.myListWidget.setSpacing(5)
        self.myListWidget.setObjectName(_fromUtf8("myListWidget"))
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.myListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/images (3).jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.myListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setIcon(icon)
        self.myListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setIcon(icon)
        self.myListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setIcon(icon)
        self.myListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setIcon(icon)
        self.myListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setIcon(icon)
        self.myListWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        item.setIcon(icon)
        self.myListWidget.addItem(item)
        self.gridLayout.addWidget(self.myListWidget, 0, 0, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet(_fromUtf8("QPushButton {background-color: #5930ac; color: #00ff00;}"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet(_fromUtf8("QPushButton {background-color: #5930ac; color: #00ff00;}\n"
"QPushButton:pressed { background-color: #000000 }"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.myStackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.myStackedWidget.setObjectName(_fromUtf8("myStackedWidget"))
        self.osdagPage = QtGui.QWidget()
        self.osdagPage.setObjectName(_fromUtf8("osdagPage"))
        self.label = QtGui.QLabel(self.osdagPage)
        self.label.setGeometry(QtCore.QRect(60, 100, 151, 131))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/cfd_logo.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.osdagPage)
        self.label_2.setGeometry(QtCore.QRect(240, 110, 461, 121))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/banner12.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.osdagPage)
        self.label_3.setGeometry(QtCore.QRect(670, 599, 91, 81))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/logo.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.osdagPage)
        self.label_5.setGeometry(QtCore.QRect(770, 600, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.myStackedWidget.addWidget(self.osdagPage)
        self.connectionPage = QtGui.QWidget()
        self.connectionPage.setObjectName(_fromUtf8("connectionPage"))
        self.gridLayout_2 = QtGui.QGridLayout(self.connectionPage)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.myTabWidget = QtGui.QTabWidget(self.connectionPage)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.myTabWidget.setFont(font)
        self.myTabWidget.setStyleSheet(_fromUtf8("QTabBar::tab { height: 30px; width: 200px; }\n"
""))
        self.myTabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.myTabWidget.setObjectName(_fromUtf8("myTabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.cleatRdBtn = QtGui.QRadioButton(self.tab)
        self.cleatRdBtn.setGeometry(QtCore.QRect(50, 110, 137, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cleatRdBtn.setFont(font)
        self.cleatRdBtn.setStyleSheet(_fromUtf8(""))
        self.cleatRdBtn.setObjectName(_fromUtf8("cleatRdBtn"))
        self.endPlateRdBtn = QtGui.QRadioButton(self.tab)
        self.endPlateRdBtn.setGeometry(QtCore.QRect(50, 150, 137, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.endPlateRdBtn.setFont(font)
        self.endPlateRdBtn.setObjectName(_fromUtf8("endPlateRdBtn"))
        self.finPlateRdBtn = QtGui.QRadioButton(self.tab)
        self.finPlateRdBtn.setGeometry(QtCore.QRect(50, 190, 137, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.finPlateRdBtn.setFont(font)
        self.finPlateRdBtn.setObjectName(_fromUtf8("finPlateRdBtn"))
        self.shearBtnStart = QtGui.QPushButton(self.tab)
        self.shearBtnStart.setGeometry(QtCore.QRect(430, 400, 186, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.shearBtnStart.setFont(font)
        self.shearBtnStart.setStyleSheet(_fromUtf8("QPushButton {\n"
"     color:#00ff00;\n"
" background-color:#5930ac;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: #00ff00;}\n"
"\n"
"QPushButton:pressed { background-color: #000000 }\n"
"   \n"
""))
        self.shearBtnStart.setObjectName(_fromUtf8("shearBtnStart"))
        self.seatedRdBtn = QtGui.QRadioButton(self.tab)
        self.seatedRdBtn.setGeometry(QtCore.QRect(50, 230, 137, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.seatedRdBtn.setFont(font)
        self.seatedRdBtn.setObjectName(_fromUtf8("seatedRdBtn"))
        self.myTabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.myTabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.myTabWidget, 0, 0, 1, 1)
        self.myStackedWidget.addWidget(self.connectionPage)
        self.tensionPage = QtGui.QWidget()
        self.tensionPage.setObjectName(_fromUtf8("tensionPage"))
        self.label_4 = QtGui.QLabel(self.tensionPage)
        self.label_4.setGeometry(QtCore.QRect(380, 240, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("QLabel{ color : #5930ac;}"))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.myStackedWidget.addWidget(self.tensionPage)
        self.gridLayout.addWidget(self.myStackedWidget, 0, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1352, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.myStackedWidget.setCurrentIndex(1)
        self.myTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        __sortingEnabled = self.myListWidget.isSortingEnabled()
        self.myListWidget.setSortingEnabled(False)
        item = self.myListWidget.item(0)
        item.setText(_translate("MainWindow", " Design:", None))
        item = self.myListWidget.item(1)
        item.setText(_translate("MainWindow", "Connection", None))
        item = self.myListWidget.item(2)
        item.setText(_translate("MainWindow", "Tension Member", None))
        item = self.myListWidget.item(3)
        item.setText(_translate("MainWindow", "Compression Member", None))
        item = self.myListWidget.item(4)
        item.setText(_translate("MainWindow", "Flexural Member", None))
        item = self.myListWidget.item(5)
        item.setText(_translate("MainWindow", "Beam-Column", None))
        item = self.myListWidget.item(6)
        item.setText(_translate("MainWindow", "Plate Girder", None))
        item = self.myListWidget.item(7)
        item.setText(_translate("MainWindow", "Gantry Girder", None))
        self.myListWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "Help", None))
        self.pushButton.setText(_translate("MainWindow", "Open File", None))
        self.label_5.setText(_translate("MainWindow", "Indian Institute of \n"
"Technology Bombay", None))
        self.cleatRdBtn.setText(_translate("MainWindow", "Cleat Angle", None))
        self.endPlateRdBtn.setText(_translate("MainWindow", "End Plate", None))
        self.finPlateRdBtn.setText(_translate("MainWindow", "Fin Plate", None))
        self.shearBtnStart.setText(_translate("MainWindow", "Start", None))
        self.seatedRdBtn.setText(_translate("MainWindow", "Seated", None))
        self.myTabWidget.setTabText(self.myTabWidget.indexOf(self.tab), _translate("MainWindow", "Shear Connection", None))
        self.myTabWidget.setTabText(self.myTabWidget.indexOf(self.tab_2), _translate("MainWindow", "Moment Connection", None))
        self.label_4.setText(_translate("MainWindow", "Coming soon!", None))

