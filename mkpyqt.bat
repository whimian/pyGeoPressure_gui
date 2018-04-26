@ECHO OFF
REM generate resource file
CD pygeopressure_gui
pyrcc4.exe -o qrc_resources.py resources.qrc
REM generate ui file
CD ui
CALL pyuic4.bat -o ui_pygeopressure.py pygeopressure.ui
CALL pyuic4.bat -o ui_survey_edit.py survey_edit.ui
CALL pyuic4.bat -o ui_survey_select.py survey_select.ui
CD ..\..
python app.py
