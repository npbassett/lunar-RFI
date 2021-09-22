# Lunar Low Frequency Environment #

This repository contains scripts for characterizing the low frequency radio environment behind the moon. The `FDTD_simulations` folder contains scripts to run electrodynamics simulations of the diffraction of radio waves around the Moon. The `calc_width` folder uses the results of these simulations to claculate the width of the quiet region given the frequency, height above the surface of the Moon, and intensity threshold. See the `README.md` file within each folder for further details. Special thanks to the [meep](https://meep.readthedocs.io/en/latest/) software team for providing an open-source platform for the simulations performed in this work.

## Citation
This code was presented in [Bassett et al. 2020](https://ui.adsabs.harvard.edu/abs/2020AdSpR..66.1265B/abstract). If you use this code for any academic work, please cite this paper.

## Dependencies
To run the scripts in the `calc_width` folder using the results of the FDTD simulations that have already been performed, you will need the following Python packages:
* [numpy](http://www.numpy.org/)
* [scipy](http://www.scipy.org/)

If you want to run full FDTD simulations yourself, you will need the following additional packages:
* [meep](https://meep.readthedocs.io/en/latest/)
* [h5py](https://www.h5py.org/)

## Contact
Neil.Bassett@colorado.edu
