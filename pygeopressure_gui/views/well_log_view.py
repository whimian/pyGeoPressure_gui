# -*- coding: utf-8 -*-
"""
a Well log display widget based on matplotlib

Created on Tue May 2nd 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import super

__author__ ="Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QWidget, QHBoxLayout, QGridLayout
from PyQt4 import uic, QtCore

from pygeopressure_gui.ui.ui_well_log_view_control import Ui_well_Log_View_Control

from pygeopressure_gui.widgets.matplotlib_widget import MatplotlibWidget
from pygeopressure_gui.config import CONF


class WellLogView(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        # self.setupUi(self)
        self.initUI()
        # connect
        # self.surveyListWidget.itemSelectionChanged.connect(
        #     self.display_map_and_info)
        # self.surveyButton.clicked.connect(self.on_clicked_surveyButton)
        # self.selectButton.clicked.connect(self.on_clicked_selectButton)

        # self.load_survey_list()

    def initUI(self):
        layout = QHBoxLayout(self)
        self.control_widget = Well_Log_View_Control(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout.addWidget(self.control_widget)
        layout.addWidget(self.matplotlib_widget)


class Well_Log_View_Control(QWidget, Ui_well_Log_View_Control):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
