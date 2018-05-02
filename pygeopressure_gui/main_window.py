# -*- coding: utf-8 -*-
"""
A GUI application for geopressure prediction

Created on Fri Jan 05 2018
"""
# =============================================================================
# Stdlib imports
# =============================================================================
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import super, str

__author__ = "Yu Hao"

import sys
import time
import json
#==============================================================================
# Qt imports
#==============================================================================
# Since we are using Mayavi, pyface has to be used
from pyface.qt.QtGui import (QIcon, QApplication, QMainWindow, QMessageBox,
                             QGridLayout, QTreeWidgetItem, QWidget)
from pyface.qt import QtCore, QtGui
from pyface.qt.QtCore import Qt, pyqtSignal
# except uic which works fine
from PyQt4 import uic
# -----------------------------------------------------------------------------
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)
# =============================================================================
# Third Party imports
# =============================================================================
import numpy as np
from pathlib2 import Path
# =============================================================================
# Local imports
# =============================================================================
import pygeopressure as ppp

import pygeopressure_gui.qrc_resources
from pygeopressure_gui.ui.ui_pygeopressure import Ui_MainWindow
from pygeopressure_gui.dialogs.survey_edit_dialog import SurveyEditDialog
from pygeopressure_gui.dialogs.survey_select_dialog import SurveySelectDialog
from pygeopressure_gui.dialogs.seismic_manager_dialog import SeismicManagerDialog
from pygeopressure_gui.widgets.mayavi_widget import MayaviQWidget
from pygeopressure_gui.widgets.matplotlib_widget import MatplotlibWidget
from pygeopressure_gui.views.map_view import MapView
from pygeopressure_gui.views.section_view import SectionView
from pygeopressure_gui.views.well_log_view import WellLogView
from pygeopressure_gui.basic.well_plotter import WellPlotter

from pygeopressure_gui.config import CONF

# class TreeWidgetItem(QTreeWidgetItem):
#     def setData(self, column, role, value):
#         state = self.checkState(column)
#         QTreeWidgetItem.setData(self, column, role, value)
#         if (role == Qt.CheckStateRole and
#                 state != self.checkState(column)):
#             treewidget = self.treeWidget()
#             if treewidget is not None:
#                 treewidget.itemChecked.emit(self, column)
#==============================================================================
# Main Window
#==============================================================================
class MainWindow(QMainWindow, Ui_MainWindow):

    # itemChecked = pyqtSignal(object, int)

    def __init__(self):
        # super(MainWindow, self).__init__()
        super().__init__()
        self.program_setting = None
        self.setupUi(self)
        self.initUI()
        # connect events
        self.actionAbout.triggered.connect(self.aboutEvent)
        self.actionNewSurvey.triggered.connect(self.surveyEditEvent)
        self.actionSelectSurvey.triggered.connect(self.surveySelectEvent)
        self.actionManageSeismic.triggered.connect(self.open_seismic_manager_dialog)
        self.actionMapView.triggered.connect(self.create_Map_View)
        self.actionSectionView.triggered.connect(self.create_Section_View)
        self.actionWellLogView.triggered.connect(self.create_Well_Log_View)
        self.DataTree.itemClicked.connect(self.handleItemChecked)

        # self.statusBar().showMessage("System Status | Normal")
        self.source = None

    def initUI(self):
        # uic.loadUi('pygeopressure_gui/ui/pygeopressure.ui', self)
        self.setWindowIcon(QIcon(':/icon.png'))
        self.setWindowTitle("pyGeoPressure V1.0")

        layout = QGridLayout(self.tab_seis)
        self.mayavi_widget = MayaviQWidget(self.tab_seis)
        layout.addWidget(self.mayavi_widget)

        # layout2 = QGridLayout(self.tab_well)
        # self.matplotlib_widget = MatplotlibWidget(self.tab_well)
        # layout2.addWidget(self.matplotlib_widget)
        # self.plot_well()

        # self.mayavi_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.populate_treeWidget()
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
                    self.plot_seis() # Plot seismic data
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

    def populate_treeWidget(self):
        survey_file = Path(CONF.data_root, CONF.current_survey, '.survey')
        if survey_file.exists():
            self.DataTree.clear()
            self.DataTree.setHeaderLabel(CONF.current_survey)
            # populate seismic data
            seis_data = QTreeWidgetItem(self.DataTree)
            seis_data.setText(0, 'Seismic')
            # seis_data.setFlags(seis_data.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            with open(str(Path(CONF.data_root, CONF.current_survey, "Seismics/.seismics"))) as fl:
                seis_dict = json.load(fl)
                for item in seis_dict.keys():
                    f3 = QTreeWidgetItem(seis_data)
                    f3.setFlags(f3.flags() | Qt.ItemIsUserCheckable)
                    f3.setText(0, item)
                    f3.setCheckState(0, Qt.Unchecked)
            # populate well data
            well_data = QTreeWidgetItem(self.DataTree)
            well_data.setText(0, 'Wells')
            with open(str(Path(CONF.data_root, CONF.current_survey, "Wellinfo/.wellinfo"))) as fl:
                well_dict = json.load(fl)
                for item in well_dict.keys():
                    f3 = QTreeWidgetItem(well_data)
                    f3.setFlags(f3.flags() | Qt.ItemIsUserCheckable)
                    f3.setText(0, item)
                    f3.setCheckState(0, Qt.Unchecked)
            # populate surface data
            surface_data = QTreeWidgetItem(self.DataTree)
            surface_data.setText(0, 'Surfaces')
            with open(str(Path(CONF.data_root, CONF.current_survey, "Surfaces/.surfaces"))) as fl:
                surface_dict = json.load(fl)
                for item in surface_dict.keys():
                    f3 = QTreeWidgetItem(surface_data)
                    f3.setFlags(f3.flags() | Qt.ItemIsUserCheckable)
                    f3.setText(0, item)
                    f3.setCheckState(0, Qt.Unchecked)

            self.DataTree.show()

    def surveyEditEvent(self, event):
        survey_edit_window = SurveyEditDialog()
        survey_edit_window.exec_()

    def surveySelectEvent(self, event):
        survey_select_dialog = SurveySelectDialog()
        survey_select_dialog.selectButton.clicked.connect(self.populate_treeWidget)
        survey_select_dialog.exec_()

    def open_seismic_manager_dialog(self):
        seismic_manager_dialog = SeismicManagerDialog()
        seismic_manager_dialog.exec_()

    def create_new_tab(self, tab_name, display_name):
        """
        add new tab to the central tab widget
        """
        new_tab = QWidget()
        new_tab.setObjectName(_fromUtf8(tab_name))
        self.tabWidget.addTab(new_tab, _fromUtf8(""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(new_tab),
                                  _translate("MainWindow", display_name, None))
        return new_tab

    def create_Well_View(self):
        pass

    def create_Map_View(self):
        "Create a New Tab containing the MapView in the main TabWidget"
        self.tab_new = self.create_new_tab("tab_new", "Map View")
        # add adtional info
        self.tab_new.view_type = "MapView"
        layout = QGridLayout(self.tab_new)
        self.map_view = MapView(self.tab_new)
        layout.addWidget(self.map_view)

        file_path = Path(CONF.data_root) / CONF.current_survey / ".survey"
        if file_path.exists():
            self.map_view.draw_map(ppp.SurveySetting(ppp.ThreePoints(str(file_path))))
        self.tabWidget.setCurrentWidget(self.tab_new)
        # return the current tab
        # self.tabWidget.currentWidget()

    def create_Section_View(self):
        self.tab_section_view = self.create_new_tab("tab_section_view", "Section View")
        # add adtional info
        self.tab_section_view.view_type = "SectionView"
        layout = QGridLayout(self.tab_section_view)
        self.section_view = SectionView(self.tab_section_view)
        layout.addWidget(self.section_view)
        self.tabWidget.setCurrentWidget(self.tab_section_view)

    def create_Well_Log_View(self):
        self.tab_well_log_view = self.create_new_tab("tab_well_log_view", "Well Logs")
        self.tab_well_log_view.view_type = "WellLogView"
        layout = QGridLayout(self.tab_well_log_view)
        self.well_log_view = WellLogView(self.tab_well_log_view)
        layout.addWidget(self.well_log_view)
        self.tabWidget.setCurrentWidget(self.tab_well_log_view)

    # -------------------------------------------------------------------------
    # Override default events
    # def resizeEvent(self, event):
    #     # file_path = Path(CONF.data_root) / CONF.current_survey / ".survey"
    #     # self.map_view.draw_map(ppp.SurveySetting(ppp.ThreePoints(str(file_path))))
    #     self.map_view.redraw()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            save_config()
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


# =============================================================================
# Utilities
# =============================================================================
def save_config():
    if Path(CONF.data_root + CONF.current_survey).exists():
        CONF.to_json(CONF.setting_abs_path)

def start():
    # app = QApplication(sys.argv)
    # Don't create a new QApplication, it would unhook the Events
    # set by Traits on the existing QApplication. Simply use the
    # '.instance()' method to retrieve the existing one.
    app = QApplication.instance()
    window = MainWindow()
    sys.exit(app.exec_())
