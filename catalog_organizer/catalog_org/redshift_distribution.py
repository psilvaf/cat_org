from astropy.io import fits
import numpy as np
import os
import random
from astropy.table import Table
import time 

def random_selector(data,data2,dist):

    start = time.time()
    new=[i for i in range(len(data2)) if data2[i]==data[random.choice(dist)]]

    end = time.time()
    print(end - start)
    return new

def new_file(data2,new_ind,output):
	new={}
	for i in new_ind:
		new['Z']=data2['Z'][i]
		new['RA']=data2['RA'][i]
		new['DEC']=data2['DEC'][i]
	Table(new).write(output,overwrite=True)
	return
	
def z_eff(wfkp,wtot,z):

    w=np.array([wfkp[i]*wtot[i] for i in range(len(z))])
    w2=np.sum(w*z)/np.sum(w)
    return w2
