# -*- coding: utf-8 -*-
"""
run script for pygeopressure gui program

Created on Sun Jan 21 2018
"""
from __future__ import print_function

import sys, getopt

from pyface.qt.QtGui import QApplication

# CORE_PATH = "D:\\HUB\\Python\\PorePressurePrediction"

# if CORE_PATH not in sys.path:
#     sys.path.append(CORE_PATH)

# from pygeopressure_gui.main_window import MainWindow

# import pyGeoPressure Core code
def main(argv):
    # pyGeoPressure core code path
    core_path = "D:\\HUB\\Python\\PorePressurePrediction"
    try:
        opts, args = getopt.getopt(argv, "hp:", ["path="])
    except getopt.GetoptError:
        print('app.py -p <path to pyGeoPressure core>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('app.py -p <path to pyGeoPressure core>')
            sys.exit()
        elif opt in ("-p", "--corepath"):
            core_path = arg
            print("pyGeoPressure core path：'{}'".format(core_path))
    if core_path not in sys.path:
        sys.path.append(core_path)


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # Don't create a new QApplication, it would unhook the Events
    # set by Traits on the existing QApplication. Simply use the
    # '.instance()' method to retrieve the existing one.
    main(sys.argv[1:])
    from pygeopressure_gui.main_window import MainWindow
    app = QApplication.instance()
    window = MainWindow()
    sys.exit(app.exec_())
