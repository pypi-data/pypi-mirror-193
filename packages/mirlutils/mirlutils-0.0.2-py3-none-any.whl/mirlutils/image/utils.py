import numpy as np
import SimpleITK as sitk 

def dicom_to_nifti(src, dst):
    """
    src : dicom directory path
    dst : nifti save path with .nii suffix 
    """
    reader = sitk.ImageSeriesReader()
    dicoms = reader.GetGDCMSeriesFileNames(str(src))
    reader.SetFileNames(dicoms)
    image = reader.Execute()
    sitk.WriteImage(image, str(dst))

def get_array(file, dtype=np.float64):
    """
    Get numpy array from .img, .dcm, .hdr, .nii
    file : path
    """
    temp = sitk.ReadImage(str(file))
    return sitk.GetArrayFromImage(temp).astype(dtype)

def windowing(array, wl, ww, normalize=True):
    """
    array : target array to adjust window setting
    wl : window level
    ww : window width
    normalize : return values in range (0-1) 
    """
    lower_bound = wl - ww/2
    upper_bound = wl + ww/2

    if normalize:
        return (np.clip(array, lower_bound, upper_bound) - lower_bound) / ww
    else:
        return np.clip(array, lower_bound, upper_bound) 