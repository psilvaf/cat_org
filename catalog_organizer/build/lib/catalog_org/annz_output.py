import matplotlib.pyplot as plt
from astropy.io import fits
import numpy as np
import os
import pandas as pd
from multiprocessing import Pool
from astropy.table import Table


def read_files(path):
    '''Reads ANNz output +csv files
    path(str): path of file
    return: list of lines from the file
    
    '''
    File = [open(i, 'r') for i in path]
    lista=[[y.strip()for y in File[i].readlines()] for i in range(len(File))]
    return lista
    
def split1(lista0):
    '''Split the comma separated lines from ANNz files
    lista0(list): lines from a file
    return: matrix with the lines and columns from the file
    '''
    lista=[lista0[i].split(',') for i in range(len(lista0))]
    matrix=np.array([np.array([float(lista[i][j]) for j in range(len(lista[i]))]) for i in range(len(lista))])
    return matrix
