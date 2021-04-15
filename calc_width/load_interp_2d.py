"""
File: load_2d_interp.py
Author: Neil Bassett
Date: 20 Aug 2019

Description: Contains functions which load interpolations of height vs. dB
             threshold grid for the coefficients a and b in the power law
             a*(nu**b) where nu is the frequency. Grid was calculated 
             from fits to FDTD simulations of RFI diffraction around the moon.
"""
from __future__ import division
import numpy as np
import pickle
from scipy.interpolate import interp2d

def load_interp_2d():
    """
    Loads interpolation of h vs. dB grid for a and b power law parameters
    from 2d_interp_h_vs_dB.pkl
    """
    f = open('2d_interp_h_vs_dB.pkl', 'rb')
    interp_dict = pickle.load(f)
    f.close()
    return interp_dict['a_grid_interp'],\
           interp_dict['b_grid_interp']
