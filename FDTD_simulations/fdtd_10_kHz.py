"""
File: fdtd_10_kHz.py
Author: Neil Bassett
Last Updated: 11 September 2019

Description: This script runs an Finite Difference Time Domain (FDTD)
             simulation to investigate the dirraction of radio waves
             around the Moon. This should be run in conjunction with
             fdtd_10_kHz_no_moon.py to get a meaningful relative
             intensity. Must install the Meep software package, see
             https://meep.readthedocs.io/en/latest/Installation/
"""
from __future__ import print_function
import cmath
import math
import meep as mp
import numpy as np
import h5py as h5

def moon_constant(position):
    """
    Function which returns a Medium object with the correct permittivity
    and conductivity based on a constant density profile (rho = 3.34 g/cc).
    """
    z = (1737 - np.sqrt(np.power(position.x, 2) +\
         np.power(position.y, 2)))*1e5 #depth in cm
    rho = 3.34
    epsilon = np.power(1.919, rho) #permittivity
    L = np.power(10, (0.44*rho - 2.943)) #loss tangent
    sigma = 2*math.pi*freq*L #see "conductivity" in MEEP docs
    return mp.Medium(epsilon=epsilon, D_conductivity=sigma)

def moon_continuous(position):
    """
    Function which returns a Medium object with the correct permittivity
    and conductivity based on a continous density profile given in the
    Lunar Sourcebook (rho = 1.39z^0.056)
    """
    z = (1737 - np.sqrt(np.power(position.x, 2) +\
         np.power(position.y, 2)))*1e5 #depth in cm
    rho = 1.39*(np.power(z, 0.056))
    epsilon = np.power(1.919, rho) #permittivity
    L = np.power(10, (0.44*rho - 2.943)) #loss tangent
    sigma = 2*math.pi*freq*L #see "conductivity" in MEEP docs
    return mp.Medium(epsilon=epsilon, D_conductivity=sigma)

def moon_step(position):
    """
    Function which returns a Medium object with the correct permittivity
    and conductivity based on a stepped density profile from seismic
    measurements of Weber et al. 2011
    """
    z = (1737 - np.sqrt(np.power(position.x, 2) +\
         np.power(position.y, 2))) #depth in km
    depth_steps = np.array([1, 15, 40, 238, 1407.1, 1497.1, 10000000])
    rho_steps = np.array([1.92, 2.7, 2.8, 3.3, 3.4, 5.1, 8.0])
    rho = rho_steps[z < depth_steps][0]
    epsilon = np.power(1.919, rho) #permittivity
    L = np.power(10, (0.44*rho - 2.943)) #loss tangent
    sigma = 2*math.pi*freq*L #see "conductivity" in MEEP docs
    return mp.Medium(epsilon=epsilon, D_conductivity=sigma)

#Scale factor is chosen to be 1 km
freq = 1./30. #10 kHz, see Meep documentation for info about units
cell = mp.Vector3(4000, 4000, 0) #4000 x 4000 km grid

#Insert Moon as object
geometry = [mp.Sphere(1737,
                      center=mp.Vector3(),
                      material=moon_constant #moon_continuous or moon_step
            )]
#Plane wave source
sources = [mp.Source(mp.ContinuousSource(frequency=freq),
                     component=mp.Hz, #magnetic polarization
                     center=mp.Vector3(-1900, 0),
                     size=mp.Vector3(0, 4000)
           )]
pml_layers = [mp.PML(100.0)] #PML absorbs outgoing waves
resolution = 1 #increase resolution for higher frequencies, see Meep docs

#Initialize simulation
sim = mp.Simulation(cell_size=cell,
                    boundary_layers=pml_layers,
                    geometry=geometry,
                    sources=sources,
                    resolution=resolution,
                    symmetries=[mp.Symmetry(direction=mp.Y, phase=-1)],
                    extra_materials=[moon_constant(mp.Vector3()),
                                     moon_continuous(mp.Vector3()),
                                     moon_step(mp.Vector3())]
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
