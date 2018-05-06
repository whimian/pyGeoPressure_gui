# -*- coding: utf-8 -*-
"""
Utility functions

Created on Thu Jan 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import int

__author__ = "Yu Hao"

import json

import pygeopressure as ppp


class DuplicateSurveyNameExeption(Exception):
    def __init__(self):
        self.message = ""
        super(DuplicateSurveyNameExeption, self).__init__(self.message)

# =============================================================================
def read_survey_setting(json_file, parent_window):
    "read survey settings into import window widgets"
    threepoint = ppp.ThreePoints(json_file)
    parent_window.a_inline_text.setText(str(threepoint.inline_A))
    parent_window.a_crline_text.setText(str(threepoint.crline_A))
    parent_window.b_inline_text.setText(str(threepoint.inline_B))
    parent_window.b_crline_text.setText(str(threepoint.crline_B))
    parent_window.c_inline_text.setText(str(threepoint.inline_C))
    parent_window.c_crline_text.setText(str(threepoint.crline_C))
    parent_window.a_x_text.setText(str(threepoint.east_A))
    parent_window.a_y_text.setText(str(threepoint.north_A))
    parent_window.b_x_text.setText(str(threepoint.east_B))
    parent_window.b_y_text.setText(str(threepoint.north_B))
    parent_window.c_x_text.setText(str(threepoint.east_C))
    parent_window.c_y_text.setText(str(threepoint.north_C))

    parent_window.inline_0_spinBox.setValue(int(threepoint.startInline))
    parent_window.inline_1_spinBox.setValue(int(threepoint.endInline))
    parent_window.inline_step_spinBox.setValue(int(threepoint.stepInline))

    parent_window.crline_0_spinBox.setValue(int(threepoint.startCrline))
    parent_window.crline_1_spinBox.setValue(int(threepoint.endCrline))
    parent_window.crline_step_spinBox.setValue(int(threepoint.stepCrline))

    parent_window.z_0_spinBox.setValue(int(threepoint.startDepth))
    parent_window.z_1_spinBox.setValue(int(threepoint.endDepth))
    parent_window.z_step_spinBox.setValue(int(threepoint.stepDepth))

def discern_setting_from_gui(parent_window):
    "read survey settings from window widgets as a dict"
    dict_survey = dict()
    dict_survey['name'] = parent_window.surveyNameLineEdit.text()
    dict_survey["point_A"] = [
        int(parent_window.a_inline_text.text()),
        int(parent_window.a_crline_text.text()),
        float(parent_window.a_x_text.text()),
        float(parent_window.a_y_text.text())]
    dict_survey["point_B"] = [
        int(parent_window.b_inline_text.text()),
        int(parent_window.b_crline_text.text()),
        float(parent_window.b_x_text.text()),
        float(parent_window.b_y_text.text())]
    dict_survey["point_C"] = [
        int(parent_window.c_inline_text.text()),
        int(parent_window.c_crline_text.text()),
        float(parent_window.c_x_text.text()),
        float(parent_window.c_y_text.text())]
    dict_survey["inline_range"] = [
        parent_window.inline_0_spinBox.value(),
        parent_window.inline_1_spinBox.value(),
        parent_window.inline_step_spinBox.value()
    ],
    dict_survey["crline_range"] = [
        parent_window.crline_0_spinBox.value(),
        parent_window.crline_1_spinBox.value(),
        parent_window.crline_step_spinBox.value()
    ],
    dict_survey["z_range"] = [
        parent_window.z_0_spinBox.value(),
        parent_window.z_1_spinBox.value(),
        parent_window.z_step_spinBox.value(),
        parent_window.unitComboBox.currentText()
    ]
    # it's a bug of pyqt4
    if isinstance(dict_survey['inline_range'], tuple):
        dict_survey['inline_range'] = dict_survey['inline_range'][0]
        dict_survey['crline_range'] = dict_survey['crline_range'][0]
        # dict_survey['z_range'] = dict_survey['z_range'][0]
    return dict_survey

def create_survey_directory(root_dir, survey_name):
    """
    Create survey folder structure

    Parameters
    ----------
    root_dir : Path
        Root directory for storing surveys
    survey_nam : str
    """
    survey_root = root_dir / survey_name
    try:
        survey_root.mkdir()
        dir_to_create = [root_dir / survey_name / 'Seismics',
                         root_dir / survey_name / 'Wellinfo',
                         root_dir / survey_name / 'Surfaces']
        for directory in dir_to_create:
            directory.mkdir()
        # new folder structure does not require folder dot file
        #     file_path = directory / ".{}".format(str(directory.name).lower())
        #     file_path.touch()
        return survey_root
    except WindowsError:
        raise DuplicateSurveyNameExeption()

def write_survey_file(path_file, survey_dict):
    file_to_write = path_file
    with open(str(file_to_write), "w") as fl:
        json.dump(survey_dict, fl, indent=4)

def create_survey_info_file(survey_root, parent_window):
    """"""
    survey_dict = {
        "name": "F3",
        "inline_range": [int(parent_window.inline_0_spinBox.value),
                         int(parent_window.inline_1_spinBox.value),
                         int(parent_window.inline_step_spinBox.value)],
        "crline_range": [int(parent_window.crline_0_spinBox.value),
                         int(parent_window.crline_1_spinBox.value),
                         int(parent_window.crline_step_spinBox.value)],
        "z_range": [int(parent_window.z_0_spinBox.value),
                    int(parent_window.z_1_spinBox.value),
                    int(parent_window.z_step_spinBox.value),
                    "T"],#!!!!!!!!!!!!!!!!!!!!!!
        "point_A": [int(parent_window.a_inline_text.text),
                    int(parent_window.a_crline_text.text),
                    float(parent_window.a_x_text.text),
                    float(parent_window.a_y_text.text)],
        "point_B": [int(parent_window.b_inline_text.text),
                    int(parent_window.b_crline_text.text),
                    float(parent_window.b_x_text.text),
                    float(parent_window.b_y_text.text)],
        "point_C": [int(parent_window.c_inline_text.text),
                    int(parent_window.c_crline_text.text),
                    float(parent_window.c_x_text.text),
                    float(parent_window.c_y_text.text)]
    }
    survey_file = survey_root.joinpath('.survey')
    with survey_file.open('w') as wf:
        json.dump(survey_dict, wf, indent=4)

# =============================================================================
def get_available_survey_dir(data_root):
    """
    data_root : Path
    """
    dnames = list()
    for folder in data_root.glob("*/"):
        if list(folder.glob('*.survey')):
            dnames.append(folder.stem)
    return dnames

def get_data_files(dir_path):
    """
    get all dot file with given path

    dir_path: Path
    """
    fnames = list()
    # dir_path = Path(dir_path)
    if dir_path.exists():
        if list(dir_path.glob('.*')):
            for item in list(dir_path.glob('.*')):
                fnames.append(item.name[1:])
    return fnames
