# -*- coding: utf-8 -*-
"""
segy import dialog 2

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
from PyQt4.QtCore import Qt, pyqtSlot

import pygeopressure as ppp

from pygeopressure_gui.ui.ui_segy_import_two_dialog import Ui_segy_import_two_Dialog
from pygeopressure_gui.config import CONF

class SegyImportTwoDialog(QDialog, Ui_segy_import_two_Dialog):
    def __init__(self, file_path, info_dict):
        super().__init__()
        self.setupUi(self)
        self.file_path = file_path
        self.info_from_parent = info_dict
        self.initUI()
        # connect
        self.okButton.clicked.connect(self.import_data)

    def initUI(self):
        self.file_label.setText(str(self.file_path))
        self.output_lineEdit.setText(str(self.file_path.stem))

    @pyqtSlot()
    def import_data(self):
        self.create_info_file()

    def create_info_file(self):
        info_file_path = Path(CONF.data_root) / CONF.current_survey / \
            "Seismics" / ".{}".format(self.output_lineEdit.text())
        info_dict = dict()
        info_dict["inDepth"] = True if self.indepth_checkBox.isChecked() \
            else False
        info_dict["Property_Type"] = self.type_comboBox.currentText()
        info_dict["path"] = str(self.file_path)
        info_dict["inline_range"] = self.info_from_parent["inline_range"]
        info_dict["crline_range"] = self.info_from_parent["crline_range"]
        info_dict["z_range"] = self.info_from_parent["z_range"]

        with open(str(info_file_path), "w") as fl:
            json.dump(info_dict, fl, indent=4)
