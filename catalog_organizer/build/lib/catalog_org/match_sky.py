from astropy.io import fits
import numpy as np
import os
from astropy.table import Table
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import match_coordinates_sky

def match_cats(smaller_cat,catalog,names=('RA','DEC','RA','DEC'),upperlimit=16):

    """    
    from a smaller catalog, find the objects indexes that are in a larger catalog 
    as long as the angular distance is smaller than upperlimit
    
    
    smaller_cat,catalog: path to fits file
    names: tuple with the cat's coords names(str)
    upperlimit: max angle separation in degrees
    
    """
    catalog1=fits.open(os.path.join(catalog))[1].data
    catalog2=fits.open(os.path.join(smaller_cat))[1].data
    if names==('RA','DEC','RA','DEC'):
    	cat_RA = catalog1['RA']
    	cat_DEC = catalog1['DEC']
    	object_RA = catalog2['RA']
    	object_DEC = catalog2['DEC']
    else:
    	cat_RA = catalog2[names[0]]
    	cat_DEC = catalog2[names[1]]
    	object_RA = catalog1[names[2]]
    	object_DEC = catalog1[names[3]]
    skycoord_cat = SkyCoord(cat_RA*u.degree,cat_DEC*u.degree, frame='icrs')
    skycoord_object = SkyCoord(object_RA*u.degree,object_DEC*u.degree, frame='icrs')
    idx, d2d, d3d = match_coordinates_sky(skycoord_cat, skycoord_object)
    separations = np.asarray(d2d)*3600.0
    table={}
    table['idx']=idx
    table['d2d']=separations
    table=Table(table)
    table = table[(table['d2d']<=upperlimit)]
    return table['idx']
