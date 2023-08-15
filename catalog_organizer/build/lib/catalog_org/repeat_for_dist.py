import numpy as np



def construct_dist(z_dist,pdfs,bin_size):
	'''Construct a set of redshift values from pdfs'''
	Dist=[]
	for j in range(len(pdfs)):
		Dist.append([np.repeat(z_dist[i],pdfs[j][i]) for i in range(bin_size)])
	return [np.concatenate(Dist[i]) for i in range(len(Dist))]
