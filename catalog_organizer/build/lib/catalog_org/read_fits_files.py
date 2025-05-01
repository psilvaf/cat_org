from astropy.io import fits
import os
from pathlib import Path
from astropy.table import Table
import numpy as np

def read_data(data):
    '''Reads fits files from mocks
    return: astropy fits data
    
    '''
    galaxies_cat = fits.open(Path(data))[1].data
    return galaxies_cat
    
def join_nodes(names,output_path):
	
	z=[]
	dz=[]
	ra=[]
	dec=[]
	DATA=[]
	for i in range(len(names)):
		DATA.append(read_data(names[i]))
	for i in range(len(names)):
		z.append(DATA[i]['Z_COSMO'])
		dz.append(DATA[i]['DZ_RSD'])
		ra.append(DATA[i]['RA'])
		dec.append(DATA[i]['DEC'])
	new={}
	new['Z_COSMO']=np.hstack((z))
	new['RA']=np.hstack((ra))
	new['DEC']=np.hstack((dec))
	new['DZ_RSD']=np.hstack((dz))
	fit = Table(new)
	fit.write(output_path+'.fits',format='fits',overwrite=True)

	return
		








