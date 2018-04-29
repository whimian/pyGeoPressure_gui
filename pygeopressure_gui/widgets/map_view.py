# -*- coding: utf-8 -*-
"""
a Seismic display widget based on mayavi

Created on Tue Jan 16 2018
"""
from __future__ import division, absolute_import, print_function
from __future__ import with_statement, unicode_literals
from builtins import *

from PyQt4.QtGui import QGridLayout, QWidget

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

        self._draw_survey_line()
        self._draw_well_loc()

        # retaining aspect ratio when resizing
        self.ax.set_aspect(aspect='equal', anchor='C', adjustable='datalim')
        self.fig.tight_layout()

    def _draw_survey_line(self):
        func = self.survey_setting.line_2_coord
        min_inline = self.survey_setting.startInline
        max_inline = self.survey_setting.endInline
        step_inline = self.survey_setting.stepInline
        if min_inline > max_inline:
            min_inline, max_inline = max_inline, min_inline
            step_inline = -step_inline

        min_crline = self.survey_setting.startCrline
        max_crline = self.survey_setting.endCrline
        step_crline = self.survey_setting.stepCrline
        if min_crline > max_crline:
            min_crline, max_crline = max_crline, min_crline
            step_crline = -step_crline

        for inl in range(min_inline, max_inline, step_inline):

            x_1, y_1 = func(inl, max_crline)
            x_2, y_2 = func(inl, min_crline)
            self.ax.plot([x_1, x_2],
                    [y_1, y_2], 'r', alpha=0.5, linewidth=0.1)

        for crl in range(min_crline, max_crline, step_crline):
            x_1, y_1 = func(min_inline, crl)
            x_2, y_2 = func(max_inline, crl)
            self.ax.plot([x_1, x_2],
                    [y_1, y_2], 'r', alpha=0.5, linewidth=0.1)
        self.ax.set(xlabel="X (Latitude)", ylabel="Y (Longitude)")

        x, y = func(min_inline, min_crline)
        self.ax.text(x, y, "{}/{}".format(min_inline, min_crline), color='blue')
        x, y = func(min_inline, max_crline)
        self.ax.text(x, y, "{}/{}".format(min_inline, max_crline), color='blue')
        x, y = func(max_inline, max_crline)
        self.ax.text(x, y, "{}/{}".format(max_inline, max_crline), color='blue')
        x, y = func(max_inline, min_crline)
        self.ax.text(x, y, "{}/{}".format(max_inline, min_crline), color='blue')

    def _draw_well_loc(self):
        pass
