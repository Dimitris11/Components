# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:16:05 2015

@author: dimitris
"""

#from os import path
import numpy as np
import csv
import matplotlib.pyplot as plt
#import scipy.io as sio

vessels = ['Philippe','Felix', 'Theodora', 'Victor', 'Charles', 'Guillaume', 'Lara']
v = dict.fromkeys(vessels)
for vessel in vessels:
    f = open(vessel +'_AC.csv', 'r')
    r = csv.reader(f, delimiter=';')
    mat = {}; headers=[]; shop = []; sea = []; oper =[];
    dates = r.next()
    for row in r:
    #   print row
        headers.append(row[0])
        sh = row[1:7]; se = row[7:12]; op = row[12:]; 
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
    dtaw = shop[15]-shop[16]
    dtww = shop[17]-shop[16]
    dtaw_Ta = dtaw/shop[2]
    dtww_Ta = dtww/shop[2]
    eff = (shop[14]-shop[15])/(shop[14]-shop[16])
    shop = np.row_stack((shop,dtaw, dtww, dtaw_Ta, dtww_Ta, eff))
    
    sea = np.array(sea[:], dtype = 'float')
    ac_ain=(sea[4]+sea[5])/2.
    ac_aout=(sea[6]+sea[7])/2.
    ac_win=(sea[8]+sea[9])/2.
    ac_wout=(sea[10]+sea[11])/2.
    dp_ac=(sea[12]+sea[13])/2.
    sea = np.row_stack((sea, ac_ain, ac_aout,ac_win,ac_wout,dp_ac))
    dtaw = sea[15]-sea[16]
    dtww = sea[17]-sea[16]
    dtaw_Ta = dtaw/sea[2]
    dtww_Ta = dtww/sea[2]
    eff = (sea[14]-sea[15])/(sea[14]-sea[16])
    sea = np.row_stack((sea,dtaw, dtww, dtaw_Ta, dtww_Ta, eff))
    
    oper = np.array(oper[:], dtype = 'float')
    ac_ain=(oper[4]+oper[5])/2.
    ac_aout=(oper[6]+oper[7])/2.
    ac_win=(oper[8]+oper[9])/2.
    ac_wout=(oper[10]+oper[11])/2.
    dp_ac=(oper[12]+oper[13])/2.
    oper = np.row_stack((oper, ac_ain, ac_aout,ac_win,ac_wout,dp_ac))
    dtaw = oper[15]-oper[16]
    dtww = oper[17]-oper[16]
    dtaw_Ta = dtaw/oper[2]
    dtww_Ta = dtww/oper[2]
    eff = (oper[14]-oper[15])/(oper[14]-oper[16])
    oper = np.row_stack((oper,dtaw, dtww, dtaw_Ta, dtww_Ta,eff)) 
    
    mat['shop']=shop
    mat['sea']=sea
    mat['oper']=oper
    
    v[vessel] = [shop, sea, oper]
    #filemat = 'philippe.mat'
    #sio.savemat(filemat, mat)
    #np.vstack((philippe['shop'], np.atleast_2d(philippe['shop'][4]+philippe['shop'][5])/2.))
    np.savez(vessel+'.npz', **mat)
    
    #a = np.load('philippe.npy').item() # to load the npy file
headers.extend(['Tsc_Ain_av','Tsc_Aout_av', 'Tsc_Win_av', 'Tsc_Wout_av', \
'DP_ac_av', 'DTaw', 'DTww', 'DTaw/Tamb', 'DTww/Tamb', 'Effectiveness' ])

lara = v['Lara']
ph = v['Philippe']
cha = v['Charles']
fe = v['Felix']
gui = v['Guillaume']
th = v['Theodora']
vi = v['Victor']
    
    
   
