# -*- coding: utf-8 -*-
"""
segy import dialog

Created on Sat May 5 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import super

__author__ = "Yu Hao"

import json
from pathlib2 import Path

from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QTableWidgetItem
from PyQt4 import uic
from PyQt4.QtCore import Qt, pyqtSlot, pyqtSignal

import pygeopressure as ppp

from pygeopressure_gui.ui.ui_segy_import_one_dialog import Ui_segy_import_one_Dialog
from pygeopressure_gui.dialogs.segy_import_two_dialog import SegyImportTwoDialog
from pygeopressure_gui.config import CONF

class SegyImportOneDialog(QDialog, Ui_segy_import_one_Dialog):

    data_imported = pyqtSignal()

    def __init__(self):
        super(SegyImportOneDialog, self).__init__()
        self.setupUi(self)
        # self.initUI()
        # connect
        self.selectButton.clicked.connect(self.on_clicked_selectButton)
        self.next_Button.clicked.connect(self.on_clicked_next_Button)

    @pyqtSlot()
    def on_clicked_selectButton(self):
        self.file_path_lineEdit.setText(str(
            QFileDialog.getOpenFileName(
                self, caption="Open Segy", filter="Segy Files (*.sgy *.segy)")))
        segy_path = Path(self.file_path_lineEdit.text())
        if segy_path.exists() is True:
            self.create_seis_object(str(segy_path))

    def create_seis_object(self, segy_path):
        seis_object = ppp.SeiSEGY(segy_path)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("1"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("1 - Floating point"))
        self.tableWidget.setItem(
            2, 0, QTableWidgetItem("{} ({} traces)".format(
                seis_object.survey_setting.nDepth,
                seis_object.survey_setting.nEast * \
                seis_object.survey_setting.nNorth)))
        self.tableWidget.setItem(
            3, 0, QTableWidgetItem("{} - {} (s or m)".format(
                seis_object.survey_setting.startDepth * 0.001,
                seis_object.survey_setting.endDepth * 0.001)))
        self.tableWidget.setItem(
            4, 0, QTableWidgetItem("{} - {}".format(
                seis_object.survey_setting.startInline,
                seis_object.survey_setting.endInline)))
        self.tableWidget.setItem(
            5, 0, QTableWidgetItem("{} - {}".format(
                seis_object.survey_setting.startCrline,
                seis_object.survey_setting.endCrline)))
        self.nsample_spinBox.setValue(seis_object.survey_setting.nDepth)
        self.start_lineEdit.setText(
            str(seis_object.survey_setting.startDepth * 0.001))
        self.step_lineEdit.setText(
            str(seis_object.survey_setting.stepDepth * 0.001))
        self.info_dict = {
            "inline_range": [
                seis_object.survey_setting.startInline,
                seis_object.survey_setting.endInline,
                seis_object.survey_setting.stepInline],
            "crline_range": [
                seis_object.survey_setting.startCrline,
                seis_object.survey_setting.endCrline,
                seis_object.survey_setting.stepCrline],
            "z_range": [
                float(seis_object.survey_setting.startDepth),
                float(seis_object.survey_setting.endDepth),
                float(seis_object.survey_setting.stepDepth)]
        }

    @pyqtSlot()
    def on_clicked_next_Button(self):
        segy_import_two_dialog = SegyImportTwoDialog(
            Path(self.file_path_lineEdit.text()), self.info_dict)
        segy_import_two_dialog.data_imported.connect(self.emit_signal)
        segy_import_two_dialog.exec_()

    @pyqtSlot()
    def emit_signal(self):
        self.data_imported.emit()
