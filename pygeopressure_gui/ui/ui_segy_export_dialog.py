# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segy_export.ui'
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

class Ui_segy_export_Dialog(object):
    def setupUi(self, segy_export_Dialog):
        segy_export_Dialog.setObjectName(_fromUtf8("segy_export_Dialog"))
        segy_export_Dialog.resize(430, 250)
        self.label_2 = QtGui.QLabel(segy_export_Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 61, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(segy_export_Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 70, 91, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.lineEdit = QtGui.QLineEdit(segy_export_Dialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 80, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(segy_export_Dialog)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(264, 70, 80, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(segy_export_Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 70, 61, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(segy_export_Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 190, 47, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.output_lineEdit = QtGui.QLineEdit(segy_export_Dialog)
        self.output_lineEdit.setGeometry(QtCore.QRect(180, 190, 171, 20))
        self.output_lineEdit.setText(_fromUtf8(""))
        self.output_lineEdit.setPlaceholderText(_fromUtf8(""))
        self.output_lineEdit.setObjectName(_fromUtf8("output_lineEdit"))
        self.type_comboBox = QtGui.QComboBox(segy_export_Dialog)
        self.type_comboBox.setGeometry(QtCore.QRect(180, 130, 131, 20))
        self.type_comboBox.setObjectName(_fromUtf8("type_comboBox"))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(segy_export_Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 130, 61, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.okButton = QtGui.QPushButton(segy_export_Dialog)
        self.okButton.setGeometry(QtCore.QRect(260, 220, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.cancelButton = QtGui.QPushButton(segy_export_Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(350, 220, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.groupBox_2 = QtGui.QGroupBox(segy_export_Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 40, 181, 20))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(70, 0, 51, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(0, 0, 82, 17))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_5.setGeometry(QtCore.QRect(130, 0, 51, 17))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.input_cube_comboBox = QtGui.QComboBox(segy_export_Dialog)
        self.input_cube_comboBox.setGeometry(QtCore.QRect(180, 10, 181, 20))
        self.input_cube_comboBox.setObjectName(_fromUtf8("input_cube_comboBox"))
        self.label_6 = QtGui.QLabel(segy_export_Dialog)
        self.label_6.setGeometry(QtCore.QRect(110, 10, 61, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.output_lineEdit_2 = QtGui.QLineEdit(segy_export_Dialog)
        self.output_lineEdit_2.setGeometry(QtCore.QRect(180, 160, 171, 20))
        self.output_lineEdit_2.setPlaceholderText(_fromUtf8(""))
        self.output_lineEdit_2.setObjectName(_fromUtf8("output_lineEdit_2"))
        self.label_7 = QtGui.QLabel(segy_export_Dialog)
        self.label_7.setGeometry(QtCore.QRect(106, 160, 61, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton = QtGui.QPushButton(segy_export_Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 160, 61, 20))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBox_2 = QtGui.QCheckBox(segy_export_Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(180, 100, 181, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.selectButton = QtGui.QPushButton(segy_export_Dialog)
        self.selectButton.setGeometry(QtCore.QRect(360, 190, 61, 20))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))

        self.retranslateUi(segy_export_Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), segy_export_Dialog.close)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), segy_export_Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(segy_export_Dialog)

    def retranslateUi(self, segy_export_Dialog):
        segy_export_Dialog.setWindowTitle(_translate("segy_export_Dialog", "Export SEG-Y", None))
        self.label_2.setText(_translate("segy_export_Dialog", "Null traces", None))
        self.checkBox.setText(_translate("segy_export_Dialog", "Scale values:", None))
        self.label_3.setText(_translate("segy_export_Dialog", "Shift/Factor", None))
        self.label_4.setText(_translate("segy_export_Dialog", "OUTPUT", None))
        self.type_comboBox.setItemText(0, _translate("segy_export_Dialog", "1 - Floating Point", None))
        self.type_comboBox.setItemText(1, _translate("segy_export_Dialog", "2 - Integer (32 bits)", None))
        self.type_comboBox.setItemText(2, _translate("segy_export_Dialog", "3 - Integer (16 bits)", None))
        self.type_comboBox.setItemText(3, _translate("segy_export_Dialog", "5 - IEEE Float (32 bits)", None))
        self.type_comboBox.setItemText(4, _translate("segy_export_Dialog", "8 - Signed char (8 bits)", None))
        self.label_5.setText(_translate("segy_export_Dialog", "Data format", None))
        self.okButton.setText(_translate("segy_export_Dialog", "OK", None))
        self.cancelButton.setText(_translate("segy_export_Dialog", "Cancel", None))
        self.radioButton_3.setText(_translate("segy_export_Dialog", "Pass", None))
        self.radioButton_4.setText(_translate("segy_export_Dialog", "Discard", None))
        self.radioButton_5.setText(_translate("segy_export_Dialog", "Add", None))
        self.label_6.setText(_translate("segy_export_Dialog", "Input Cube", None))
        self.output_lineEdit_2.setText(_translate("segy_export_Dialog", "<Generate>", None))
        self.label_7.setText(_translate("segy_export_Dialog", "Text header", None))
        self.pushButton.setText(_translate("segy_export_Dialog", "Define", None))
        self.checkBox_2.setText(_translate("segy_export_Dialog", "Adjust Z range to survey range", None))
        self.selectButton.setText(_translate("segy_export_Dialog", "Select", None))

