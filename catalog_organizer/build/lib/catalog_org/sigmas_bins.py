from scipy import stats
import numpy as np

def chunks(x, n):
    '''Divides in chunks with at least n objects for chunk
    x(array/list):array or list to be divided
    n(int): number of chunks
    return: list of lists with size n    
    '''
    xs=np.array(x)
    n = max(1, n)
    gen=(xs[i:i+n] for i in range(0, len(xs), n))
    return list(gen)
    
    
def bins0(num,data,z1,z2,zname):
    '''
    Divides a fits file in bins and computes the average redshift of each bin.
    num(int): number of bins
    data(fits data): fits data
    z1(float): minimum redshift
    z2(float): maximum redshift
    zname(str): name of redshift column
    
    return(arr): average redshift of each bin  
    
    '''
    bins=[[] for i in range(num)]
    z_bins=np.linspace(z1,z2,num)
    for j in range(len(data[zname])):
        for i in range(len(z_bins)-1):
            if z_bins[i]<=data[zname][j]<z_bins[i+1]:
                bins[i].append(data[zname][j])
    med_z=np.array([np.mean(i) for i in bins])
    return med_z

def bins(num,data):
    '''
    Divides a fits file in bins and computes the average redshift of each bin.
    This considers just the min and max values of the survey redshift
    
    num(int): number of bins
    data(fits data): fits data
    zname(str): name of redshift column
    
    return(arr): average redshift of each bin  
    
    '''
    bins=[[] for i in range(num)]
    z_bins=np.linspace(min(data['Z']),max(data['Z']),num)
    for j in range(len(data['Z'])):
        for i in range(len(z_bins)-1):
            if z_bins[i]<=data['Z'][j]<z_bins[i+1]:
                bins[i].append(data['Z'][j])
    med_z=np.array([np.mean(i) for i in bins])
    return med_z
 
def interval(bias,interv):
	'''Computes the confidence interval of "interv" level from the bias 
	between the spec-z and photo-z.
	
	bias(arr): bias between spec-z and photo-z
	interv(float): either 0.68, 0.95, .997
	
	return (tuple): (-interv,+interv)
	
	'''
	mean, sigma = np.mean(bias), np.std(bias)

	conf_int = stats.norm.interval(interv, loc=mean, scale=sigma)
	return conf_int
