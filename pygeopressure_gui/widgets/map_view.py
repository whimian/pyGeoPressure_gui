# -*- coding: utf-8 -*-
"""
a Seismic display widget based on mayavi

Created on Tue Jan 16 2018
"""
from __future__ import division, absolute_import, print_function
from __future__ import with_statement, unicode_literals
from builtins import range

import random

from pyface.qt.QtGui import QGridLayout, QWidget

from pygeopressure_gui.widgets.well_log_widget import MatplotlibWidget


class MapView(QWidget):
    def __init__(self, parent=None):
        super(MapView, self).__init__()
        self.initUI()

    def initUI(self):
        layout2 = QGridLayout(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout2.addWidget(self.matplotlib_widget)

    def draw_map(self, survey_setting):
        fig = self.matplotlib_widget.fig
        fig.add_subplot(111)
        ax = fig.get_axes()[0]
        inline_step = survey_setting.stepInline if \
            survey_setting.startInline < survey_setting.endInline else \
            -survey_setting.stepInline
        inline_step *= 1
        step1 = 1 if \
            survey_setting.startInline < survey_setting.endInline else \
            -1
        max_crline = survey_setting.endCrline
        min_crline = survey_setting.startCrline
        for inl in range(survey_setting.startInline,
            survey_setting.endInline+step1, inline_step):
            x_1, y_1 = survey_setting.line_2_coord(inl, max_crline)
            x_2, y_2 = survey_setting.line_2_coord(inl, min_crline)
            ax.plot([x_1, x_2],
                    [y_1, y_2], 'r', alpha=0.5, linewidth=0.1)
        crline_step = survey_setting.stepCrline if \
            survey_setting.startCrline < survey_setting.endCrline else \
            -survey_setting.stepCrline
        crline_step *= 1
        step2 = 1 if \
            survey_setting.startCrline < survey_setting.endCrline else \
            -1
        max_inline = survey_setting.endInline
        min_inline = survey_setting.startInline
        for crl in range(survey_setting.startCrline,
            survey_setting.endCrline+step2, crline_step):
            x_1, y_1 = survey_setting.line_2_coord(min_inline, crl)
            x_2, y_2 = survey_setting.line_2_coord(max_inline, crl)
            ax.plot([x_1, x_2],
                    [y_1, y_2], 'r', alpha=0.5, linewidth=0.1)
        ax.set(xlabel="X", ylabel="Y")
