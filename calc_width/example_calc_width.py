"""
File: example_load_2d_interp.py
Author: Neil Bassett
Date: 20 Aug 2019

Description: Example of how to use calc_width.py to calculate the width of the
             radio quiet region given the frequency, height, and dB threshold.
"""
from calc_width import calc_width

nu = 534 #kHz
h = 73.5 #km above surface
dB = -85 #intensity threshold
width, plus, minus = calc_width(nu, h, dB)
print('Freq = %.1f kHz, h = %.1f km, threshold = %.1f dB:' % (nu, h, dB))
print('Width of radio quiet region = %.2f +%.2f/-%.2f deg'\
      % (width, plus, minus))
