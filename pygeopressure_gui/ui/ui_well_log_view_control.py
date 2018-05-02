# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'well_log_view_control.ui'
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

class Ui_well_Log_View_Control(object):
    def setupUi(self, well_Log_View_Control):
        well_Log_View_Control.setObjectName(_fromUtf8("well_Log_View_Control"))
        well_Log_View_Control.resize(160, 434)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(well_Log_View_Control.sizePolicy().hasHeightForWidth())
        well_Log_View_Control.setSizePolicy(sizePolicy)
        well_Log_View_Control.setMinimumSize(QtCore.QSize(160, 0))
        well_Log_View_Control.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox = QtGui.QGroupBox(well_Log_View_Control)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 160, 489))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(160, 300))
        self.groupBox.setMaximumSize(QtCore.QSize(160, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.well_ComboBox = QtGui.QComboBox(self.groupBox)
        self.well_ComboBox.setGeometry(QtCore.QRect(10, 50, 141, 23))
        self.well_ComboBox.setObjectName(_fromUtf8("well_ComboBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 59, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.curve_listWidget = QtGui.QListWidget(self.groupBox)
        self.curve_listWidget.setGeometry(QtCore.QRect(10, 110, 141, 231))
        self.curve_listWidget.setObjectName(_fromUtf8("curve_listWidget"))

        self.retranslateUi(well_Log_View_Control)
        QtCore.QMetaObject.connectSlotsByName(well_Log_View_Control)

    def retranslateUi(self, well_Log_View_Control):
        well_Log_View_Control.setWindowTitle(_translate("well_Log_View_Control", "Form", None))
        self.groupBox.setTitle(_translate("well_Log_View_Control", "Control", None))
        self.label.setText(_translate("well_Log_View_Control", "Well", None))
        self.label_2.setText(_translate("well_Log_View_Control", "curve to display", None))

