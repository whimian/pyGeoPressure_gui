# -*- coding: utf-8 -*-
"""
Velocity converison calculation

Created on Fri Jan 05 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import range

__author__ = "Yu Hao"

import numpy as np

import pygeopressure as ppp

def interval_to_rms(input_object, output_object):
    input_seisegy = ppp.SeiSEGY(str(input_object.path))
    output_seisegy = ppp.SeiSEGY(str(output_object.path))
    twt = np.array(list(input_seisegy.depths()))
    for il in input_seisegy.inlines():
        input_data_inline = input_seisegy.inline(il)
        output_data_inline = np.copy(input_data_inline)
        for idx in range(input_seisegy.nNorth):
            output_data_inline[idx] = ppp.int2rms(
                twt, input_data_inline[idx])
        output_seisegy.update(ppp.InlineIndex(il), output_data_inline)

def rms_to_interval(input_object, output_object):
    input_seisegy = ppp.SeiSEGY(str(input_object.path))
    output_seisegy = ppp.SeiSEGY(str(output_object.path))
    twt = np.array(list(input_seisegy.depths()))
    for il in input_seisegy.inlines():
        input_data_inline = input_seisegy.inline(il)
        output_data_inline = np.copy(input_data_inline)
        for idx in range(input_seisegy.nNorth):
            output_data_inline[idx] = ppp.rms2int(
                twt, input_data_inline[idx])
        output_seisegy.update(ppp.InlineIndex(il), output_data_inline)
