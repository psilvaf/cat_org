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
	'''RSD damping factor accounting for photo-z error'''
	cosmo = cosmology.setCosmology('planck18')	
	return (speed_of_light*.001/cosmo.Hz(z))*sigma_z/(1+z)

def attribute_bias(z):
	'''bias as a function of redshift, based on the ICE_COLA results'''
	b=np.array([1.58,1.59,1.68,1.82,2.02])#ICE-Cola bias from w(theta)
	bins=np.array([0,.7,.8,.9,1.,2])
	bias=np.array([b[i] for i in range(len(bins)-1) if bins[i]<=z<=bins[i+1]])
	return bias

def growth_values(z):
	'''Growth of structure values: D(z), f, beta'''
	cosmo = cosmology.setCosmology('planck18')
	D=cosmo.growthFactor(z)
	dDdz=cosmo.growthFactor(z,derivative=1)
	f=-(1+z)*dDdz/D
	beta=np.array([f[i]/attribute_bias(z[i]) for i in range(len(z))])
	dicio={}
	dicio['D']=D
	dicio['f']=f
	dicio['beta']=beta
	return dicio

def R_mu(mu,beta,Sigma_z):
	'''RSD accounting for photo-z error'''
	k_eff=.12
	first_part=1+beta*mu**2
	second_part=np.exp(-(k_eff*mu*Sigma_z)**2)
	return (first_part**2)*second_part

def integrate_R(z,Sigma_z):
	return quad(R_mu, -1, 1, args=(beta,Sigma_z))


def wfkp(z,n_eff):
	k_eff=.12
	cosmo = cosmology.setCosmology('planck18')
	bias=np.concatenate([attribute_bias(i) for i in z])
	print(bias)
	pk=cosmo.matterPowerSpectrum(k_eff,z)*bias**2
	D=cosmo.growthFactorUnnormalized(z)
	den=1+n_eff*pk
	num=bias*D
	return num/den
	
	
	
