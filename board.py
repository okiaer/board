# pylint: disable-all
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:12:24 2017

@author: OKiaer
"""

from prettytable import PrettyTable
import matplotlib.pyplot as plt
import pdb

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

def getCycleTime(queues, speeds, n_procs):
    cycletime = n_procs
    for i in range(n_procs-1):
        if speeds[i+1] == 0:
            return 'infinite'
        cycletime += int(queues[i]/speeds[i+1])
    return cycletime

def plotCFD(cfd):
    colors = ['r', 'b', 'g', 'y', 'k']
    fig, ax = plt.subplots()
    plt.title('Control Flow Diagram')
    plt.xlabel('Number of days')
    plt.ylabel('Work in progress')
    for i in range(len(cfd)):
        x = [(n+1) for n in range(len(cfd[i]))] # days
        y = cfd[i]
        #plt.plot(x, y)
        ax.stackplot(x, y)
    plt.show()

processes = input('Enter the names of your processes separated by comma: ')
processes = [str(proc) for proc in processes.split(',')]

n_procs = len(processes)

speeds = [0] * n_procs

for i in range(n_procs):
    speed = input('Enter the speed of the "' + processes[i] + '" process: ')
    speeds[i] = int(speed)

queues = [0] * n_procs
local_throughput = [0]*n_procs
local_throughput[0] = speeds[0]
acc_throughput = 0
day = 1

cfd = [0] * n_procs

for i in range(n_procs):
    cfd[i] = [0]

while True:

    print('\n')

    throughput = queues[-1]
    acc_throughput += throughput
    queues[-1] = 0
          
    bottleneckIndex = findBottleneck(queues)
    
    wip = sum(local_throughput) + sum(queues)
    
    cycle_time = getCycleTime(queues, speeds, n_procs)
    
    # Add headers
    headers = ['Day ' + str(day)] + [processes[i] for i in range(n_procs)]
    table = PrettyTable(headers)

    # Add rows
    table.add_row(['Speed'] + speeds)
    table.add_row(['Active tasks'] + local_throughput)
    table.add_row(['Queue'] + ['N/A'] + queues[:-1])

    print(table)

    print('WIP: '+ str(wip))
    print('Throughput: '+str(throughput))
    print('Accumulative throughput: '+str(acc_throughput))
    print('Cycle time: '+str(cycle_time))

    for i in range(0, n_procs):
        cfd[i].append(cfd[i][day-1] + local_throughput[i])

    if bottleneckIndex is not None:
        print('The bottleneck is  the "' + processes[bottleneckIndex] + '" process')
    else:
        print('There is no bottleneck.')    
    
    processToModify = '-1'
    day += 1
    inp = input('\nPress enter for next day, "q" to quit, or "m" to modify process speeds: ')
    if inp == 'q': break
    if inp == 'm':
        keepUpdating = True
        while keepUpdating:
            for proc in range(n_procs):
                print('[' + str(proc + 1) + ']: ' + processes[proc])
            processToModify = input('Which process number would you like to change? ')
            newSpeed = input('Enter the new speed for ' + processes[int(processToModify) - 1] + ': ')
            speeds[int(processToModify) - 1] = int(newSpeed)
            ans = input('Press enter for next day, or "m" to modify another process: ')
            if ans != 'm':
                keepUpdating = False
    if inp == 'p':
        print('plotting ...')
        plotCFD(cfd)
    # Fill queues
    fillQueues(queues, local_throughput)
    
    # Clear queues
    clearQueues(queues, local_throughput)

    if int(processToModify) == 1:
        local_throughput[0] = speeds[0]