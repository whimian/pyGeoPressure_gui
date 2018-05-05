# -*- coding: utf-8 -*-
"""
a Seismic section display widget based on matplotlib

Created on Tue Jan 16 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
# from future.builtins import super

__author__ = "Yu Hao"

import json

from pathlib2 import Path
from PyQt4.QtGui import QWidget, QHBoxLayout, QListWidgetItem
from PyQt4 import uic, QtCore

import pygeopressure as ppp

from pygeopressure_gui.ui.ui_section_view_control import Ui_section_View_Control
from pygeopressure_gui.widgets.matplotlib_widget import MatplotlibWidget
from pygeopressure_gui.config import CONF


class SectionView(QWidget):

    status = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(SectionView, self).__init__()
        self.initUI()
        # connect
        self.control_widget.il_radioButton.toggled.connect(self.radioButton_check_changed)
        self.control_widget.cl_radioButton.toggled.connect(self.radioButton_check_changed)
        self.control_widget.inline_SpinBox.valueChanged.connect(self.plot_section)
        self.control_widget.crline_SpinBox.valueChanged.connect(self.plot_section)

    def initUI(self):
        # uic.loadUi('pygeopressure_gui/ui/survey_select.ui', self)
        layout = QHBoxLayout(self)
        self.control_widget = Section_View_Control(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout.addWidget(self.control_widget)
        layout.addWidget(self.matplotlib_widget)
        # layout.addWidget(self.control_widget)

    def plot_section(self):
        # self.matplotlib_widget.fig.clf()
        ax = self.matplotlib_widget.axes
        ax.cla()
        for idx in range(self.control_widget.data_listWidget.count()):
        # for data_item in self.control_widget.data_listWidget.items:
            item = self.control_widget.data_listWidget.item(idx)
            if self.control_widget.il_radioButton.isChecked() is True:
                if item.checkState() == QtCore.Qt.Checked:
                    data_path = Path(CONF.data_root) / CONF.current_survey / "Seismics" / ".{}".format(item.text())
                    if data_path.exists() is True:
                        if not hasattr(self, "data_{}".format(item.text())):
                            # check if data has already been loaded
                            # create new seis object if not
                            self.new_seis_object(item.text())
                        self.status.emit("Reading data ...")
                        seis_object = getattr(self, "data_{}".format(item.text()))
                        self.status.emit("Plotting ...")
                        seis_object.plot(ppp.InlineIndex(self.control_widget.inline_SpinBox.value()), ax)
                        self.matplotlib_widget.fig.canvas.draw()
                        self.status.emit("")
                    else:
                        self.statusBar().showMessage("can not find data file {}".format(item.text))

            elif self.control_widget.cl_radioButton.isChecked() is True:
                if item.checkState() == QtCore.Qt.Checked:
                    data_path = Path(CONF.data_root) / CONF.current_survey / "Seismics" / ".{}".format(item.text())
                    if data_path.exists() is True:
                        if not hasattr(self, "data_{}".format(item.text())):
                            # check if data has already been loaded
                            # create new seis object if not
                            self.new_seis_object(item.text())
                        self.status.emit("Reading data ...")
                        seis_object = getattr(self, "data_{}".format(item.text()))
                        self.status.emit("Plotting ...")
                        seis_object.plot(ppp.CrlineIndex(self.control_widget.crline_SpinBox.value()), ax)
                        self.matplotlib_widget.fig.canvas.draw()
                        self.status.emit("")
                    else:
                        self.statusBar().showMessage("can not find data file {}".format(item.text))

    def new_seis_object(self, name):
        # emit status signal to MainWindow
        self.status.emit("Setting up seismic data object ...")

        data_path = Path(CONF.data_root) / CONF.current_survey / "Seismics" / ".{}".format(name)
        if data_path.exists() is True:
            segy_path = ""
            with open(str(data_path), "r") as fl:
                json_object =  json.load(fl)
                segy_path = json_object['path']
            seis_object = ppp.SeiSEGY(segy_path)
            setattr(self, "data_{}".format(name), seis_object)
        # flush status bar
        self.status.emit("")

    def radioButton_check_changed(self):
        if self.control_widget.il_radioButton.isChecked() is True:
            self.control_widget.inline_SpinBox.setEnabled(True)
            self.control_widget.crline_SpinBox.setDisabled(True)
            # self.inline_SpinBox.enabled = True
            # self.crline_SpinBox.enabled = False
        elif self.control_widget.cl_radioButton.isChecked() is True:
            self.control_widget.inline_SpinBox.setEnabled(False)
            self.control_widget.crline_SpinBox.setEnabled(True)

    def load_data_list(self, file_path):
        with open(str(file_path), "r") as fl:
            data_dict = json.load(fl)
            for name in data_dict.keys():
                # only initialize this way can it be set checkable
                new_item = QListWidgetItem(name, self.control_widget.data_listWidget)
                new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsUserCheckable)
                new_item.setCheckState(QtCore.Qt.Unchecked)


class Section_View_Control(QWidget, Ui_section_View_Control):
    def __init__(self, parent=None):
        super(Section_View_Control, self).__init__()
        self.setupUi(self)
