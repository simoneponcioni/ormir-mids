"""
This is the muscle-bids base package providing basic I/O functionality for reading and writing DICOM and BIDS files.
The python representation of the data is the MedicalVolume class, provided by pyvoxel, with added attributes for BIDS.


Specifically, the MedicalVolumes returned have four additional attributes:
    - bids_header: a dictionary containing the information contained in the BIDS header
    - patient_header: a dictionary containing patient information
    - extra_header: a dictionary containing raw DICOM tags that are not part of the BIDS header
    - meta_header: a dictionary containing the meta DICOM information
"""
from voxel import MedicalVolume
from .utils.io import load_dicom, save_bids, load_dicom_with_subfolders, save_dicom, find_bids

__all__ = ['load_dicom', 'save_bids', 'load_dicom_with_subfolders', 'save_dicom', 'find_bids']

__version__ = '0.1.0'