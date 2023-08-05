#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 12:47:09 2022

@author: lucas

Atomic units converter
"""
# %% hbar == 1; m == 1; e**2 == 1;
'''length'''
a0 = 5.29177249e-1           # Bohr radius to meter a0:[Å]
'''velocity'''
v0 = 2.18769142e6            # electron velocity 1st Bohr orbit v0:[m/s]
'''time'''
tau0 = 2.41888433e-17        # a0/v0=tau0:[s]
'''frequency'''
nu0 = 1/tau0                 # inverse of time 1/tau0=nu0:[Hz]
'''energy'''
Eau = 27.2113962             # 2x hydrogen binding energy Eau:[eV]
 
'''mass'''
Mu = 9.10953e-31             # atomic mass Mu:[Kg]
me = 5.4858e-04              # electron rest mass in atomic mass units me:[uA]
'''Planck'''
hbar = 6.58212e-16           # hbar:[ev.s] 
ev2J = 1.602176565e-19       # eV:[J] 

'''Electromagnetic'''
c = 299792458
mu0 = 1.25663706212e-6       # permeability [N/A^2]
ep0 = 1/c**2/mu0             # permitivitty [F/m] 

E0 = 5.14220826e11           # unit of electric field strength [V/m]

