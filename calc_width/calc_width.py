"""
File: calc_width.py
Author: Neil Bassett
Date: 20 Aug 2019

Description: Contains function to calculate the width of the radio quiet region
             given the frequency, height above the lunar surface, and intensity
             threshold in dB.
"""
from __future__ import division
import numpy as np
from load_interp_2d import load_interp_2d

def geom_width(h):
    """
    Calculates width of quiet from pure geometry (i.e. ignoring diffraction)

    h: height above the surface of the Moon in km 
    """
    r_moon = 1737.1
    r_earth = 6371
    d = 384400
    slope = (r_earth - r_moon)/d
    A = 1 + (slope**2)
    B = -2*(slope*r_moon)
    C = (r_moon**2) - ((r_moon + h)**2)
    root1 = (-B + np.sqrt((B**2) - 4*A*C))/(2*A)
    root2 = (-B - np.sqrt((B**2)- 4*A*C))/(2*A)
    if root1 > 0:
        x = root1
    else:
        x = root2
    y = np.sqrt((r_moon + h)**2 - x**2)
    angle = np.arctan(y/x)
    return 2*angle*(180./np.pi)

def width_pwr_law(nu, h, a, b):
    """
    Defines power law model for the width of the quiet region as a function
    of frequency. Offset is determined by geometric width which is the
    behavior at infinite frequency.

    nu: frequency in kHz
    h: height above lunar surface in km
    a: coefficient, may be calculated from interpolation of h vs dB grid
    b: coefficient, may be calculated from interpolation of h vs dB grid
    """
    return geom_width(h) - a*(nu**b)

def calc_width(nu, h, dB):
    """
    Calculates width of quiet cone given frequency, height, and dB threshold

    nu: frequency in kHz
    h: height above lunar surface in km (0 <= h <= 150)
    dB: quiet region intensity threshold in dB (-90 <= dB <= -50)

    returns: best estimate of width of quiet region (in degrees) with
             plus and minus uncertainties
    """
    #if (h < 0 or h > 150 or dB < -90 or dB > -50):
    #    raise ValueError('Parameters not within appropriate bounds!')
    a_interp, b_interp = load_interp_2d()
    best_fit = width_pwr_law(nu, h, a_interp(h, dB)[0], b_interp(h, dB)[0])
    plus_uncert = width_pwr_law(nu, h, a_interp(h, dB)[0] - 7,\
                                b_interp(h, dB)[0] - 0.01) - best_fit
    minus_uncert = best_fit - width_pwr_law(nu, h, a_interp(h, dB)[0] + 7,\
                                            b_interp(h, dB)[0] + 0.01)
    if (best_fit < 0):
        best_fit = minus_uncert = 0
        plus_uncert = max(0, best_fit + plus_uncert)
    return best_fit, plus_uncert, minus_uncert
