
from astropy.io import fits
import numpy as np
import random
from scipy.interpolate import CubicSpline
from scipy.interpolate import splev, splrep

def get_dist_function(data):

	'''Computes the histogram and interpolates the n(z) function
	data (arr):: redshift column name
	
	return: function	
	'''
	# Interpolation
	dist_z=np.histogram(data,bins=100,density=True)
	spl0 = splrep(np.linspace(min(data),max(data),len(dist_z[0])), dist_z[0], s=0.001, 	per=False)
	x2 = np.linspace(min(data),max(data), 200)
	y2 = splev(x2, spl0)
	return CubicSpline(x2, y2)
	

def uniform_proposal(l,h):
    '''Returns random uniform distributioin
    l(float): lower limit
    h(float): upper limit
    
    return (float): random number 
    '''
    return np.random.uniform(l,h)

def metropolis_sampler(redshift,p, nsamples,proposal=uniform_proposal):
    '''Generates random redshift numbers from a predefinef distribution 
    using the Metropolis sampling method.
    
    redshift(array): redshift
    p(function): the distribution function
    nsamples(int): size of the new distribution
    proposal(function): function to generate random numbers
    '''
    l = min(redshift)
    h=max(redshift)
    x=min(redshift) # start somewhere
    for i in range(nsamples):
        trial = proposal(l,h) # random neighbour from the proposal distribution
        acceptance = p(trial)/p(x)
        # accept the move conditionally
        if np.random.uniform()<acceptance:
            x = trial

        yield x

