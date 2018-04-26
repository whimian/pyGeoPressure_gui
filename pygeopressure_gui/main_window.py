# -*- coding: utf-8 -*-
"""
A GUI application for geopressure prediction

Created on Fri Jan 05 2018
"""
from __future__ import division, absolute_import, print_function
from __future__ import with_statement, unicode_literals

import sys
import os
from os import path
import time

from pyface.qt.QtGui import (QIcon, QApplication, QMainWindow, QMessageBox,
    QGridLayout, QTreeWidgetItem)
from PyQt4 import uic
from pyface.qt.QtCore import Qt, pyqtSignal
import numpy as np
from pathlib2 import Path
# # add designer plugin path
# USER_HOME = path.expanduser("~")
# PLUGIN_PATH = path.join(USER_HOME, 'dropbox/pyqt_designer_plugins')

# if PLUGIN_PATH not in sys.path:
#     sys.path.append(PLUGIN_PATH)

import pygeopressure as ppp

import pygeopressure_gui.qrc_resources

from .ui.ui_pygeopressure import Ui_MainWindow

from .dialogs.survey_edit_dialog import SurveyEditDialog
from .dialogs.survey_select_dialog import SurveySelectDialog
from .widgets.seis_widget import MayaviQWidget
from .widgets.well_log_widget import MatplotlibWidget
from .basic.well_plotter import WellPlotter

from . import DATA_ROOT

__author__ = "Yu Hao"
__copyright__ = "Copyright (C) 2018 Yu Hao"
__license__ = "MIT"

# class TreeWidgetItem(QTreeWidgetItem):
#     def setData(self, column, role, value):
#         state = self.checkState(column)
#         QTreeWidgetItem.setData(self, column, role, value)
#         if (role == Qt.CheckStateRole and
#                 state != self.checkState(column)):
#             treewidget = self.treeWidget()
#             if treewidget is not None:
#                 treewidget.itemChecked.emit(self, column)

class MainWindow(QMainWindow, Ui_MainWindow):

    # itemChecked = pyqtSignal(object, int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect events
        self.actionAbout.triggered.connect(self.aboutEvent)
        self.actionNewSurvey.triggered.connect(self.surveyEditEvent)
        self.actionSelectSurvey.triggered.connect(self.surveySelectEvent)
        self.DataTree.itemClicked.connect(self.handleItemChecked)

        # self.statusBar().showMessage("System Status | Normal")
        self.source = None

        self.plot_well()

    def initUI(self):
        # uic.loadUi('pygeopressure_gui/ui/pygeopressure.ui', self)
        self.setWindowIcon(QIcon(':/icon.png'))
        self.setWindowTitle("pyGeoPressure V1.0")

        layout = QGridLayout(self.tab_seis)
        self.mayavi_widget = MayaviQWidget(self.tab_seis)
        layout.addWidget(self.mayavi_widget)

        layout2 = QGridLayout(self.tab_well)
        self.matplotlib_widget = MatplotlibWidget(self.tab_well)
        layout2.addWidget(self.matplotlib_widget)

        # self.mayavi_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.init_treeview()
        self.show()

    def handleItemChecked(self):
        # self.statusBar().showMessage("{}".format(self.DataTree.selectedItems()))
        self.statusBar().showMessage("evoked")
        # for item in self.DataTree.selectedItems():
        for ti in range(self.DataTree.topLevelItemCount()):
            item = self.DataTree.topLevelItem(ti)
            for i in range(item.childCount()):
                child = item.child(i)
                if child.checkState(0) == Qt.Checked:
                    self.statusBar().showMessage('Displaying Data')
                    self.plot_seis()
                elif child.checkState(0) == Qt.Unchecked:
                    self.statusBar().showMessage('Unchecked')
                    if self.source is None:
                        pass
                    else:
                        self.source.remove()

    def plot_seis(self):

        f3 = ppp.SeisCube("D:\\HUB\\Python\\ui_pygeopressure\\f3_seismic.json")

        # read data into a ndarray
        data_cube = list()
        start = time.time()
        for inline in f3.inlines():
            data_cube.append(f3.get_inline(inline, 'seis'))
        data_cube = np.array(data_cube)
        end = time.time() - start

        start2 = time.time()
        # Create source
        self.source = self.mayavi_widget.visualization.scene.\
            mlab.pipeline.scalar_field(data_cube)
        self.source.spacing = [f3.inline_bin, f3.crline_bin, -f3.stepDepth*1.5]


        for axis in ['x', 'y', 'z']:
            plane = self.mayavi_widget.visualization.scene.\
                mlab.pipeline.image_plane_widget(
                    self.source,
                    plane_orientation='{}_axes'.format(axis),
                    slice_index=100,
                    colormap='Greys')
            # only slice is reversed(the actual data is not)
            plane.module_manager.scalar_lut_manager.reverse_lut = True

        self.mayavi_widget.visualization.scene.\
            mlab.outline()
        # add direction hint
        self.mayavi_widget.visualization.scene.\
            mlab.orientation_axes(
                xlabel='inline', ylabel='crline', zlabel='depth')
        ax = self.mayavi_widget.visualization.scene. \
            mlab.axes(
                xlabel='inline', ylabel='crline', zlabel='depth',
                ranges=[200, 650, 700, 1100, 1100, 400])
        ax.axes.label_format = '%.0f'
        # fig = self.mayavi_widget.visualization.scene.mlab.gcf()
        self.mayavi_widget.visualization.scene.\
            mlab.show()
        end2 = time.time() - start2
        self.statusBar().showMessage("data import:{}s, display: {}".format(end, end2))

    def plot_well(self):
        log_test = ppp.Log(
            str(Path(r"D:\HUB\Python\xihu_shanghai\data\bowers_kqt1.txt")))
        # axis = self.matplotlib_widget.axes
        # axis.invert_yaxis()
        # axis.ylim = [5000, 0]
        # log_test.plot(axis)
        well_plot_control = WellPlotter(self.matplotlib_widget.fig, log_test)
        well_plot_control.plot_well_log()

    def init_treeview(self):
        self.DataTree.setHeaderLabel('Data')

        seis_data = QTreeWidgetItem(self.DataTree)
        seis_data.setText(0, 'Seismic')
        # seis_data.setFlags(seis_data.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)

        self.f3 = QTreeWidgetItem(seis_data)
        self.f3.setFlags(self.f3.flags() | Qt.ItemIsUserCheckable)
        self.f3.setText(0, "f3")
        self.f3.setCheckState(0, Qt.Unchecked)

        self.DataTree.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def aboutEvent(self, event):
        box = QMessageBox.about(
            self, "pyGeoPressue",
            "A software for geopressure prediction.\n" + "\n" + \
            "Copyright: CUG\n" + \
            "Author: yuhao\n" + \
            "E-mail: yuhao89@live.cn")

    def surveyEditEvent(self, event):
        survey_edit_window = SurveyEditDialog()
        survey_edit_window.exec_()

    def surveySelectEvent(self, event):
        survey_select_dialog = SurveySelectDialog()
        survey_select_dialog.exec_()
