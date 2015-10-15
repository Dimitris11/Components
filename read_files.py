# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:16:05 2015

@author: dimitris
"""

#from os import path
import numpy as np
import csv
import matplotlib.pyplot as plt

#f = open('sample1.csv', 'r')
#r = csv.reader(f, delimiter=';')
#headers = r.next() #if u want 1st row as heeaders 
#column = {}
#for h in headers:
#    column[h] = []
#
#for row in r:
#    for h, v in zip(headers, row):
#        column[h].append(v)

####################    OR      ######################

f = open('sample1.csv', 'r')
r = csv.reader(f, delimiter=';')
col = {}; headers=[]; shop = []; sea = []; oper =[];

for row in r:
    print row
    headers.append(row[0])
    sh = row[1:7]; se = row[7:12]; op = row[12:]; 
    shop.append(sh)
    sea.append(se)
    oper.append(op)

shop = np.array(shop[:], dtype = 'float')   
sea = np.array(sea[:], dtype = 'float')
oper = np.array(oper[:], dtype = 'float')

shop1 = np.array(shop[0], dtype='float')
shop2 = np.array(shop[1], dtype='float')
av1 = (shop1 + shop2)/2.

plt.plot(shop[0], av1)






