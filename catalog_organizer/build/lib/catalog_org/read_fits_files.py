from astropy.io import fits
import os
from astropy.table import Table
from pathlib import Path


def read_data(data):

    galaxies_cat = fits.open(Path(data))[1].data
    return galaxies_cat
