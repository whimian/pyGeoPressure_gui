# -*- coding: utf-8 -*-
"""
Pore Pressure calculation with Bowers Method

Created on Wen May 09 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import range

__author__ = "Yu Hao"

import numpy as np

import pygeopressure as ppp


def bowers_calculation(obp_object, vel_object, output_object, a, b):
    obp_seisegy = ppp.SeiSEGY(str(obp_object.path))
    vel_seisegy = ppp.SeiSEGY(str(vel_object.path))
    output_seisegy = ppp.SeiSEGY(str(output_object.path))

    # actual calcualtion
    for il in obp_seisegy.inlines():
        obp_data_inline = obp_seisegy.inline(il)
        vel_data_inline = vel_seisegy.inline(il)
        output_data_inline = np.copy(obp_data_inline)
        for idx in range(obp_seisegy.nNorth):
            output_data_inline[idx] = ppp.bowers(
                vel_data_inline[idx], obp_data_inline[idx], 1,
                start_idx=-1, a=a, b=b, vmax=5000, end_idx=None)
        output_seisegy.update(ppp.InlineIndex(il), output_data_inline)
