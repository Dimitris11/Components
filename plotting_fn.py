# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 01:18:23 2015

@author: Dimitris
"""

import matplotlib.pyplot as plt
x = [0,1,2]
y = [0,1,4]
#fig = plt.figure(figsize =(15,10))
#
#ax1 = fig.add_subplot(3,3,1)
#ax1.plot(x,y, color = 'blue', linestyle = 'dashed', linewidth = 2)
#ax1.set_title()
#ax1.grid(True)
#ax1.set_xlabel('x')
#ax1.set_ylabel('y')


fig, axes = plt.subplots(nrows=1, ncols=2)
fig.suptitle('sgds', fontsize = 28)
for ax in axes: 
    ax.plot(x, y, 'r') 
    ax.set_xlabel('x') 
    ax.set_ylabel('y') 
    ax.set_title('title')