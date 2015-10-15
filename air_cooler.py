# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:16:05 2015

@author: dimitris
"""

#from os import path
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.io as sio
 
f = open('Philippe_AC.csv', 'r')
r = csv.reader(f, delimiter=';')
mat = {}; headers=[]; shop = []; sea = []; oper =[];
dates = r.next()
for row in r:
#   print row
    headers.append(row[0])
    sh = row[1:7]; se = row[7:14]; op = row[14:]; 
    shop.append(sh)
    sea.append(se)
    oper.append(op)

shop = np.array(shop[:], dtype = 'float')
ac_ain=(shop[4]+shop[5])/2.
ac_aout=(shop[6]+shop[7])/2.
ac_win=(shop[8]+shop[9])/2.
ac_wout=(shop[10]+shop[11])/2.
dp_ac=(shop[12]+shop[13])/2.
shop = np.row_stack((shop, ac_ain, ac_aout,ac_win,ac_wout,dp_ac))

sea = np.array(sea[:], dtype = 'float')
ac_ain=(sea[4]+sea[5])/2.
ac_aout=(sea[6]+sea[7])/2.
ac_win=(sea[8]+sea[9])/2.
ac_wout=(sea[10]+sea[11])/2.
dp_ac=(sea[12]+sea[13])/2.
sea = np.row_stack((sea, ac_ain, ac_aout,ac_win,ac_wout,dp_ac))

oper = np.array(oper[:], dtype = 'float')
ac_ain=(oper[4]+oper[5])/2.
ac_aout=(oper[6]+oper[7])/2.
ac_win=(oper[8]+oper[9])/2.
ac_wout=(oper[10]+oper[11])/2.
dp_ac=(oper[12]+oper[13])/2.
oper = np.row_stack((oper, ac_ain, ac_aout,ac_win,ac_wout,dp_ac))

mat['shop']=shop
mat['sea']=sea
mat['oper']=oper

#filemat = 'philippe.mat'
#sio.savemat(filemat, mat)
#np.vstack((philippe['shop'], np.atleast_2d(philippe['shop'][4]+philippe['shop'][5])/2.))
np.savez('philippe.npz', **mat)
ph = np.load('philippe.npz') # to load the npy file
#a = np.load('philippe.npy').item() # to load the npy file




