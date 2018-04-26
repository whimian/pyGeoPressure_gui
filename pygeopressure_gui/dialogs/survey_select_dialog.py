# -*- coding: utf-8 -*-
"""
A survey setting class

Created on Sat Jan 20 2018
"""
from __future__ import division, absolute_import, print_function
from __future__ import with_statement, unicode_literals

from pathlib2 import Path
from PyQt4.QtGui import QIcon, QDialog, QFileDialog
from PyQt4 import uic

from ..basic.utils import get_available_survey_dir
from ..basic.survey_setting import SurveySetting
from ..widgets.survey_map_widget import SurveyMap
from ..ui.ui_survey_select import Ui_surveySelectDialog

from .. import DATA_ROOT

__author__ = "yuhao"
__copyright__ = "Copyright (C) 2018 Yu Hao"


class SurveySelectDialog(QDialog, Ui_surveySelectDialog):
    def __init__(self):
        super(SurveySelectDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.surveyButton.clicked.connect(self.selectDataRootEvent)
        # connect events
        self.surveyListWidget.itemSelectionChanged.connect(
            self.display_map_and_info)

    def initUI(self):
        # uic.loadUi('pygeopressure_gui/ui/survey_select.ui', self)
        self.setWindowIcon(QIcon(':/survey_icon.png'))
        self.survey_map = SurveyMap(self)
        self.gridLayout.addWidget(self.survey_map)
        self.show()

    def selectDataRootEvent(self, event):
        # set new DATA_ROOT
        global DATA_ROOT
        DATA_ROOT = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        # display DATA_ROOT
        self.dataRootLabel.setText(DATA_ROOT)
        # populate surveylist
        dnames = get_available_survey_dir(Path(DATA_ROOT))
        self.surveyListWidget.clear()
        self.surveyListWidget.addItems(dnames)

    def display_map_and_info(self):
        # get survey file path
        survey_folder = str(self.surveyListWidget.selectedItems()[0].text())
        global DATA_ROOT
        survey_file = Path(DATA_ROOT, survey_folder, '.survey')
        # create new survey
        new_survey = SurveySetting(survey_file)
        # build survey info string for display
        info_string = \
            "In-line range: {} - {} - {}\n".format(
                new_survey.startInline,
                new_survey.endInline,
                new_survey.stepInline) + \
            "Cross-line range: {} - {} - {}\n".format(
                new_survey.startCrline,
                new_survey.endCrline,
                new_survey.stepCrline) + \
            "Z range({}): {} - {} - {}\n".format(
                new_survey.startDepth,
                new_survey.endDepth,
                new_survey.stepDepth,
                new_survey.zType) + \
            "Inl/Crl bin size (m/line): {}/{}\n".format(
                new_survey.inline_bin,
                new_survey.crline_bin) + \
            "Area (sq km): {}; Survey type: Only 3D\n".format(
                new_survey.area) + \
            "In-line Orientation: {:.2f} Degrees from N\n".format(
                new_survey.azimuth) + \
            "Location: {}".format(str(Path(DATA_ROOT, survey_folder)))
        self.surveyInfoTextEdit.setPlainText(info_string)
        # draw survey area plot
        inlines = [new_survey.startInline, new_survey.startInline,
                   new_survey.endInline, new_survey.endInline]
        crlines = [new_survey.startCrline, new_survey.endCrline,
                   new_survey.endCrline, new_survey.startCrline]
        x_c, y_c = new_survey.four_corner_on_canvas(
            self.survey_map.width(), self.survey_map.height())
        self.survey_map.inlines = inlines
        self.survey_map.crlines = crlines
        self.survey_map.x_canvas = x_c
        self.survey_map.y_canvas = y_c
        self.survey_map.repaint()
