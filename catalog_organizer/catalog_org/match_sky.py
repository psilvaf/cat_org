from astropy.io import fits
import numpy as np
from astropy.table import Table
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.coordinates import match_coordinates_sky

def match_cats(smaller_cat, catalog, upperlimit=2):
    """
    Match objects between two catalogs within a specified angular separation.
    
    Parameters
    ----------
    smaller_cat : astropy Table or dict
        The smaller catalog to match against the larger catalog
    catalog : astropy Table or dict
        The larger reference catalog
    upperlimit : float, optional
        Maximum angular separation in arcseconds (default: 2)
    
    Returns
    -------
    astropy Table
        Table with matched indices and angular separations (in arcseconds)
        Only rows with separations <= upperlimit are included
    """
    cat_RA = catalog['RA']
    cat_DEC = catalog['DEC']
    object_RA = smaller_cat['RA']
    object_DEC = smaller_cat['DEC']
    
    skycoord_cat = SkyCoord(cat_RA*u.degree, cat_DEC*u.degree, frame='icrs')
    skycoord_object = SkyCoord(object_RA*u.degree, object_DEC*u.degree, frame='icrs')
    
    idx, d2d, d3d = match_coordinates_sky(skycoord_object, skycoord_cat)
    separations = np.asarray(d2d.arcsecond)
    
    # Create table with all matches
    table = Table()
    table['idx'] = idx
    table['d2d'] = separations
    
    # Filter matches based on upperlimit
    good_matches = table[table['d2d'] <= upperlimit]
    
    return good_matches
