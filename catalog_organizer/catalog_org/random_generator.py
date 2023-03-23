
from astropy.io import fits
import numpy as np
import random
from scipy.interpolate import CubicSpline
from scipy.interpolate import splev, splrep

def get_dist_function(data):
	# Interpolation
	dist_z=np.histogram(data['Z'],bins=100,density=True)
	spl0 = splrep(np.linspace(min(data['Z']),max(data['Z']),len(dist_z[0])), dist_z[0], s=0.001, 	per=False)
	x2 = np.linspace(min(data['Z']),max(data['Z']), 200)
	y2 = splev(x2, spl0)
	return CubicSpline(x2, y2)
	

def uniform_proposal(l,h):
    return np.random.uniform(l,h)

def metropolis_sampler(data,p, nsamples,proposal=uniform_proposal):
    l = min(data['Z'])
    h=max(data['Z'])
    x=min(data['Z']) # start somewhere
    for i in range(nsamples):
        trial = proposal(l,h) # random neighbour from the proposal distribution
        acceptance = p(trial)/p(x)
        # accept the move conditionally
        if np.random.uniform()<acceptance:
            x = trial

        yield x

