from astropy.io import fits
import numpy as np
import os
import pandas as pd
from multiprocessing import Pool
from astropy.table import Table
import time

def pdf_photoz(path,output_file):
	data = open(path, 'r')
	distribution=[i for i in data.read().split('\n')][1:-1]
	with Pool() as pool:
		start = time.time()
		tables=[]
		for i in range(len(distribution)):
			tab=pd.DataFrame(distribution[i][:-1].split(' '),dtype=float).values
			tables.append(tab)
		end = time.time()
		multi_time = end - start
		print("Multiprocessing took {0:.2f} seconds".format(multi_time))
	final_table=np.array(tables).T
	np.save(output_file,final_table)
	return	

