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
    photoz=np.array([float(bpz_photoz[i][1]) for i in range(len(bpz_photoz))])
    z_bmin=np.array([float(bpz_photoz[i][2]) for i in range(len(bpz_photoz))])
    z_bmax=np.array([float(bpz_photoz[i][5]) for i in range(len(bpz_photoz))])
    np.save(output_file,np.column_stack((photoz,z_bmin,z_bmax)))
    
    return

def bins(survey,outputfile):

    start = time.time()
    z_bin=np.arange(0,2.2,.2)
    binnedz=[[] for i in range(len(z_bin))]
    binnedra=[[] for i in range(len(z_bin))]
    binneddec=[[] for i in range(len(z_bin))]
    binnedw=[[] for i in range(len(z_bin))]
    with Pool() as pool:
        for i in range(len(z_bin)-1):
            for j in range(len(survey)):
                if z_bin[i]<=survey['Z'][j]<=z_bin[i+1]:
                    binnedz[i].append(survey['Z'][j])
                    binnedra[i].append(survey['RA'][j])
                    binneddec[i].append(survey['DEC'][j])
                    binnedw[i].append(survey['WTOT'][j])
    tab=[{} for i in range(len(z_bin))]
    for l in range(len(z_bin)):
        for k in range(len(tab)):
            tab[k]['Z']=binnedz[l]
            tab[k]['RA']=binnedra[l]
            tab[k]['DEC']=binneddec[l]
            tab[k]['WTOT']=binnedw[l]
            fit = Table(tab[k])
            fit.write(outputfile+str(l)+'.fits',format='fits',overwrite=True)
    end = time.time()
    print(end - start)
    return
