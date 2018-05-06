@ECHO OFF
REM generate resource file
CD pygeopressure_gui
pyrcc4.exe -o qrc_resources.py resources.qrc
REM generate ui file
CD ui
CALL pyuic4.bat -o ui_pygeopressure.py pygeopressure.ui
CALL pyuic4.bat -o ui_survey_edit.py survey_edit.ui
CALL pyuic4.bat -o ui_survey_select.py survey_select.ui
CALL pyuic4.bat -o ui_seismic_manager.py seismic_manager.ui
CALL pyuic4.bat -o ui_section_view_control.py section_view_control.ui
CALL pyuic4.bat -o ui_well_log_view_control.py well_log_view_control.ui
CALL pyuic4.bat -o ui_segy_import_one_dialog.py segy_import_one.ui
CALL pyuic4.bat -o ui_segy_import_two_dialog.py segy_import_two.ui

CD ..\..
python app.py
