from astropy.io import fits
import numpy as np
import os
import random
from astropy.table import Table
import time 

def random_selector(data,data2,ind):
    '''Randomly chooses a distribution comparing to another.
    data(array): reference data
    data2(array): second distribution
    dist(int): size of data
    
    return (list): distribution from data2 that fits in data
    '''
    start = time.time()
    new=[i for i in range(len(data2)) if data2[i]==data[random.choice(ind)]]

    end = time.time()
    print(end - start)
    return new

	
def z_eff(wfkp,wtot,z):
    '''Computes the effective redshift of a survey
    wfkp(array): Feldman, Kaiser, Peacock weight
    wtot(array): survey weights
    z(array): redshift
    
    return (float): zeff
    '''
    w=np.array([wfkp[i]*wtot[i] for i in range(len(z))])
    w2=np.sum(w*z)/np.sum(w)
    return w2
    
def smooth(y, box_pts):
    '''Smooths an array distribution using a convolution.
    y (array): distribution
    box_pts (int): resolution to smooth
    
    return(array): new smoothed distribution with the same size as the original
    '''

    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth
