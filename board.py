# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:12:24 2017

@author: OKiaer
"""

def fillQueues(queues, local_throughput):
    n_procs = len(queues)
    for i in range(n_procs):
        queues[i] = queues[i] + local_throughput[i]
        if i > 0:
            local_throughput[i] = 0

def clearQueues(queues, local_throughput):
    n_procs = len(queues)
    for i in range(n_procs):
        if i > 0:
            local_throughput[i] = min(queues[i-1], speeds[i])
            queues[i-1] = queues[i-1] - local_throughput[i]                    

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
    fillQueues(queues, local_throughput)
    
    # Clear queues
    clearQueues(queues, local_throughput)
    
    throughput = queues[-1]
    queues[-1] = 0
    # Find bottleneck
    bottleneckIndex = None
    revqueues = queues[:]
    revqueues.reverse()
    for i, queue in enumerate(revqueues):
        if queue != 0:
            bottleneckIndex = n_procs - i
            break
    
    if bottleneckIndex is not None:
        print('The bottleneck is process number ' + str(bottleneckIndex + 1))
    else:
        print('There is no bottleneck.')
    
    #nonemptyQueues = filter(lambda x: x != 0, queues[:-1])
    #bottleneckIndex = None if len(nonemptyQueues) == 0 else nonemptyQueues[-1] + 1
    
    print('Throughput: '+str(throughput))
    print('Queues: ' + str(queues[:-1]))
    day += 1
    inp = input('Press enter for next day or "q" to quit')
    if inp == 'q': break


