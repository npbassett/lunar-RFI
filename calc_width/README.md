# Calculating Width of Quiet Region #

This folder contains Python functions which use the numerical results of FDTD simulations to quickly calculate the size of the radio quiet cone.
The width of the quiet region depends on three parameters:

* ν: frequency (in kHz)
* h: height above in the lunar surface (0 km <= h <= 150 km)
* dB: the relative intensity threshold for the quiet region (-90 <= dB <= -50)

### Running scripts ###

The `calc_width` will likely be the only function that you will need to use directly. This function will return the width of the quiet region along with a +/- uncertainty in degrees given the three input parameters listed above. If the calculated width is negative, the function will return 0. An example of how to use the `calc_width` function is shown in the `example_calc_width.py` script.