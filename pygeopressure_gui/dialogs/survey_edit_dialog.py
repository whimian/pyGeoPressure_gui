# -*- coding: utf-8 -*-
"""
Survey info edit dialog

Created on Fri Jan 05 2018
"""
from __future__ import division, absolute_import, print_function
from __future__ import with_statement, unicode_literals

import sys
from os import path

from PyQt4.QtGui import QIcon, QMessageBox, QDialog, \
    QWidget, QFileDialog
from PyQt4 import uic

from ..basic.utils import read_survey_setting
from ..ui.ui_survey_edit import Ui_surveyEditDialog

__author__ = "Yu Hao"
__copyright__ = "Copyright (C) 2018 Yu Hao"

class SurveyEditDialog(QDialog, Ui_surveyEditDialog):
    def __init__(self):
        super(SurveyEditDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect events
        self.settingComboBox.currentIndexChanged.connect(self.from_file_event)

    def initUI(self):
        # uic.loadUi('pygeopressure_gui/ui/survey_edit.ui', self)
        self.setWindowIcon(QIcon(':/survey_icon.png'))
        self.settingComboBox.addItems(['Enter Below',
                                       'From File'])
        self.unitComboBox.addItems(['msec', 'm'])
        self.surveyNameLineEdit.setText("new")
        self.surveyNameLineEdit.selectAll()
        self.show()

    def from_file_event(self, event):
        if self.settingComboBox.currentText() == 'From File':
            file_dlg = QFileDialog(self)
            file_dlg.setFileMode(QFileDialog.ExistingFile)
            file_dlg.setOption(QFileDialog.ReadOnly, True)

            file_dlg.setNameFilters(["coordinates (*.json)"])
            file_dlg.selectNameFilter("coordinates (*.json)")
            file_dlg.setDefaultSuffix("png")

            if file_dlg.exec_():
                filenames = file_dlg.selectedFiles()
                read_survey_setting(filenames[0], self)
