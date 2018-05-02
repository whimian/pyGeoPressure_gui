# -*- coding: utf-8 -*-
"""
Seismic data manager dialog

Created on Mon Apr 30 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import super

__author__ = "Yu Hao"

import json
from pathlib2 import Path

from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QListWidgetItem
from PyQt4 import uic
from PyQt4.QtCore import Qt

from pygeopressure_gui.ui.ui_seismic_manager import Ui_seismic_manager_Dialog
from pygeopressure_gui.config import CONF

class SeismicManagerDialog(QDialog, Ui_seismic_manager_Dialog):
    def __init__(self):
        # super(SurveySelectDialog, self).__init__()
        super().__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.data_list_Widget.itemSelectionChanged.connect(
            self.display_data_info)
        # self.surveyButton.clicked.connect(self.on_clicked_surveyButton)
        # self.selectButton.clicked.connect(self.on_clicked_selectButton)

    def initUI(self):
        self.load_data_list()

    def load_data_list(self):
        file_path = Path(CONF.data_root) / \
                    CONF.current_survey / "Seismics" / ".seismics"
        with open(str(file_path), "r") as fl:
            data_dict = json.load(fl)
            for name in data_dict.keys():
                # only initialize this way can it be set checkable
                new_item = QListWidgetItem(name, self.data_list_Widget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)

    def display_data_info(self):
        data_name = self.data_list_Widget.currentItem().text()
        file_path = Path(CONF.data_root) / \
                    CONF.current_survey / "Seismics" / ("."+ data_name)
        if file_path.exists():
            with open(str(file_path), "r") as fl:
                data_dict = json.load(fl)
                info_string = \
                    "In-line range: {} - {} - {}\n".format(
                        data_dict['inline_range'][0],
                        data_dict['inline_range'][1],
                        data_dict['inline_range'][2],) + \
                    "Cross-line range: {} - {} - {}\n".format(
                        data_dict['crline_range'][0],
                        data_dict['crline_range'][1],
                        data_dict['crline_range'][2]) + \
                    "Z range: {} - {} - {}\n".format(
                        data_dict['z_range'][0],
                        data_dict['z_range'][1],
                        data_dict['z_range'][2])
                self.seismic_info_textEdit.setPlainText(info_string)
