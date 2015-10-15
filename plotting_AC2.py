# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:16:17 2015

@author: dimitris

Plot per vessel
"""

param_x = 0
param_y = 23
col = ['blue', 'red', 'green', 'black', 'orange', 'magenta', 'cyan']
fig, ax = plt.subplots()
l = ['Shop', 'Sea', 'Oper']
for a, vessel in enumerate(vessels): 
    x = v[vessel][1][param_x]
    y = v[vessel][1][param_y]
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit) 
    ax.plot(x, y, 'o', color = col[a], label = vessel)
    ax.plot(x, fit_fn(x), '-',color= col[a])
ax.set_ylim([0.9, 1.0])
ax.set_xlabel(headers[param_x]) 
ax.set_ylabel(headers[param_y]) 
#ax.set_title('title');
ax.grid(True);
ax.legend(loc=2); # upper left corner, loc=2