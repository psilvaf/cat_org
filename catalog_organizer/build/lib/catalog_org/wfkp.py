from nbodykit.lab import *
from nbodykit import setup_logging, style,cosmology,algorithms
from astropy.io import fits
import numpy as np
import os
from scipy.interpolate import InterpolatedUnivariateSpline


def read_data(data):
    galaxies_cat =FITSCatalog(os.path.join(data))
    return galaxies_cat
    
def wfkp(cat, cat_rand, data_z,rand_z,data_ra,data_dec):


	# Planck18 mocks cosmology
	cosmo=cosmology.cosmology.Cosmology(h=0.6766,Omega0_m=0.3153,n_s=0.9649,sigma8=0.811)


	# add Cartesian position column
	cat['pos'] = transform.SkyToCartesian(cat[data_ra], cat[data_dec], cat[data_z], cosmo=cosmo)
	fraction=4108.47/ 41252.96125
	zhist=algorithms.zhist.RedshiftHistogram(cat_rand,fraction,cosmo,redshift=rand_z)

	# re-normalize to the total size of the data catalog
	alpha = 1.0 * len(cat) / len(cat_rand)

	# add n(z) from randoms to the FKP source
	nofz = InterpolatedUnivariateSpline(zhist.bin_centers, alpha*zhist.nbar)

	cat['NZ']=nofz(cat[data_z])
	cat_rand['NZ']=nofz(cat_rand[rand_z])

	fkp = FKPCatalog(cat, rand)
	fkp['data/FKPWeight'] = 1.0 / (1 + fkp['data/NZ'] * 1e4)
	fkp['randoms/FKPWeight'] = 1.0 / (1 + fkp['randoms/NZ'] * 1e4)

	return np.array(fkp['data/FKPWeight']),print(np.array(fkp['randoms/FKPWeight']))

