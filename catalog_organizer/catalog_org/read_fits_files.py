from astropy.io import fits
import os
from pathlib import Path


def read_data(data):
    '''Reads fits files
    return: astropy fits data
    
    '''
    galaxies_cat = fits.open(Path(data))[1].data
    return galaxies_cat
