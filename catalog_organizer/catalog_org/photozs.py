from astropy.io import fits
import numpy as np
import os
import pandas as pd
from multiprocessing import Pool
from astropy.table import Table

def handling_photoz(path,output_file):
    '''Writes a numpy array from the BPZ output
    Array columns: photo_z, photo_z+1_sigma, photo_z-1_sigma
    
    
    path(str): path to file
    output_file(str)
    return: matrix with photo_z, photo_z+1_sigma, photo_z-1_sigma
    
    '''
    df = open(path, 'r')
	
    lista=[y.strip() for y in df.readlines() if not y.startswith("#")]

    bpz_photoz=[lista[i].split(' ') for i in range(len(lista))]
    photoz=np.array([float(bpz_photoz[i][1]) for i in range(len(bpz_photoz))])
    z_bmin=np.array([float(bpz_photoz[i][2]) for i in range(len(bpz_photoz))])
    z_bmax=np.array([float(bpz_photoz[i][5]) for i in range(len(bpz_photoz))])
    np.save(output_file,z_bmin)
    np.column_stack((photoz,z_bmin,z_bmax))
    return

