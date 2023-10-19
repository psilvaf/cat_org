from astropy.io import fits
import os
from pathlib import Path


def read_data(data):
    '''Reads fits files
    return: astropy fits data
    
    '''
    galaxies_cat = fits.open(Path(data))[1].data
    return galaxies_cat
    
def join_nodes(names,output_path):
	
	z=[]
	dz=[]
	ra=[]
	dec=[]
	DATA=np.zeros(len(names))
	for i in range(len(names)):
		DATA[i]=read_data(names[i])
	for i in range(len(names)):
		z.append(DATA[i]['Z_COSMO'])
		dz.append(DATA[i]['DZ_RSD'])
		ra.append(DATA[i]['RA'])
		dec.append(DATA[i]['DEC'])
	new={}
	new['Z']=z
	new['RA']=ra
	new['DEC']=dec
	new['DZ_RSD']=dz
	fit = Table(d)
	fit.write(output_path+'.fits',format='fits',overwrite=True)
	return
		







