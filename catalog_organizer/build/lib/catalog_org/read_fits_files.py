from astropy.io import fits
import os
from astropy.table import Table

def read_data(data):

    galaxies_cat = fits.open(os.path.join(data))[1].data
    return galaxies_cat
