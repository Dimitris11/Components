# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:45:14 2015

@author: dimitris
"""
import numpy as np
import matplotlib.pyplot as plt

ph = np.load('Philippe.npz') # to load the npy file
th = np.load('Theodora.npz')
lara = np.load('Lara.npz')
gui = np.load('guillaume.npz')
vic = np.load('victor.npz')
fe = np.load('felix.npz')
cha = np.load('charles.npz')



fig, axes = plt.subplots(nrows=1, ncols=2)
fig.suptitle('Shop Tests', fontsize = 18)
for ax in axes: 
    ax.plot(, y, 'r') 
    ax.set_xlabel('x') 
    ax.set_ylabel('y') 
    ax.set_title('title')