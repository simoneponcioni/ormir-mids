# ormir-bids
I/O of standardized data formats for Open and Reproducible Musculoskeletal Imaging Research ([ORMIR](https://ormircommunity.github.io/)). Based on the [BIDS](https://bids.neuroimaging.io/) data structure.

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

## Installation

### Dependencies
To install `ormir-bids`, run the code below, noting this list of [dependencies](dependencies.md).

It is recommended to install `ormir-mids` in a separate virtual environment:
```commandline
conda env create -n ormir-bids
conda activate ormir-bids
```

Clone the git repository:
```shell
git clone https://github.com/ormir-bids/ormir-bids.git
```
Now we can install the package using `pip`. This will also install the required dependencies.
```shell
cd ormir-bids
pip install .
pip install --upgrade nibabel # the default nibabel has bugs
```

## Usage
`ormir-bids` can be used in two ways: 
    
1. Running `dcm2mbids` as an executable to convert DICOM data to the BIDS format.
2. Importing `ormir-bids` as a Python module to find, load, and interrogate BIDS-format data.

The commandline script is called `dcm2mbids.exe`. To view the commandline script help type
```commandline
dcm2mbids -h
```

To use `ormir-bids` within Python, import the following modules
```python
from muscle_bids.utils.io import find_bids, load_bids
import nibabel as nib
```

For a detailed description of how to use `ormir-bids` see the following notebook
#### [ORMIR-bids usage: dcm2mbids](examples/jupyter/Muscle-bids_dcm2mbids.ipynb) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](examples/jupyter/Muscle-bids_dcm2mbids.ipynb)

### Medical volume manipulation within Pyhon
`ormir-bids` can be used within Python to load, manipule and visualize medical volume datasets, without convertion to the BIDS format.

- Load a DICOM file to a MedicalVolume object

```python
from muscle_bids.utils.io import load_dicom
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


Examples of how to use `ormir-bids` for common data handling, image manipulation and processing tasks within Python can be found in this notebook
#### [ORMIR-bids usage: MedicalVolume class](examples/jupyter/Muscle-bids_MedicalVolume_tests.ipynb) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](examples/jupyter/Muscle-bids_MedicalVolume_tests.ipynb)

## Acknowledgement

This package was developed thanks to the support of the JCMSK community during the Maastricht 2022 workshop and hackaton “Building the Jupyter Community in Musculoskeletal Imaging Research”.

Image I/O is based on [DOSMA](https://github.com/ad12/DOSMA) by Arjun Desai. A stripped-down version of DOSMA is present
in muscle-bids/dosma_io.
