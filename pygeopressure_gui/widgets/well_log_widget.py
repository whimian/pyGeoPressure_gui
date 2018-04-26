# -*- coding: utf-8 -*-
"""
A plot widget based on matplotlib

Created on Sun Jan 21 2018
"""
from __future__ import division, absolute_import, print_function
from __future__ import with_statement, unicode_literals
import random

from PyQt4.QtCore import Qt, QSize, QTimer
from PyQt4.QtGui import QWidget, QVBoxLayout, QSizePolicy

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib import rcParams

rcParams['font.size'] = 9
# self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)

        self.fig = Figure((5.0, 4.0), dpi=100)
        self.axes = self.fig.add_subplot(111)

        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.canvas.setFocus()

        self.mpl_toolbar = NavigationToolbar(self.canvas, self)

        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_toolbar)
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)

        # timer = QTimer(self)
        # timer.timeout.connect(self.update_figure)
        # timer.start(1000)

    # def compute_initial_figure(self):
    #     self.axes.plot([0, 1, 2, 3], [1, 2, 0, 4], 'r')

    # def update_figure(self):
    #     # Build a list of 4 random integers between 0 and 10 (both inclusive)
    #     l = [random.randint(0, 10) for i in range(4)]
    #     self.axes.cla()
    #     self.axes.plot([0, 1, 2, 3], l, 'r')
    #     self.canvas.draw()

    def on_key_press(self, event):
        print('you pressed', event.key)
        # implement the default mpl key press events described at
        # http://matplotlib.org/users/navigation_toolbar.html#navigation-keyboard-shortcuts
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    # def sizeHint(self):
    #     return QSize(*self.canvas.get_width_height())

    def minimumSizeHint(self):
        return QSize(10, 10)
