# ormir-mids
I/O of Medical Image Data Structure (MIDS) for Open and Reproducible Musculoskeletal Imaging Research ([ORMIR](https://ormircommunity.github.io/)). Based on the [BIDS](https://bids.neuroimaging.io/) data structure.

> [!NOTE]  
> This package is a fork of [muscle-bids](https://github.com/muscle-bids/muscle-bids) for muscle MR imaging data.

[![GitHub license](https://img.shields.io/github/license/ormir-mids/ormir-mids)](https://github.com/ormir-mids/ormir-mids/blob/main/LICENSE)

## Tutorial
Run the tutorial: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/muscle-bids/muscle-bids/blob/main/jupyter/Muscle-bids_dcm2mbids.ipynb)

## Main contributors

* Francesco Santini
* Donnie Cameron
* Leonardo Barzaghi
* Judith Cueto Fernandez
* Jilmen Quintiens
* Lee Youngjun
* Jukka Hirvasniemi
* Gianluca Iori
* Serena Bonaretti

## Installation

### Dependencies
To install `ormir-mids`, run the code below, noting this list of [dependencies](dependencies.md).

It is recommended to install `ormir-mids` in a separate virtual environment:
```commandline
conda env create -n ormir-mids
conda activate ormir-mids
```

Clone the git repository:
```shell
git clone https://github.com/ormir-mids/ormir-mids.git
```
Now we can install the package using `pip`. This will also install the required dependencies.
```shell
cd ormir-mids
pip install .
pip install --upgrade nibabel # the default nibabel has bugs
```

## Usage
`ormir-mids` can be used in two ways: 
    
1. Running `dcm2mbids` as an executable to convert DICOM data to the MIDS format.
2. Importing `ormir-mids` as a Python module to find, load, and interrogate ORMIR-MIDS-format data.

### 1. Converting DICOMs to the ORMIR-MIDS format

The commandline script is called `dcm2mbids.exe`. To view the commandline script help type
```commandline
dcm2mbids -h
```

To use `ormir-mids` within Python, import the following modules
```python
from ormir_mids.utils.io import find_bids, load_bids
import nibabel as nib
```

For a detailed description of how to use `ormir-mids` see the following notebook
#### [ormir-mids usage: dcm2mbids](examples/jupyter/Muscle-bids_dcm2mbids.ipynb) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](examples/jupyter/Muscle-bids_dcm2mbids.ipynb)

### 2. Exploring medical volumes with ORMIR-MIDS
`ormir-mids` can be used within Python to load, manipule and visualize medical volume datasets, without convertion to the BIDS format.

- Load a DICOM file to a MedicalVolume object

```python
from ormir_mids.utils.io import load_dicom
```
```python
mv = load_dicom('<Path-to-DICOM-file>')
```

- Slice the volume. This will create a separate subvolume. Metadata will be sliced appropriately.
```python
mv_subvolume = mv[50:90, 50:90, 30:70]
```

- Convert volume to ITK image with [SimpleITK](https://simpleitk.org/)
```python
mv_itk = mv.to_sitk()
```


Examples of how to use `ormir-mids` for common data handling, image manipulation and processing tasks within Python can be found in this notebook
#### [ormir-mids usage: MedicalVolume class](examples/jupyter/Muscle-bids_MedicalVolume_tests.ipynb) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](examples/jupyter/Muscle-bids_MedicalVolume_tests.ipynb)

## Acknowledgement

This package was developed thanks to the support of the JCMSK community during the Maastricht 2022 workshop and hackaton “Building the Jupyter Community in Musculoskeletal Imaging Research”.

Image I/O is based on [DOSMA](https://github.com/ad12/DOSMA) by Arjun Desai. A stripped-down version of DOSMA is present
in src/ormir_mids/dosma_io.
