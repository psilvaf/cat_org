from astropy.io import fits
import numpy as np
import os
from astropy.table import Table
import astropy.units as u
from scipy.interpolate import InterpolatedUnivariateSpline
from colossus.cosmology import cosmology
from scipy.integrate import quad
import matplotlib.pyplot as plt
from scipy.constants import speed_of_light

def Sigma(z,sigma_z):
	cosmo = cosmology.setCosmology('planck18')	
	return (speed_of_light/cosmo.Hz(z))*sigma_z/(1+z)

def attribute_bias(z):
	b=np.array([1.58,1.59,1.68,1.82,2.02])#ICE-Cola bias from w(theta)
	bins=np.array([.6,.7,.8,.9,1.,1.1])
	bias=np.array([b[i] for i in range(len(bias)-1) if bins[i]<=z<=bins[i+1]])
	return bias

def R_mu(mu,z,Sigma_z):
	k_eff=.12
	a=1/(1+z)
	cosmo = cosmology.setCosmology('planck18')
	D=cosmo.growthFactorUnnormalized(z)
	f=-np.gradient(np.log(D),np.log(1+z))
	beta=np.array([f[i]/attribute_bias(z[i]) for i in range(len(z))])
	first_part=1+beta*mu**2
	second_part=np.exp(-(k_eff*mu*Sigma_z)**2)
	return first_par/*second_part

def integrate_R(z,Sigma_z):
	return quad(R_mu, -1, 1, args=(z,Sigma_z))


	
	
	
	
