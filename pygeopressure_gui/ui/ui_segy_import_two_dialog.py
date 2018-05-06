# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segy_import_two.ui'
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

class Ui_segy_import_two_Dialog(object):
    def setupUi(self, segy_import_two_Dialog):
        segy_import_two_Dialog.setObjectName(_fromUtf8("segy_import_two_Dialog"))
        segy_import_two_Dialog.resize(464, 210)
        self.file_label = QtGui.QLabel(segy_import_two_Dialog)
        self.file_label.setGeometry(QtCore.QRect(0, 0, 491, 22))
        self.file_label.setObjectName(_fromUtf8("file_label"))
        self.line = QtGui.QFrame(segy_import_two_Dialog)
        self.line.setGeometry(QtCore.QRect(0, 20, 451, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(segy_import_two_Dialog)
        self.label.setGeometry(QtCore.QRect(110, 30, 61, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(segy_import_two_Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 61, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(segy_import_two_Dialog)
        self.checkBox.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.lineEdit = QtGui.QLineEdit(segy_import_two_Dialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(180, 90, 80, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(segy_import_two_Dialog)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(264, 90, 80, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(segy_import_two_Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 61, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(segy_import_two_Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 120, 47, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.output_lineEdit = QtGui.QLineEdit(segy_import_two_Dialog)
        self.output_lineEdit.setGeometry(QtCore.QRect(180, 120, 201, 20))
        self.output_lineEdit.setText(_fromUtf8(""))
        self.output_lineEdit.setPlaceholderText(_fromUtf8(""))
        self.output_lineEdit.setObjectName(_fromUtf8("output_lineEdit"))
        self.indepth_checkBox = QtGui.QCheckBox(segy_import_two_Dialog)
        self.indepth_checkBox.setGeometry(QtCore.QRect(390, 120, 71, 20))
        self.indepth_checkBox.setObjectName(_fromUtf8("indepth_checkBox"))
        self.type_comboBox = QtGui.QComboBox(segy_import_two_Dialog)
        self.type_comboBox.setGeometry(QtCore.QRect(180, 150, 91, 20))
        self.type_comboBox.setObjectName(_fromUtf8("type_comboBox"))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.type_comboBox.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(segy_import_two_Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 150, 31, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.okButton = QtGui.QPushButton(segy_import_two_Dialog)
        self.okButton.setGeometry(QtCore.QRect(260, 180, 75, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.cancelButton = QtGui.QPushButton(segy_import_two_Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(350, 180, 75, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.groupBox = QtGui.QGroupBox(segy_import_two_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(180, 30, 221, 20))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 0, 111, 17))
        self.radioButton_2.setChecked(True)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(0, 0, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.groupBox_2 = QtGui.QGroupBox(segy_import_two_Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 60, 221, 20))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 0, 111, 17))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(0, 0, 82, 17))
        self.radioButton_4.setChecked(True)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))

        self.retranslateUi(segy_import_two_Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), segy_import_two_Dialog.close)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), segy_import_two_Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(segy_import_two_Dialog)

    def retranslateUi(self, segy_import_two_Dialog):
        segy_import_two_Dialog.setWindowTitle(_translate("segy_import_two_Dialog", "Import 3D Volume", None))
        self.file_label.setText(_translate("segy_import_two_Dialog", "TextLabel", None))
        self.label.setText(_translate("segy_import_two_Dialog", "Copy data", None))
        self.label_2.setText(_translate("segy_import_two_Dialog", "Null traces", None))
        self.checkBox.setText(_translate("segy_import_two_Dialog", "Scale values:", None))
        self.label_3.setText(_translate("segy_import_two_Dialog", "Shift/Factor", None))
        self.label_4.setText(_translate("segy_import_two_Dialog", "OUTPUT", None))
        self.indepth_checkBox.setText(_translate("segy_import_two_Dialog", "inDepth", None))
        self.type_comboBox.setItemText(0, _translate("segy_import_two_Dialog", "Reflection", None))
        self.type_comboBox.setItemText(1, _translate("segy_import_two_Dialog", "Velocity", None))
        self.type_comboBox.setItemText(2, _translate("segy_import_two_Dialog", "Density", None))
        self.type_comboBox.setItemText(3, _translate("segy_import_two_Dialog", "Pressure", None))
        self.label_5.setText(_translate("segy_import_two_Dialog", "Type", None))
        self.okButton.setText(_translate("segy_import_two_Dialog", "OK", None))
        self.cancelButton.setText(_translate("segy_import_two_Dialog", "Cancel", None))
        self.radioButton_2.setText(_translate("segy_import_two_Dialog", "No (scan&link)", None))
        self.radioButton.setText(_translate("segy_import_two_Dialog", "Yes (import)", None))
        self.radioButton_3.setText(_translate("segy_import_two_Dialog", "Pass", None))
        self.radioButton_4.setText(_translate("segy_import_two_Dialog", "Discard", None))

