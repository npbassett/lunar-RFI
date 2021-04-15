# FDTD Simulations #

This folder contains scripts to run FDTD simulations of the diffraction of RFI around the Moon. The scripts require the Meep software package. Documentation and installation instructions can be found below. The scripts are currently set up to run simulations at 10 kHz but the frequency can be changed as desired. In order to ensure accurate results, the spacing of grid points should 5-10 times smaller than the wavelength and ideally greater than 8 times smaller. This means that simulating higher frequencies requires that the resolution be increased which requires more computational resources. For this reason, simulations above 100 kHz are very difficult, even with supercomputing resources.

### Meep Software ###

* [Documentation](https://meep.readthedocs.io/en/latest/)
* [Installation instructions](https://meep.readthedocs.io/en/latest/Installation/)
* Parallel computing can be utilized very easily by installing the parallel distribution of PyMeep
* Attention should be payed to [units in Meep](https://meep.readthedocs.io/en/latest/Introduction/#units-in-meep) to ensure that all values are specified correctly

### Running Simulations ###
Serial:

    conda activate mp
	python fdtd_10_kHz.py

Parallel:

    conda activate pmp
	mpirun -np (# processes) python fdtd_10_kHz.py