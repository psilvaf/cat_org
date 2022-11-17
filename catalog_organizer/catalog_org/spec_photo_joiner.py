import numpy as np
from os.path import dirname, abspath, join as pjoin
from astropy.io import fits
import os
from astropy.table import Table


def spec_photo(data1,data2,output_file,zphoto=False, weight=False, mags=False):
	"""
	Reads the data in the SDSS format and joins caps and 
	
	:data1,data2: string, name of the file
		
	:output_file: string, name of outputfile
	
	:zphoto,weight,mags: if True saves zphoto,weight, and magnitudes (ugriz), default is False.
	
	:return: file in fits format
	
	:raises: The file must be in fits format
	
	"""
	galaxies_cat1 = fits.getdata(os.path.join(data1))
	galaxies_cat1=Table(galaxies_cat1)
	galaxies_cat2 = fits.getdata(os.path.join(data2))
	galaxies_cat2=Table(galaxies_cat2)
	d={'Z':galaxies_cat1['Z'],'RA':galaxies_cat1['RA'],'DEC':galaxies_cat1['DEC']}
	if zphoto==True:
		photoz=galaxies_cat2['pZ']
		d['pz']=photoz
	if weight==True:
		w=galaxies_cat1['WEIGHT_SYSTOT']
		d['WEIGHT_SYSTOT']=w
	if mags==True:
		mags=galaxies_cat2['MODELMAG']
		mags_err=galaxies_cat2['MODELMAGERR']
		d['u']=[mags[i][0] for i in range(len(mags))]
		d['g']=[mags[i][1] for i in range(len(mags))]
		d['r']=[mags[i][2] for i in range(len(mags))]
		d['i']=[mags[i][3] for i in range(len(mags))]
		d['z']=[mags[i][4] for i in range(len(mags))]
		d['uerr']=[mags_err[i][0] for i in range(len(mags_err))]
		d['gerr']=[mags_err[i][1] for i in range(len(mags_err))]
		d['rerr']=[mags_err[i][2] for i in range(len(mags_err))]
		d['ierr']=[mags_err[i][3] for i in range(len(mags_err))]
		d['zerr']=[mags_err[i][4] for i in range(len(mags_err))]
	fit = Table(d)
	fit.write(output_file +'.fits',format='fits',overwrite=True)
	print(len(d['Z']))
	return 

def cap_joiner(NGC,SGC,output_file):
	galaxies_cat1 = fits.getdata(os.path.join(NGC))
	galaxies_cat1=Table(galaxies_cat1)

	galaxies_cat2 = fits.getdata(os.path.join(SGC))
	galaxies_cat2=Table(galaxies_cat2)
	d={}
	d['Z']=np.append(galaxies_cat1['Z'],galaxies_cat2['Z'])
	d['RA']=np.append(galaxies_cat1['RA'],galaxies_cat2['RA'])
	d['DEC']=np.append(galaxies_cat1['DEC'],galaxies_cat2['DEC'])
	d['WEIGHT_SYSTOT']=np.append(galaxies_cat1['WEIGHT_SYSTOT'],galaxies_cat2['WEIGHT_SYSTOT'])
	d['u']=np.append(galaxies_cat1['u'],galaxies_cat2['u'])
	d['g']=np.append(galaxies_cat1['g'],galaxies_cat2['g'])
	d['r']=np.append(galaxies_cat1['r'],galaxies_cat2['r'])
	d['i']=np.append(galaxies_cat1['i'],galaxies_cat2['i'])
	d['z']=np.append(galaxies_cat1['z'],galaxies_cat2['z'])
	d['uerr']=np.append(galaxies_cat1['uerr'],galaxies_cat2['uerr'])
	d['gerr']=np.append(galaxies_cat1['gerr'],galaxies_cat2['gerr'])
	d['rerr']=np.append(galaxies_cat1['rerr'],galaxies_cat2['rerr'])
	d['ierr']=np.append(galaxies_cat1['ierr'],galaxies_cat2['ierr'])
	d['zerr']=np.append(galaxies_cat1['zerr'],galaxies_cat2['zerr'])
	fit = Table(d)
	fit.write(output_file +'.fits',format='fits',overwrite=True)
	return print(len(d['Z']))
