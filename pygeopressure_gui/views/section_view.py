# -*- coding: utf-8 -*-
"""
a Seismic section display widget based on matplotlib

Created on Tue Jan 16 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import super

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QWidget, QHBoxLayout, QGridLayout
from PyQt4 import uic, QtCore

from pygeopressure_gui.ui.ui_section_view_control import Ui_section_View_Control

from pygeopressure_gui.widgets.matplotlib_widget import MatplotlibWidget
from pygeopressure_gui.config import CONF


class SectionView(QWidget):
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
        # uic.loadUi('pygeopressure_gui/ui/survey_select.ui', self)
        layout = QHBoxLayout(self)
        self.control_widget = Section_View_Control(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout.addWidget(self.control_widget)
        layout.addWidget(self.matplotlib_widget)
        # layout.addWidget(self.control_widget)


class Section_View_Control(QWidget, Ui_section_View_Control):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
