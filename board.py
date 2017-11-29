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

def findBottleneck(queues):
    bottleneckIndex = None
    for i, queue in enumerate(queues[::-1]):
        if queue != 0:
            bottleneckIndex = n_procs - i
            break
    return bottleneckIndex
            

speeds = input("Input the speed of the boxes separated by comma:")

speeds = [int(sp) for sp in speeds.split(',')]
n_procs = len(speeds)
queues = [0]*n_procs
local_throughput = [0]*n_procs
local_throughput[0] = speeds[0]
acc_throughput = 0
day = 1
while True:
    print('\nDay '+str(day)+':')
    
    throughput = queues[-1]
    acc_throughput += throughput
    queues[-1] = 0
          
    bottleneckIndex = findBottleneck(queues)
    
    # WIP
    wip = sum(local_throughput) + sum(queues)
    
    print('Queues: ' + str(queues[:-1]))
    print('Active tasks: ' + str(local_throughput))
    print('WIP: '+ str(wip))
    print('Throughput: '+str(throughput))
    print('Accumulative throughput: '+str(acc_throughput))
    
    if bottleneckIndex is not None:
        print('The bottleneck is process number ' + str(bottleneckIndex + 1))
    else:
        print('There is no bottleneck.')    
    
    day += 1
    inp = input('Press enter for next day or "q" to quit')
    if inp == 'q': break

    # Fill queues
    fillQueues(queues, local_throughput)
    
    # Clear queues
    clearQueues(queues, local_throughput)
