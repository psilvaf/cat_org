from scipy import stats
import numpy as np

def chunks(x, n):
    '''Divides in chunks with at least n objects for chunk'''
    xs=np.array(x)
    n = max(1, n)
    gen=(xs[i:i+n] for i in range(0, len(xs), n))
    return list(gen)
    
    
def bins0(num,data,z1,z2):
    bins=[[] for i in range(num)]
    z_bins=np.linspace(z1,z2,num)
    for j in range(len(data['Z'])):
        for i in range(len(z_bins)-1):
            if z_bins[i]<=data['Z'][j]<z_bins[i+1]:
                bins[i].append(data['Z'][j])
    med_z=np.array([np.mean(i) for i in bins])
    return med_z

def bins(num,data):
    bins=[[] for i in range(num)]
    z_bins=np.linspace(min(data['Z']),max(data['Z']),num)
    for j in range(len(data['Z'])):
        for i in range(len(z_bins)-1):
            if z_bins[i]<=data['Z'][j]<z_bins[i+1]:
                bins[i].append(data['Z'][j])
    med_z=np.array([np.mean(i) for i in bins])
    return med_z
 
def interval(sigma68,interv):
	mean, sigma = np.mean(sigma68), np.std(sigma68)

	conf_int = stats.norm.interval(interv, loc=mean, scale=sigma)
	return conf_int
