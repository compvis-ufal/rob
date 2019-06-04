#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:40:53 2019

@author: tiago
"""

#%%
import numpy as np

def rotn(n, t):
    """
    R = ROTN(N, T)
    Function that returns the 3x3 rotation matrix around diretion 'N' of
    angle T:
        - n: unitary vector in R^3.
        - T: rotation angle in degrees.
    """

    # Guarantees that |n| = 1.
    if np.linalg.norm(n) != 1:
        n = n/np.linalg.norm(n)
    
    nx = n[0]
    ny = n[1]
    nz = n[2]
    
    t = np.deg2rad(t)
    
    ct = np.cos(t)
    vt = 1 - ct
    st = np.sin(t)

    return np.array(
            [
                    [nx**2*vt + ct,     nx*ny*vt - nz*st,   nx*nz*vt + ny*st],
                    [nx*ny*vt + nz*st,  ny**2*vt + ct,      ny*nz*vt - nx*st],
                    [nx*nz*vt - ny*st,  ny*nz*vt + nx*st,   nz**2*vt + ct]
            ])

#%% Example - Rotate [0, 1, 0] of 240 deg around direction [1, 1, 1] to 
#   get [1, 0, 0] as a result.
n = np.array([1, 1, 1])
r = rotn(n,240)
pl = np.array([0, 1, 0])
p = np.matmul(r, pl)

#%% Exmple - Make multiple rotations of increasing angles:
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

t = np.linspace(0, 360, 35)
p = np.zeros((3,len(t)))
for i in range(len(t)):
    print(t[i])
    p[:,i] = np.matmul(rotn(n,t[i]), np.array([0,1,0]).reshape(3,1)).reshape(3,)
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax = axes3d(fig)
xs = p[0, :]
ys = p[1, :]
zs = p[2, :]
ax.plot(xs, ys, zs, 'ro')
ax.quiver(0, 0, 0, 1, 0, 0, color = 'r')
ax.quiver(0, 0, 0, 0, 1, 0, color = 'g')
ax.quiver(0, 0, 0, 0, 0, 1, color = 'b')
ax.quiver(0, 0, 0, 1, 1, 1, color = 'k')
for i in range(len(t)):
    ax.text(xs[i], ys[i], zs[i], '{:3.0f}'.format(t[i]))
ax.view_init(10, 10)
plt.show()




