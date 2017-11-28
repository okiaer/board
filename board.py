# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:12:24 2017

@author: OKiaer
"""

speeds = input("Input the speed of the boxes separated by comma:")
speeds = [int(sp) for sp in speeds.split(',')]
n_procs = len(speeds)

day = 0
while True:
    print('\nDay '+str(day)+':')
    throughput = 0 if day < n_procs else min(speeds)
    print('The throughput is '+str(throughput))
    day += 1
    inp = input('Press enter for next day or "q" to quit')
    if inp == 'q': break