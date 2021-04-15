"""
File: fdtd_10_kHz_no_moon.py
Author: Neil Bassett
Last Updated: 14 August 2019

Description: This script runs an Finite Difference Time Domain (FDTD)
             simulation to investigate the dirraction of radio waves
             around the Moon. This should be run in conjunction with
             fdtd_10_kHz.py to get a meaningful relative intensity.
             Must install the Meep software package, see
             https://meep.readthedocs.io/en/latest/Installation/
"""
from __future__ import print_function
import cmath
import math
import meep as mp
import numpy as np
import h5py as h5

#Scale factor is chosen to be 1 km
freq = 1./30. #10 kHz, see Meep documentation for info about units

cell = mp.Vector3(4000, 4000, 0) #4000 x 4000 km grid

#Plane wave source
sources = [mp.Source(mp.ContinuousSource(frequency=freq),
                     component=mp.Hz, #magnetic polarization
                     center=mp.Vector3(-1900, 0),
                     size=mp.Vector3(0, 4000)
           )]
pml_layers = [mp.PML(100.0)] #PML absorbs outgoing waves
resolution = 1 #increase resolution for higher frequencies, see Meep docs

sim = mp.Simulation(cell_size=cell,
                    boundary_layers=pml_layers,
                    sources=sources,
                    resolution=resolution,
                    symmetries=[mp.Symmetry(direction=mp.Y, phase=-1)]
                    )

#Run simulation until steady state is reached, output energy density
#over one wave period and average in post-processing
tmax = 20000
sim.run(mp.synchronized_magnetic(mp.at_time(tmax-27, mp.output_tot_pwr),
                                 mp.at_time(tmax-24, mp.output_tot_pwr),
                                 mp.at_time(tmax-21, mp.output_tot_pwr),
                                 mp.at_time(tmax-18, mp.output_tot_pwr),
                                 mp.at_time(tmax-15, mp.output_tot_pwr),
                                 mp.at_time(tmax-12, mp.output_tot_pwr),
                                 mp.at_time(tmax-9, mp.output_tot_pwr),
                                 mp.at_time(tmax-6, mp.output_tot_pwr),
                                 mp.at_time(tmax-3, mp.output_tot_pwr),
                                 mp.at_end(mp.output_tot_pwr)
                                 ),
        until=tmax)
