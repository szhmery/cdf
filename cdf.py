#! /usr/bin/python
"""
###############################################################################
##
## Confidential Information Access Agreement (NDA).                          ##
## For internal use only; do not distribute.                                 ##
##                                                                           ##
###############################################################################
"""
import gc
import sys
import time
import matplotlib
# C++ antigrain rendering engine backend for nice PNGs
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import os.path
import numpy as np
# Argument checking
# Expected arguments are 1) typeOfPlot, 2) rates, 3) heading, 4) preemption flag 5) scenario group

xval, yval = [], []
n_bins = 100
xpercent, ypercent = [], []

if 1:
    latencyFileName = 'raw_data.txt'


    if (os.path.isfile(str(latencyFileName))):
        with open(str(latencyFileName)) as f:
            for line in f:
                sim_time, delay_sample = line.split()[0:2]
                #print sim_time, delay_sample
                latency = float(delay_sample)/1000
                xval.append(sim_time)
                yval.append(latency)
        latency_max = "Max latency:" + str(np.amax(yval)) + " ms\n"
        latency_min = "Min latency:" + str(np.amin(yval)) + " ms"
        labelString = "Latency \n"+latency_max + latency_min
        # Avoid visual effect of the CDF returning to y=0
        # histtype=step returns a single patch, open polygon
        n, bins, patches = plt.hist(yval, n_bins, normed=True, cumulative=True, label=labelString, histtype='step')
        # delete the last point
        patches[0].set_xy(patches[0].get_xy()[:-1])
        f.close()
    else:
        print("%s not found" % latencyFileName)
    #xval, yval = [], []


plt.legend(loc="center right")
plt.xlabel('Latency (ms) ')
plt.ylabel('CDF')
plt.title("CDF example", size=9)
plt.legend(frameon=False, loc='upper right', fontsize=9)
latencyPlotName = 'latency-cdf.pdf'
print "save file : " + latencyPlotName
plt.savefig(latencyPlotName, format='pdf')
plt.close()


