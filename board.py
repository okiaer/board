# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:12:24 2017

@author: OKiaer
"""

speeds = input("Input the speed of the boxes separated by comma:")
speeds = [int(sp) for sp in speeds.split(',')]

print(min(speeds))