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
	'''RSD damping factor accounting for photo-z error
	z(arr/float): redshift
	sigma_z(array/float): photo-z error
	
	return(float/array): Sigma_z
	
	'''
	cosmo = cosmology.setCosmology('planck18')	
	return (speed_of_light*.001/cosmo.Hz(z))*sigma_z/(1+z)

def attribute_bias(zs):
	'''bias as a function of redshift, based on the ICE_COLA results
	z(arr/float): redshift
	
	return(arr/float): bias of the galaxies
	
	'''
	
	b = .98+1.24*zs-(1.72*zs**2)+1.28*zs**3
	#b=np.array([1.58,1.59,1.68,1.82,2.02])#ICE-Cola bias from w(theta)
	#bins=np.array([0,.7,.8,.9,1.,5])
	#bias=[]
	#for i in range(len(bins)-1):
	
	#	if bins[i]<z<=bins[i+1]:
	#		bias.append(b[i])
	#bias=np.array([b[i] for i in range(len(bins)-1) if bins[i]<=z<=bins[i+1]])
	return b

def growth_values(z):
	'''Growth of structure values: D(z), f, beta
	z(arr/float): redshift
	return(dicio): dictionary with D(z), f(z), and beta
	
	'''
	cosmo = cosmology.setCosmology('planck18')
	D=cosmo.growthFactor(z)
	dDdz=cosmo.growthFactor(z,derivative=1)
	f=-(1+z)*dDdz/D
	beta=f/attribute_bias(z)
	dicio={}
	dicio['D']=D
	dicio['f']=f
	dicio['beta']=beta
	return dicio

def R_mu(mu,beta,Sigma_z):
	'''RSD accounting for photo-z error
	mu(array/float): cosine of angle to the line of sight
	beta(float/arr): beta
	Sigma_z(float/arr): damping factor
	
	'''
	k_eff=.12
	first_part=1+beta*mu**2
	second_part=np.exp(-(k_eff*mu*Sigma_z)**2)
	return (first_part**2)*second_part

def integrate_R(z,Sigma_z):

	'''Integrates R for n_eff
	z(arr/float):redshift
	Sigma_z(arr/float): damping factor
	
	return(tuple): yfloat,abserrfloat	
	'''
	return quad(R_mu, -1, 1, args=(beta,Sigma_z))


def wfkp(z,n_eff):
	'''
	The Ross et al. MNRAS 472, 4456–4468 (2017) weight FKP.
	z(arr/float): redshift
	n_eff(arr/float): effective number density
	
	return (arr/float): weights 

	'''

	k_eff=.12
	cosmo = cosmology.setCosmology('planck18')
	bias=attribute_bias(z)
	pk=cosmo.matterPowerSpectrum(k_eff,z)*bias**2
	D=cosmo.growthFactor(z)
	den=1+n_eff*pk
	num=bias*D
	return num/den
	
	
	
