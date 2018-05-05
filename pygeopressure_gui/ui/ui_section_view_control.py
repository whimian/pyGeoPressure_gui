# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'section_view_control.ui'
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

class Ui_section_View_Control(object):
    def setupUi(self, section_View_Control):
        section_View_Control.setObjectName(_fromUtf8("section_View_Control"))
        section_View_Control.resize(163, 507)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(section_View_Control.sizePolicy().hasHeightForWidth())
        section_View_Control.setSizePolicy(sizePolicy)
        section_View_Control.setMinimumSize(QtCore.QSize(160, 300))
        self.groupBox = QtGui.QGroupBox(section_View_Control)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 160, 489))
        self.groupBox.setMinimumSize(QtCore.QSize(160, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.data_listWidget = QtGui.QListWidget(self.groupBox)
        self.data_listWidget.setGeometry(QtCore.QRect(10, 160, 141, 231))
        self.data_listWidget.setObjectName(_fromUtf8("data_listWidget"))
        self.inline_SpinBox = QtGui.QSpinBox(self.groupBox)
        self.inline_SpinBox.setGeometry(QtCore.QRect(30, 40, 91, 23))
        self.inline_SpinBox.setObjectName(_fromUtf8("inline_SpinBox"))
        self.crline_SpinBox = QtGui.QSpinBox(self.groupBox)
        self.crline_SpinBox.setEnabled(False)
        self.crline_SpinBox.setGeometry(QtCore.QRect(30, 90, 91, 23))
        self.crline_SpinBox.setObjectName(_fromUtf8("crline_SpinBox"))
        self.il_radioButton = QtGui.QRadioButton(self.groupBox)
        self.il_radioButton.setGeometry(QtCore.QRect(10, 20, 104, 21))
        self.il_radioButton.setChecked(True)
        self.il_radioButton.setObjectName(_fromUtf8("il_radioButton"))
        self.cl_radioButton = QtGui.QRadioButton(self.groupBox)
        self.cl_radioButton.setGeometry(QtCore.QRect(10, 70, 104, 21))
        self.cl_radioButton.setObjectName(_fromUtf8("cl_radioButton"))

        self.retranslateUi(section_View_Control)
        QtCore.QMetaObject.connectSlotsByName(section_View_Control)

    def retranslateUi(self, section_View_Control):
        section_View_Control.setWindowTitle(_translate("section_View_Control", "Form", None))
        self.groupBox.setTitle(_translate("section_View_Control", "control", None))
        self.label_2.setText(_translate("section_View_Control", "data to display", None))
        self.il_radioButton.setText(_translate("section_View_Control", "In-line", None))
        self.cl_radioButton.setText(_translate("section_View_Control", "Cross-line", None))

