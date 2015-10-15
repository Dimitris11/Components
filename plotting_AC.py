# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:16:17 2015

@author: dimitris
"""
#fit_fn(x)
fig, ax = plt.subplots()
for vessel in vessels: 
    x = v[vessel][2][21]
    y = v[vessel][2][22]
    fit = np.polyfit(x,y,1)
    fit_fn = np.poly1d(fit) 
    ax.plot(x, y, 'o', label= vessel) 
ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_title('title');
ax.grid(True);
ax.legend(loc=2); # upper left corner 