# -*- coding: utf-8 -*-
"""
a Seismic display widget based on mayavi

Created on Tue Jan 16 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from builtins import *

__author__ = "Yu Hao"

from PyQt4.QtGui import QGridLayout, QWidget

import pygeopressure as ppp

from pygeopressure_gui.widgets.matplotlib_widget import MatplotlibWidget


class MapView(QWidget):
    def __init__(self, parent=None):
        super(MapView, self).__init__()
        self.initUI()
        self.survey_setting = None

    def initUI(self):
        layout2 = QGridLayout(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout2.addWidget(self.matplotlib_widget)

    def draw_map(self, survey_setting):
        # fig = self.matplotlib_widget.fig
        self.survey_setting = survey_setting
        self.fig = self.matplotlib_widget.fig
        self.fig.clf()
        self.ax = self.fig.add_subplot(111)

        self.survey_setting.draw_survey_line(self.ax)
        self._draw_well_loc()

        # retaining aspect ratio when resizing
        self.ax.set_aspect(aspect='equal', anchor='C', adjustable='datalim')
        self.fig.tight_layout()

    def _draw_well_loc(self):
        pass
