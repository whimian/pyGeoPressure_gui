# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seismic_manager.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_seismic_manager_Dialog(object):
    def setupUi(self, seismic_manager_Dialog):
        seismic_manager_Dialog.setObjectName(_fromUtf8("seismic_manager_Dialog"))
        seismic_manager_Dialog.resize(381, 430)
        self.data_list_Widget = QtGui.QListWidget(seismic_manager_Dialog)
        self.data_list_Widget.setGeometry(QtCore.QRect(10, 20, 281, 251))
        self.data_list_Widget.setObjectName(_fromUtf8("data_list_Widget"))
        self.seismic_info_textEdit = QtGui.QTextEdit(seismic_manager_Dialog)
        self.seismic_info_textEdit.setGeometry(QtCore.QRect(10, 280, 361, 111))
        self.seismic_info_textEdit.setObjectName(_fromUtf8("seismic_info_textEdit"))
        self.importButton = QtGui.QPushButton(seismic_manager_Dialog)
        self.importButton.setGeometry(QtCore.QRect(300, 20, 71, 22))
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.closeButton = QtGui.QPushButton(seismic_manager_Dialog)
        self.closeButton.setGeometry(QtCore.QRect(280, 400, 80, 22))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.deleteButton = QtGui.QPushButton(seismic_manager_Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(300, 200, 71, 22))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.pushButton_4 = QtGui.QPushButton(seismic_manager_Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 140, 71, 22))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(seismic_manager_Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 231, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.importButton_2 = QtGui.QPushButton(seismic_manager_Dialog)
        self.importButton_2.setGeometry(QtCore.QRect(300, 100, 71, 22))
        self.importButton_2.setObjectName(_fromUtf8("importButton_2"))

        self.retranslateUi(seismic_manager_Dialog)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), seismic_manager_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(seismic_manager_Dialog)

    def retranslateUi(self, seismic_manager_Dialog):
        seismic_manager_Dialog.setWindowTitle(_translate("seismic_manager_Dialog", "Seismic Data Manager", None))
        self.importButton.setText(_translate("seismic_manager_Dialog", "Import", None))
        self.closeButton.setText(_translate("seismic_manager_Dialog", "Close", None))
        self.deleteButton.setText(_translate("seismic_manager_Dialog", "Delete", None))
        self.pushButton_4.setText(_translate("seismic_manager_Dialog", "Copy", None))
        self.label.setText(_translate("seismic_manager_Dialog", "Seismic data in survey directory", None))
        self.importButton_2.setText(_translate("seismic_manager_Dialog", "Edit", None))

