# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pygeopressure.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1068, 628)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.DataTree = QtGui.QTreeWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataTree.sizePolicy().hasHeightForWidth())
        self.DataTree.setSizePolicy(sizePolicy)
        self.DataTree.setMinimumSize(QtCore.QSize(40, 0))
        self.DataTree.setMaximumSize(QtCore.QSize(252, 16777215))
        self.DataTree.setToolTip(_fromUtf8(""))
        self.DataTree.setObjectName(_fromUtf8("DataTree"))
        self.DataTree.headerItem().setText(0, _fromUtf8("1"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_seis = QtGui.QWidget()
        self.tab_seis.setObjectName(_fromUtf8("tab_seis"))
        self.tabWidget.addTab(self.tab_seis, _fromUtf8(""))
        self.toolBox = QtGui.QToolBox(self.splitter)
        self.toolBox.setMinimumSize(QtCore.QSize(250, 0))
        self.toolBox.setMaximumSize(QtCore.QSize(300, 16777215))
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_eaton = QtGui.QWidget()
        self.page_eaton.setEnabled(True)
        self.page_eaton.setGeometry(QtCore.QRect(0, 0, 300, 452))
        self.page_eaton.setAccessibleName(_fromUtf8(""))
        self.page_eaton.setObjectName(_fromUtf8("page_eaton"))
        self.gridLayoutWidget = QtGui.QWidget(self.page_eaton)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 241, 103))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.gridLayoutWidget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.comboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton)
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem)
        self.spinBox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBox)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.toolBox.addItem(self.page_eaton, _fromUtf8(""))
        self.page_bowers = QtGui.QWidget()
        self.page_bowers.setGeometry(QtCore.QRect(0, 0, 300, 452))
        self.page_bowers.setObjectName(_fromUtf8("page_bowers"))
        self.formLayoutWidget = QtGui.QWidget(self.page_bowers)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 241, 188))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.wellLabel = QtGui.QLabel(self.formLayoutWidget)
        self.wellLabel.setObjectName(_fromUtf8("wellLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.wellLabel)
        self.wellComboBox = QtGui.QComboBox(self.formLayoutWidget)
        self.wellComboBox.setObjectName(_fromUtf8("wellComboBox"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.wellComboBox)
        self.aLabel = QtGui.QLabel(self.formLayoutWidget)
        self.aLabel.setObjectName(_fromUtf8("aLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.aLabel)
        self.aLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.aLineEdit.setObjectName(_fromUtf8("aLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.aLineEdit)
        self.bLabel = QtGui.QLabel(self.formLayoutWidget)
        self.bLabel.setObjectName(_fromUtf8("bLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.bLabel)
        self.bLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.bLineEdit.setObjectName(_fromUtf8("bLineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.bLineEdit)
        self.uLabel = QtGui.QLabel(self.formLayoutWidget)
        self.uLabel.setObjectName(_fromUtf8("uLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.uLabel)
        self.uLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.uLineEdit.setObjectName(_fromUtf8("uLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.uLineEdit)
        self.vmaxLabel = QtGui.QLabel(self.formLayoutWidget)
        self.vmaxLabel.setObjectName(_fromUtf8("vmaxLabel"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.vmaxLabel)
        self.vmaxLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.vmaxLineEdit.setObjectName(_fromUtf8("vmaxLineEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.vmaxLineEdit)
        self.pushButton_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_2.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.toolBox.addItem(self.page_bowers, _fromUtf8(""))
        self.page_produce = QtGui.QWidget()
        self.page_produce.setGeometry(QtCore.QRect(0, 0, 300, 452))
        self.page_produce.setObjectName(_fromUtf8("page_produce"))
        self.toolBox.addItem(self.page_produce, _fromUtf8(""))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1068, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuData = QtGui.QMenu(self.menubar)
        self.menuData.setObjectName(_fromUtf8("menuData"))
        self.menuImport = QtGui.QMenu(self.menuData)
        self.menuImport.setObjectName(_fromUtf8("menuImport"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuSurvey = QtGui.QMenu(self.menubar)
        self.menuSurvey.setObjectName(_fromUtf8("menuSurvey"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setCheckable(False)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionOutput = QtGui.QAction(MainWindow)
        self.actionOutput.setObjectName(_fromUtf8("actionOutput"))
        self.actionWell_Log = QtGui.QAction(MainWindow)
        self.actionWell_Log.setObjectName(_fromUtf8("actionWell_Log"))
        self.actionSeismic = QtGui.QAction(MainWindow)
        self.actionSeismic.setObjectName(_fromUtf8("actionSeismic"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.action2D_Time = QtGui.QAction(MainWindow)
        self.action2D_Time.setObjectName(_fromUtf8("action2D_Time"))
        self.action3D_Time = QtGui.QAction(MainWindow)
        self.action3D_Time.setObjectName(_fromUtf8("action3D_Time"))
        self.action2D_Depth = QtGui.QAction(MainWindow)
        self.action2D_Depth.setObjectName(_fromUtf8("action2D_Depth"))
        self.action3D_Depth = QtGui.QAction(MainWindow)
        self.action3D_Depth.setObjectName(_fromUtf8("action3D_Depth"))
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionNewSurvey = QtGui.QAction(MainWindow)
        self.actionNewSurvey.setObjectName(_fromUtf8("actionNewSurvey"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionOpen_2 = QtGui.QAction(MainWindow)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.actionSelectSurvey = QtGui.QAction(MainWindow)
        self.actionSelectSurvey.setObjectName(_fromUtf8("actionSelectSurvey"))
        self.actionMapView = QtGui.QAction(MainWindow)
        self.actionMapView.setObjectName(_fromUtf8("actionMapView"))
        self.actionSectionView = QtGui.QAction(MainWindow)
        self.actionSectionView.setObjectName(_fromUtf8("actionSectionView"))
        self.actionManageSeismic = QtGui.QAction(MainWindow)
        self.actionManageSeismic.setObjectName(_fromUtf8("actionManageSeismic"))
        self.menuImport.addAction(self.actionWell_Log)
        self.menuData.addAction(self.menuImport.menuAction())
        self.menuData.addAction(self.actionOutput)
        self.menuData.addSeparator()
        self.menuData.addAction(self.actionManageSeismic)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menuWindow.addAction(self.action3D_Time)
        self.menuWindow.addAction(self.action3D_Depth)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionMapView)
        self.menuWindow.addAction(self.actionSectionView)
        self.menuSurvey.addAction(self.actionSelectSurvey)
        self.menuSurvey.addAction(self.actionNewSurvey)
        self.menuSurvey.addAction(self.actionOpen_2)
        self.menuSurvey.addSeparator()
        self.menuSurvey.addAction(self.actionExit)
        self.menubar.addAction(self.menuSurvey.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(2)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pyGeoPressure", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_seis), _translate("MainWindow", "Seismic 3D", None))
        self.label.setText(_translate("MainWindow", "Wells", None))
        self.pushButton.setText(_translate("MainWindow", "Calculate", None))
        self.label_2.setText(_translate("MainWindow", "N", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_eaton), _translate("MainWindow", "Eaton", None))
        self.wellLabel.setText(_translate("MainWindow", "Well", None))
        self.aLabel.setText(_translate("MainWindow", "a", None))
        self.bLabel.setText(_translate("MainWindow", "b", None))
        self.uLabel.setText(_translate("MainWindow", "U", None))
        self.vmaxLabel.setText(_translate("MainWindow", "Vmax", None))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_bowers), _translate("MainWindow", "Bowers", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_produce), _translate("MainWindow", "Production", None))
        self.menuData.setTitle(_translate("MainWindow", "Data", None))
        self.menuImport.setTitle(_translate("MainWindow", "Import", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Scene", None))
        self.menuSurvey.setTitle(_translate("MainWindow", "Survey", None))
        self.actionImport.setText(_translate("MainWindow", "Import", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionOutput.setText(_translate("MainWindow", "Output", None))
        self.actionWell_Log.setText(_translate("MainWindow", "Well Log", None))
        self.actionSeismic.setText(_translate("MainWindow", "Seismic", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.action2D_Time.setText(_translate("MainWindow", "2D - Time", None))
        self.action3D_Time.setText(_translate("MainWindow", "3D - Time", None))
        self.action2D_Depth.setText(_translate("MainWindow", "2D - Depth", None))
        self.action3D_Depth.setText(_translate("MainWindow", "3D - Depth", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionNewSurvey.setText(_translate("MainWindow", "New", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionOpen_2.setText(_translate("MainWindow", "Open", None))
        self.actionSelectSurvey.setText(_translate("MainWindow", "Select/Setup", None))
        self.actionMapView.setText(_translate("MainWindow", "Map view", None))
        self.actionSectionView.setText(_translate("MainWindow", "Section", None))
        self.actionManageSeismic.setText(_translate("MainWindow", "Seismic", None))

