# Common utility codes used at JheLab for AFM, rheology, and ML research

jhelabtoolkit contains various code used at JheLab (Dept. of Physics, Seoul National University), including code for reading measurement files, calibrating raw data, preprocessing routines such as denoising, and other utility codes. 

While a detailed documentation is pending, below is a brief description of the main submodules of this package.
## jhelabtoolkit.io
Contains code used to read measurement files generated from commonly used instruments in the lab.
Currently supports:
- Nanosurf FlexAFM (.nid file format)
- Zurich Instrumenet MFLI Lock-in Amplifier (.txt file format)

## jhelabtoolkit.calibration
Contains algorithms to calibrate the measured experimental data.
Currently contains routines for:
- AFM spring constant calibration (Sader method)
- AFM inverse optical lever sensitivity calculation (Sader method)

## jhelabtoolkit.preprocessing
Contains code to process the measured data prior to further downstream analysis.
Currently contains the following code:
- Denoising algorithms for spectral measurements (spectral subtraction, morphological denoising)

## jhelabtoolkit.utils
Contains miscellaneous code that do not belong in the above categories.

## Let's talk!
To learn more about the work we do, visit our google scholar (https://scholar.google.co.kr/citations?user=z_c9ABQAAAAJ&hl=ko, https://scholar.google.com/citations?user=LyVlf_8AAAAJ&hl=en&oi=ao) or contact us via email (whjhe@snu.ac.kr, jhko725@snu.ac.kr)!
