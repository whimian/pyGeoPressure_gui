# -*- coding: utf-8 -*-
"""
a Seismic display widget based on mayavi

Created on Tue Jan 16 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

import os
os.environ['ETS_TOOLKIT'] = 'qt4'

from pyface.qt.QtGui import QWidget, QVBoxLayout
from pyface.qt.QtCore import Qt

from traits.api import HasTraits, Instance, on_trait_change
from traitsui.api import View, Item

from mayavi.core.ui.api import MayaviScene, MlabSceneModel, SceneEditor


#The actual visualization
class Visualization(HasTraits):
    scene = Instance(MlabSceneModel, ())

    @on_trait_change('scene.activated')
    def update_plot(self):
        # This function is called when the view is opened. We don't
        # populate the scene when the view is not yet open, as some
        # VTK features require a GLContext.

        # We can do normal mlab calls on the embedded scene.
        # self.scene.mlab.test_plot3d()
        pass

    # the layout of the dialog created
    view = View(
        Item('scene',
             editor=SceneEditor(scene_class=MayaviScene),
             height=250,
             width=300,
             show_label=False),
        resizable=True) # We need this to resize with the parent widget



class MayaviQWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.visualization = Visualization()

        # If you want to debug, beware that you need to remove the Qt
        # input hook.
        #QtCore.pyqtRemoveInputHook()
        #import pdb ; pdb.set_trace()
        #QtCore.pyqtRestoreInputHook()

        # The edit_traits call will generate the widget to embed.
        self.ui = self.visualization.edit_traits(parent=self,
                                                 kind='subpanel').control
        layout.addWidget(self.ui)
        self.ui.setParent(self)
