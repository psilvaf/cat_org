from astropy.io import fits
import numpy as np
import os
import pandas as pd
from multiprocessing import Pool
from astropy.table import Table

def handling_photoz(path,output_file):
    df = open(path, 'r')
    
    with Pool() as pool:
        lista=[]
        for y in df.readlines():
            if not y.startswith("#"):
                cols=y.strip()
                lista.append(cols)
    bpz_photoz=[lista[i].split(' ') for i in range(len(lista))]
    iden=np.array([float(bpz_photoz[i][0]) for i in range(len(bpz_photoz))])
    photoz=np.array([float(bpz_photoz[i][1]) for i in range(len(bpz_photoz))])
    z_bmin=np.array([float(bpz_photoz[i][2]) for i in range(len(bpz_photoz))])
    z_bmax=np.array([float(bpz_photoz[i][5]) for i in range(len(bpz_photoz))])
    np.save(output_file,np.column_stack((iden,photoz,z_bmin,z_bmax)))
    
    return 
