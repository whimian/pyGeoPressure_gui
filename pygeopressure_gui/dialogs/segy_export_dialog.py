# -*- coding: utf-8 -*-
"""
segy import dialog

Created on Sat May 8 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

import json
from pathlib2 import Path

from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QTableWidgetItem
from PyQt4 import uic
from PyQt4.QtCore import Qt, pyqtSlot, pyqtSignal

import pygeopressure as ppp

from pygeopressure_gui.ui.ui_segy_export_dialog import Ui_segy_export_Dialog
from pygeopressure_gui.config import CONF

from pygeopressure_gui.basic.utils import get_data_files

class SegyExportDialog(QDialog, Ui_segy_export_Dialog):
    def __init__(self):
        super(SegyExportDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.selectButton.clicked.connect(self.on_clicked_selectButton)
        # self.next_Button.clicked.connect(self.on_clicked_next_Button)

    def initUI(self):
        fnames = get_data_files(CONF.seismic_dir)
        self.input_cube_comboBox.addItems(fnames)

    @pyqtSlot()
    def on_clicked_selectButton(self):
        self.output_lineEdit.setText(str(
            QFileDialog.getSaveFileName(
                self, caption="Save Segy", filter="Segy Files (*.sgy *.segy)")))
        # segy_path = Path(self.file_path_lineEdit.text())
