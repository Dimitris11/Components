# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:16:17 2015

@author: dimitris

Plot per vessel
"""

param_x = 0
param_y = 23

col = ['blue', 'red', 'green']
l = ['Shop', 'Sea', 'Oper']

fig, ax = plt.subplots()
#fig.suptitle(headers[param_y])
for i,vessel in enumerate(vessels):
    
#vessel = 'Lara'

    ax = fig.add_subplot(3,3,i)
    for a in [0, 1, 2]: 
        x = v[vessel][a][param_x]
        y = v[vessel][a][param_y]
        fit = np.polyfit(x,y,1)
        fit_fn = np.poly1d(fit) 
        ax.plot(x, y, 'o', color = col[a], label= l[a])
        ax.plot(x, fit_fn(x), '-',color= col[a])
        ax.set_ylim([0.9, 1.0])
    ax.set_xlabel(headers[param_x]) 
    ax.set_ylabel(headers[param_y]) 
    ax.set_title(vessel);
    ax.grid(True);
    ax.legend(loc=2); # upper left corner, loc=2
    
#    
#fig.tight_layout()