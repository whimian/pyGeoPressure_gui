# -*- coding: utf-8 -*-
"""
Overburden Pressure calculation

Created on Tue May 08 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import range

__author__ = "Yu Hao"

import numpy as np

import pygeopressure as ppp


def obp_calculation(input_object, output_object):
    input_seisegy = ppp.SeiSEGY(str(input_object.path))
    stepDepth = input_seisegy.survey_setting.stepDepth
    output_seisegy = ppp.SeiSEGY(str(output_object.path))
    # depth = np.array(list(input_seisegy.depths()))
    for il in input_seisegy.inlines():
        input_data_inline = input_seisegy.inline(il)
        output_data_inline = np.copy(input_data_inline)
        for idx in range(input_seisegy.nNorth):
            output_data_inline[idx] = ppp.obp_trace(
                input_data_inline[idx], stepDepth)
        output_seisegy.update(ppp.InlineIndex(il), output_data_inline)
