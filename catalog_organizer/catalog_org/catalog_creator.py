from astropy.io import fits
from astropy.table import Table
import numpy as np
import os
import pandas as pd

def cataloger(data,output_file):
    '''Convert fits file to csv for BPZ
    data(str): file path
    output_file(str)
    return saves a csv file space separated
    '''
    galaxies_cat = fits.open(os.path.join(data))[1].data
    galaxies_cat=pd.DataFrame(galaxies_cat)
    galaxies_cat.to_csv(output_file,sep=' ',index=False,header=False)
    
    return 





