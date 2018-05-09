# -*- coding: utf-8 -*-
"""
Pore Pressure calculation with Eaton Method

Created on Wen May 09 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import range

__author__ = "Yu Hao"

import numpy as np

import pygeopressure as ppp


def eaton_calculation(obp_object, vel_object, output_object, a, b, n):
    obp_seisegy = ppp.SeiSEGY(str(obp_object.path))
    vel_seisegy = ppp.SeiSEGY(str(vel_object.path))
    output_seisegy = ppp.SeiSEGY(str(output_object.path))
    # preparation
    depth = np.array(list(obp_seisegy.depths()))
    vn = ppp.normal(depth, a, b)
    hydrostatic = ppp.hydrostatic_trace(depth)
    # actual calcualtion
    for il in obp_seisegy.inlines():
        obp_data_inline = obp_seisegy.inline(il)
        vel_data_inline = vel_seisegy.inline(il)
        output_data_inline = np.copy(obp_data_inline)
        for idx in range(obp_seisegy.nNorth):
            output_data_inline[idx] = ppp.eaton(
                vel_data_inline[idx], vn, hydrostatic,
                obp_data_inline[idx], n=n)
        output_seisegy.update(ppp.InlineIndex(il), output_data_inline)
