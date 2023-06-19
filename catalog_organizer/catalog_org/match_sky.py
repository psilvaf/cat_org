from astropy.io import fits
import numpy as np
from astropy.table import Table
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import match_coordinates_sky

def match_cats(smaller_cat,catalog,upperlimit=2):

    """    
    from a smaller catalog, find the objects indexes that are in a larger catalog 
    as long as the angular distance is smaller than upperlimit
    
    
    smaller_cat,catalog: path to fits file
    names: tuple with the cat's coords names(str)
    upperlimit: max angle separation in degrees
    return: astropy table with the indexes and angular separations of the matched galaxies
    """
    cat_RA = catalog['RA']
    cat_DEC = catalog['DEC']
    object_RA = smaller_cat['RA']
    object_DEC = smaller_cat['DEC']
    skycoord_cat = SkyCoord(cat_RA*u.degree,cat_DEC*u.degree, frame='icrs')
    skycoord_object = SkyCoord(object_RA*u.degree,object_DEC*u.degree, frame='icrs')
    idx, d2d, d3d = match_coordinates_sky(skycoord_cat, skycoord_object)
    separations = np.asarray(d2d)*3600.0
    table={}
    table['idx']=idx
    table['d2d']=separations
    table=Table(table)
    return table
    table = table[(table['d2d']<=upperlimit)]
    return table['idx']
