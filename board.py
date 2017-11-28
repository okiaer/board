# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:12:24 2017

@author: OKiaer
"""

speeds = input("Input the speed of the boxes separated by comma:")

speeds = [int(sp) for sp in speeds.split(',')]
n_procs = len(speeds)
queues = [0]*n_procs
local_throughput = [0]*n_procs
local_throughput[0] = speeds[0]
day = 1
while True:
    print('\nDay '+str(day)+':')
    
    # Fill queues
    for i in range(n_procs):
        queues[i] = queues[i] + local_throughput[i]
        if i > 0:
            local_throughput[i] = 0
    
    # Clear queues
    for i in range(n_procs):
        if i > 0:
            local_throughput[i] = min(queues[i-1], speeds[i])
            queues[i-1] = queues[i-1] - local_throughput[i]                    
    
    throughput = queues[-1]
    queues[-1] = 0
          
    print('Throughput: '+str(throughput))
    print('Queues: ' + str(queues[:-1]))
    day += 1
    inp = input('Press enter for next day or "q" to quit')
    if inp == 'q': break