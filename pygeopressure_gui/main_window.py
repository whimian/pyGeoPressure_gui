# -*- coding: utf-8 -*-
"""
A GUI application for geopressure prediction

Created on Fri Jan 05 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import super, str

__author__ = "Yu Hao"

# Stdlib imports --------------------------------------------------------------
import sys
import time
import json
# Qt imports ------------------------------------------------------------------
# Since we are using Mayavi, pyface has to be used
from pyface.qt.QtGui import (QIcon, QApplication, QMainWindow, QMessageBox,
                             QGridLayout, QTreeWidgetItem, QWidget,
                             QProgressBar)
from pyface.qt import QtCore, QtGui
from pyface.qt.QtCore import Qt, pyqtSignal, pyqtSlot
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
# Third Party imports ---------------------------------------------------------
import numpy as np
from pathlib2 import Path
# Local imports ---------------------------------------------------------------
import pygeopressure as ppp

import pygeopressure_gui.qrc_resources
from pygeopressure_gui.ui.ui_pygeopressure import Ui_MainWindow
# import Dialogs
from pygeopressure_gui.dialogs.survey_edit_dialog import SurveyEditDialog
from pygeopressure_gui.dialogs.survey_select_dialog import SurveySelectDialog
from pygeopressure_gui.dialogs.seismic_manager_dialog import \
    SeismicManagerDialog
from pygeopressure_gui.dialogs.segy_import_one_dialog import \
    SegyImportOneDialog
from pygeopressure_gui.dialogs.segy_export_dialog import SegyExportDialog
from pygeopressure_gui.widgets.mayavi_widget import MayaviQWidget
from pygeopressure_gui.widgets.matplotlib_widget import MatplotlibWidget
# import Views
from pygeopressure_gui.views.map_view import MapView
from pygeopressure_gui.views.section_view import SectionView
from pygeopressure_gui.views.well_log_view import WellLogView
from pygeopressure_gui.basic.well_plotter import WellPlotter
from pygeopressure_gui.basic.utils import (get_data_files, Seismic,
                                           create_new_seismic_file)

from pygeopressure_gui.config import CONF

from pygeopressure_gui.calculation.velocity_conversion import (
    interval_to_rms, rms_to_interval, interval_to_average, average_to_interval)
from pygeopressure_gui.calculation.velocity_to_density_conversion import (
    velocity_to_density_conversion)
from pygeopressure_gui.calculation.obp_calculation import obp_calculation
from pygeopressure_gui.calculation.eaton_calculation import eaton_calculation
from pygeopressure_gui.calculation.bowers_calculation import (
    bowers_calculation)

# Main Window =================================================================
class MainWindow(QMainWindow, Ui_MainWindow):

    # itemChecked = pyqtSignal(object, int)

    def __init__(self):
        # super(MainWindow, self).__init__()
        super().__init__()
        self.program_setting = None
        self.setupUi(self)
        self.initUI()
        # connect slots -------------------------------------------------------
        # menu actions
        self.actionAbout.triggered.connect(self.aboutEvent)
        self.actionNewSurvey.triggered.connect(self.create_survey_edit_dialog)
        self.actionSelectSurvey.triggered.connect(
            self.create_survey_select_dialog)
        self.actionManageSeismic.triggered.connect(
            self.open_seismic_manager_dialog)
        self.actionMapView.triggered.connect(self.create_Map_View)
        self.actionSectionView.triggered.connect(self.create_Section_View)
        self.actionWellLogView.triggered.connect(self.create_Well_Log_View)
        self.actionSegy.triggered.connect(self.create_segy_import_dialog)
        self.actionExportSegy.triggered.connect(self.create_segy_export_dialog)
        # toolbox
        # update ui
        self.toolBox.currentChanged.connect(
            self.update_velocity_conversion_panel)
        self.toolBox.currentChanged.connect(self.update_tdc_panel)
        self.toolBox.currentChanged.connect(self.update_density_panel)
        self.toolBox.currentChanged.connect(self.update_obp_panel)
        self.toolBox.currentChanged.connect(self.update_eaton_panel)
        self.toolBox.currentChanged.connect(self.update_bowers_panel)
        # buttons
        self.runButton_Velocity_Conversion.clicked.connect(
            self.run_velocity_conversion)
        self.runButton_gardner.clicked.connect(self.run_density_conversion)
        self.runButton_OBP.clicked.connect(self.run_obp_calculation)
        self.runButton_Eaton.clicked.connect(self.run_eaton_calculation)
        self.runButton_Bowers.clicked.connect(self.run_bowers_calculation)

        # Data Tree
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

        self.populate_treeWidget()
        self.update_velocity_conversion_panel(0)
        self.show()

# region Data Tree ============================================================

    def handleItemChecked(self):
        # self.statusBar().showMessage("evoked")
        item = self.DataTree.topLevelItem(0)
        for i in range(item.childCount()):
            child = item.child(i)
            child_name = child.text(0)
            if child.checkState(0) == Qt.Checked:
                if not hasattr(self, "source_{}".format(child_name)):
                    self.statusBar().showMessage(
                        'Displaying Data {}'.format(child_name))
                    self.plot_seis(child_name) # Plot seismic data
            elif child.checkState(0) == Qt.Unchecked:
                self.statusBar().showMessage('Unchecked', msecs=500)
                if hasattr(self, "source_{}".format(child_name)):
                    source = getattr(self, "source_{}".format(child_name))
                    source.remove()
                    delattr(self, "source_{}".format(child_name))

    def populate_treeWidget(self):
        survey_file = Path(CONF.data_root, CONF.current_survey, '.survey')
        if survey_file.exists():
            self.DataTree.clear()
            self.DataTree.setHeaderLabel(CONF.current_survey)
            # populate seismic data
            seis_data = QTreeWidgetItem(self.DataTree)
            seis_data.setText(0, 'Seismic')
            for item in get_data_files(
                    Path(CONF.data_root, CONF.current_survey, "Seismics")):
                f3 = QTreeWidgetItem(seis_data)
                f3.setFlags(f3.flags() | Qt.ItemIsUserCheckable)
                f3.setText(0, item)
                f3.setCheckState(0, Qt.Unchecked)
            # populate well data
            well_data = QTreeWidgetItem(self.DataTree)
            well_data.setText(0, 'Wells')
            for item in get_data_files(
                    Path(CONF.data_root, CONF.current_survey, "Wellinfo")):
                f3 = QTreeWidgetItem(well_data)
                f3.setFlags(f3.flags() | Qt.ItemIsUserCheckable)
                f3.setText(0, item)
                f3.setCheckState(0, Qt.Unchecked)
            # populate surface data
            surface_data = QTreeWidgetItem(self.DataTree)
            surface_data.setText(0, 'Surfaces')
            for item in get_data_files(
                    Path(CONF.data_root, CONF.current_survey, "Surfaces")):
                f3 = QTreeWidgetItem(surface_data)
                f3.setFlags(f3.flags() | Qt.ItemIsUserCheckable)
                f3.setText(0, item)
                f3.setCheckState(0, Qt.Unchecked)

            self.DataTree.show()

# region - Dialogs ============================================================

    def create_survey_edit_dialog(self):
        survey_edit_window = SurveyEditDialog()
        survey_edit_window.exec_()

    def create_survey_select_dialog(self):
        survey_select_dialog = SurveySelectDialog()
        survey_select_dialog.selectButton.clicked.connect(
            self.populate_treeWidget)
        survey_select_dialog.exec_()

    def open_seismic_manager_dialog(self):
        seismic_manager_dialog = SeismicManagerDialog()
        seismic_manager_dialog.exec_()

    @pyqtSlot()
    def create_segy_import_dialog(self):
        segy_import_dialog = SegyImportOneDialog()
        segy_import_dialog.data_imported.connect(self.populate_treeWidget)
        segy_import_dialog.exec_()

    def create_segy_export_dialog(self):
        segy_export_dialog = SegyExportDialog()
        segy_export_dialog.exec_()

# region - Views ==============================================================
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

    # 3D View -----------------------------------------------------------------
    def plot_seis(self, dataset_name):
        data_path = Path(CONF.data_root) / CONF.current_survey / \
            "Seismics" / ".{}".format(dataset_name)
        # seis_object = ppp.SeisCube(str(data_path))
        segy_path = ""
        inDepth = None
        property_type = None
        with open(str(data_path), "r") as fl:
            json_object = json.load(fl)
            segy_path = json_object['path']
            property_type = json_object['Property_Type']
            inDepth = json_object['inDepth']

        seis_object = ppp.SeiSEGY(segy_path)
        seis_object.inDepth = inDepth
        seis_object.property_type = property_type
        cm = ""
        if seis_object.property_type == 'Reflection':
            cm = u'seismic'
        elif seis_object.property_type == "Velocity":
            cm = u'jet'
        else:
            cm = u"seismic"
        # read data into a ndarray
        data_cube = list()
        start = time.time()
        for inline in seis_object.inlines():
            data_cube.append(seis_object.inline(inline))
        data_cube = np.array(data_cube)
        end = time.time() - start
        self.statusBar().showMessage("{}ms used for reading data".format(end))
        start2 = time.time()

        # Create source
        setattr(self, "source_{}".format(dataset_name), \
                self.mayavi_widget.visualization.scene. \
                    mlab.pipeline.scalar_field(data_cube))
        # self.source = self.mayavi_widget.visualization.scene.\
        #     mlab.pipeline.scalar_field(data_cube, name=dataset_name)

        self.statusBar().showMessage("type {}".format(type(self.source)))

        length_inline = (seis_object.survey_setting.nEast - 1) * \
                        seis_object.survey_setting.stepInline * \
                        seis_object.survey_setting.inline_bin
        length_depth = (seis_object.survey_setting.nDepth - 1) * \
                       seis_object.survey_setting.stepDepth
        scale = 0.5 * length_inline / length_depth

        getattr(self, "source_{}".format(dataset_name)).spacing = [
            seis_object.survey_setting.inline_bin * \
            seis_object.survey_setting.stepInline,
            seis_object.survey_setting.crline_bin * \
            seis_object.survey_setting.stepCrline,
            -seis_object.stepDepth * scale]

        x_slice = self.mayavi_widget.visualization.scene.\
            mlab.pipeline.image_plane_widget(
                getattr(self, "source_{}".format(dataset_name)),
                plane_orientation='x_axes',
                slice_index=int(seis_object.survey_setting.nEast // 2),
                colormap=cm,
                name="inline_slice")
        x_slice.module_manager.scalar_lut_manager.reverse_lut = True

        y_slice = self.mayavi_widget.visualization.scene.\
            mlab.pipeline.image_plane_widget(
                getattr(self, "source_{}".format(dataset_name)),
                plane_orientation='y_axes',
                slice_index=int(seis_object.survey_setting.nNorth // 2),
                colormap=cm, name="crline_slice")
        y_slice.module_manager.scalar_lut_manager.reverse_lut = True

        z_slice = self.mayavi_widget.visualization.scene.\
            mlab.pipeline.image_plane_widget(
                getattr(self, "source_{}".format(dataset_name)),
                plane_orientation='z_axes',
                slice_index=int(seis_object.survey_setting.nDepth // 2),
                colormap=cm,
                name='z_slice')
        z_slice.module_manager.scalar_lut_manager.reverse_lut = True

        # for axis in ['x', 'y', 'z']:
        #     plane = self.mayavi_widget.visualization.scene.\
        #         mlab.pipeline.image_plane_widget(
        #             self.source,
        #             plane_orientation='{}_axes'.format(axis),
        #             slice_index=100,
        #             colormap='Greys')
        #     # only slice is reversed(the actual data is not)
        #     plane.module_manager.scalar_lut_manager.reverse_lut = True

        outline = self.mayavi_widget.visualization.scene.\
            mlab.outline()
        # add direction hint
        self.mayavi_widget.visualization.scene.\
            mlab.orientation_axes(
                xlabel='inline', ylabel='crline', zlabel='depth')
        ax = self.mayavi_widget.visualization.scene. \
            mlab.axes(
                xlabel='inline', ylabel='crline', zlabel='depth',
                ranges=[
                    seis_object.survey_setting.startInline,
                    seis_object.survey_setting.endInline,
                    seis_object.survey_setting.startCrline,
                    seis_object.survey_setting.endCrline,
                    seis_object.survey_setting.endDepth,
                    seis_object.survey_setting.startDepth])
        ax.axes.label_format = '%.0f'

        self.mayavi_widget.visualization.scene.mlab.colorbar(
            orientation='vertical', label_fmt='%.1f')
        self.mayavi_widget.visualization.scene. \
            mlab.show()

    # Map View ----------------------------------------------------------------
    def create_Map_View(self):
        "Create a New Tab containing the MapView in the main TabWidget"
        if not hasattr(self, "tab_map_view"):
            self.tab_map_view = self.create_new_tab("tab_map_view", "Map View")
            # add adtional info
            self.tab_map_view.view_type = "MapView"
            layout = QGridLayout(self.tab_map_view)
            self.map_view = MapView(self.tab_map_view)
            layout.addWidget(self.map_view)
            self.init_map_view()
            self.tabWidget.setCurrentWidget(self.tab_new)
            # return the current tab
            # self.tabWidget.currentWidget()
        else:
            self.statusBar().showMessage('Map View already opened.')

    def init_map_view(self):
        file_path = Path(CONF.data_root) / CONF.current_survey / ".survey"
        if file_path.exists():
            self.map_view.draw_map(
                ppp.SurveySetting(
                    ppp.ThreePoints(str(file_path))))
    # Section View ------------------------------------------------------------
    def create_Section_View(self):
        if not hasattr(self, "tab_section_view"):
            self.tab_section_view = self.create_new_tab("tab_section_view",
                                                        "Section View")
            # add adtional info
            self.tab_section_view.view_type = "SectionView"
            layout = QGridLayout(self.tab_section_view)
            self.section_view = SectionView(self.tab_section_view)
            layout.addWidget(self.section_view)
            self.tabWidget.setCurrentWidget(self.tab_section_view)

            file_path = Path(CONF.data_root) / CONF.current_survey / ".survey"
            if file_path.exists():
                survey_set = ppp.SurveySetting(ppp.ThreePoints(str(file_path)))
                inline_SpinBox = \
                    self.section_view.control_widget.inline_SpinBox
                inline_SpinBox.setMaximum(survey_set.endInline)
                inline_SpinBox.setMinimum(survey_set.startInline)
                inline_SpinBox.setSingleStep(survey_set.stepInline)
                inline_SpinBox.setValue(survey_set.startInline)
                crline_SpinBox = \
                    self.section_view.control_widget.crline_SpinBox
                crline_SpinBox.setMaximum(survey_set.endCrline)
                crline_SpinBox.setMinimum(survey_set.startCrline)
                crline_SpinBox.setSingleStep(survey_set.stepCrline)
                crline_SpinBox.setValue(survey_set.stepCrline)
                step_inline_SpinBox = \
                    self.section_view.control_widget.step_inline_SpinBox
                step_inline_SpinBox.setMinimum(survey_set.stepInline)
                step_inline_SpinBox.setMaximum(
                    survey_set.stepInline * (survey_set.nEast - 1))
                step_inline_SpinBox.setSingleStep(survey_set.stepInline)
                step_crline_SpinBox = \
                    self.section_view.control_widget.step_crline_SpinBox
                step_crline_SpinBox.setMinimum(survey_set.stepCrline)
                step_crline_SpinBox.setMaximum(
                    survey_set.stepCrline * (survey_set.nEast - 1))
                step_crline_SpinBox.setSingleStep(survey_set.stepCrline)
                # seis_path = Path(CONF.data_root) / \
                #     CONF.current_survey / "Seismics" / ".seismics"
                # self.section_view.load_data_list(seis_path)

                self.section_view.status.connect(self.show_section_view_status)
        else:
            self.statusBar().showMessage('Section View already opened.')

    def create_Well_Log_View(self):
        if not hasattr(self, "tab_well_log_view"):
            self.tab_well_log_view = self.create_new_tab("tab_well_log_view",
                                                         "Well Logs")
            self.tab_well_log_view.view_type = "WellLogView"
            layout = QGridLayout(self.tab_well_log_view)
            self.well_log_view = WellLogView(self.tab_well_log_view)
            layout.addWidget(self.well_log_view)
            self.tabWidget.setCurrentWidget(self.tab_well_log_view)
        else:
            self.statusBar().showMessage('Well Log View already opened.')

# region - Panels =============================================================

    # Velocity Conversion Panel -----------------------------------------------
    @pyqtSlot(int)
    def update_velocity_conversion_panel(self, tab_index):
        if tab_index == 0:
            for fname in get_data_files(CONF.seismic_dir):
                seis = Seismic(fname, CONF)
                seis.from_file()
                if seis.Property_Type == "Velocity":
                    self.input_comboBox_Velocity_Conversion.addItem(seis.name)

    @pyqtSlot()
    def run_velocity_conversion(self):
        input_name = self.input_comboBox_Velocity_Conversion.currentText()
        output_name = self.output_lineEdit_Velocity_Conversion.text()
        if output_name != "" and \
                not output_name in get_data_files(CONF.seismic_dir):
            self.statusBar().showMessage("Creating new seismic Object ...")
            create_new_seismic_file(output_name, input_name, CONF)
            self.populate_treeWidget()
            command = self.conversion_type_comboBox.currentText()
            self.statusBar().showMessage(
                "Performing {} Velocity Conversion ...".format(command))
            eval("{}(Seismic(input_name, CONF), \
                Seismic(output_name, CONF))".format(
                    command.replace(' ', '_').lower()))
            # interval_to_rms(
            #     Seismic(input_name, CONF), Seismic(output_name, CONF))
            self.statusBar().showMessage('')
    # Time Depth Conversion Panel ---------------------------------------------
    @pyqtSlot(int)
    def update_tdc_panel(self, tab_index):
        if tab_index == 1:
            for fname in get_data_files(CONF.seismic_dir):
                seis = Seismic(fname, CONF)
                seis.from_file()
                if seis.Property_Type == "Velocity":
                    self.avg_vel_comboBox.addItem(seis.name)
                self.input_for_tdc_comboBox.addItem(seis.name)
    # Density Conversion Panel ------------------------------------------------
    @pyqtSlot(int)
    def update_density_panel(self, tab_index):
        if tab_index == 2:
            for fname in get_data_files(CONF.seismic_dir):
                seis = Seismic(fname, CONF)
                seis.from_file()
                if seis.Property_Type == "Velocity":
                    self.interval_velocity_comboBox_gardner.addItem(seis.name)

    def run_density_conversion(self):
        input_name = self.interval_velocity_comboBox_gardner.currentText()
        output_name = self.ouput_lineEdit_gardner.text()
        if output_name != "" and \
                not output_name in get_data_files(CONF.seismic_dir):
            self.statusBar().showMessage("Creating new seismic Object ...")
            create_new_seismic_file(output_name, input_name, CONF)
            self.populate_treeWidget()
            # command = self.conversion_type_comboBox.currentText()
            self.statusBar().showMessage("Calculating Density ...")
            gardner_c = float(self.gardner_C_lineEdit.text())
            gardner_d = float(self.gardner_D_lineEdit.text())
            velocity_to_density_conversion(
                Seismic(input_name, CONF), Seismic(output_name, CONF),
                gardner_c, gardner_d)
            self.statusBar().showMessage('')
    # OBP Calculation Panel ---------------------------------------------------
    @pyqtSlot(int)
    def update_obp_panel(self, tab_index):
        if tab_index == 3:
            self.density_comboBox_OBP.clear()
            for fname in get_data_files(CONF.seismic_dir):
                seis = Seismic(fname, CONF)
                seis.from_file()
                if seis.Property_Type == "Density":
                    self.density_comboBox_OBP.addItem(seis.name)

    def run_obp_calculation(self):
        input_name = self.density_comboBox_OBP.currentText()
        output_name = self.output_lineEdit_OBP.text()
        if output_name == "":
            self.statusBar().showMessage('Please set OUTPUT')
        elif output_name in get_data_files(CONF.seismic_dir):
            self.statusBar().showMessage('OUTPUT already exists.')
        else:
            self.statusBar().showMessage("Creating new seismic Object ...")
            create_new_seismic_file(output_name, input_name, CONF)
            self.populate_treeWidget()
            self.statusBar().showMessage("Calculating Density ...")
            obp_calculation(
                Seismic(input_name, CONF), Seismic(output_name, CONF))
            self.statusBar().showMessage('')
    # Eaton Panel -------------------------------------------------------------
    @pyqtSlot(int)
    def update_eaton_panel(self, tab_index):
        if tab_index == 4:
            self.obp_comboBox_Eaton.clear()
            self.velocity_comboBox_Eaton.clear()
            for fname in get_data_files(CONF.seismic_dir):
                seis = Seismic(fname, CONF)
                seis.from_file()
                if seis.Property_Type == "Pressure":
                    self.obp_comboBox_Eaton.addItem(seis.name)
                elif seis.Property_Type == "Velocity":
                    self.velocity_comboBox_Eaton.addItem(seis.name)

    def run_eaton_calculation(self):
        vel_name = self.velocity_comboBox_Eaton.currentText()
        obp_name = self.obp_comboBox_Eaton.currentText()
        output_name = self.output_lineEdit_Eaton.text()
        n = float(self.eaton_n_spinBox.value())
        a = float(self.nct_a_lineEdit.text())
        b = float(self.nct_b_lineEdit.text())
        if output_name == "":
            self.statusBar().showMessage('Please set OUTPUT')
        elif output_name in get_data_files(CONF.seismic_dir):
            self.statusBar().showMessage('OUTPUT already exists.')
        else:
            self.statusBar().showMessage("Creating new seismic Object ...")
            create_new_seismic_file(output_name, obp_name, CONF)
            self.populate_treeWidget()
            self.statusBar().showMessage("Calculating Eaton Pressure ...")
            eaton_calculation(
                Seismic(obp_name, CONF), Seismic(vel_name, CONF),
                Seismic(output_name, CONF), a, b, n)
            self.statusBar().showMessage('')
    # Bowers Panel ------------------------------------------------------------
    @pyqtSlot(int)
    def update_bowers_panel(self, tab_index):
        if tab_index == 5:
            self.obp_comboBox_Bowers.clear()
            self.vel_comboBox_Bowers.clear()
            for fname in get_data_files(CONF.seismic_dir):
                seis = Seismic(fname, CONF)
                seis.from_file()
                if seis.Property_Type == "Pressure":
                    self.obp_comboBox_Bowers.addItem(seis.name)
                elif seis.Property_Type == "Velocity":
                    self.vel_comboBox_Bowers.addItem(seis.name)

    def run_bowers_calculation(self):
        vel_name = self.vel_comboBox_Bowers.currentText()
        obp_name = self.obp_comboBox_Bowers.currentText()
        output_name = self.output_lineEdit_Bowers.text()
        a = float(self.a_lineEdit_Bowers.text())
        b = float(self.b_lineEdit_Bowers.text())
        if output_name == "":
            self.statusBar().showMessage('Please set OUTPUT')
        elif output_name in get_data_files(CONF.seismic_dir):
            self.statusBar().showMessage('OUTPUT already exists.')
        else:
            self.statusBar().showMessage("Creating new seismic Object ...")
            create_new_seismic_file(output_name, obp_name, CONF)
            self.populate_treeWidget()
            self.statusBar().showMessage("Calculating Bowers Pressure ...")
            bowers_calculation(
                Seismic(obp_name, CONF), Seismic(vel_name, CONF),
                Seismic(output_name, CONF), a, b)
            self.statusBar().showMessage('')
# endregion
    # shared slots ------------------------------------------------------------
    @pyqtSlot(str)
    def show_section_view_status(self, message):
        self.statusBar().showMessage(message)

    # Override default events -------------------------------------------------
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message',
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

# region - Utilities ==========================================================
def save_config():
    survey_path = Path(CONF.data_root) / CONF.current_survey
    if survey_path.exists():
        CONF.to_json(CONF.setting_abs_path)

def start():
    # app = QApplication(sys.argv)
    # Don't create a new QApplication, it would unhook the Events
    # set by Traits on the existing QApplication. Simply use the
    # '.instance()' method to retrieve the existing one.
    app = QApplication.instance()
    window = MainWindow()
    sys.exit(app.exec_())
# endregion
