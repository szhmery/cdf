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
# Expected arguments are

class Statistic():
    def draw_pdf(self, latencyFileName,title):
        xval, yval = [], []
        n_bins = 100
        xpercent, ypercent = [], []
        i = 0
        if (os.path.isfile(str(latencyFileName))):
            with open(str(latencyFileName)) as f:
                for line in f:
                    delay_sample = line.split()[0:1]
                    print delay_sample
                    latency = float(delay_sample[0])/1000
                    xval.append(i)
                    yval.append(latency)
                    i += 1
            if yval != []:
                latency_max = "Max:" + str(np.amax(yval)) + " ms\n"
                latency_ave = "Average:" + str(round(np.average(yval),3)) + " ms\n"
                latency_min = "Min:" + str(round(np.amin(yval),3)) + " ms"
                labelString = "\n\n\nLatency \n"+latency_max + latency_ave + latency_min
                # Avoid visual effect of the CDF returning to y=0
                # histtype=step returns a single patch, open polygon
                n, bins, patches = plt.hist(yval, n_bins, normed=True, cumulative=False, label=labelString, histtype='bar')

            f.close()
        else:
            print("%s not found" % latencyFileName)
        # xval, yval = [], []


        plt.legend(loc="center right")
        plt.xlabel('Latency (ms) ')
        plt.ylabel('PDF')
        plt.title(title+" PDF example", size=9)
        plt.legend(frameon=False, loc='upper right', fontsize=9)
        latencyPlotName = latencyFileName[:-4]+"-pdf.pdf"
        print "save file : " + latencyPlotName
        plt.savefig(latencyPlotName, format='pdf')
        plt.close()

    def draw_cdf(self,latencyFileName, title):
        xval, yval = [], []
        n_bins = 100
        xpercent, ypercent = [], []
        i = 0
        if (os.path.isfile(str(latencyFileName))):
            with open(str(latencyFileName)) as f:
                for line in f:
                    delay_sample = line.split()[0:1]
                    print delay_sample
                    latency = float(delay_sample[0])/1000
                    xval.append(i)
                    yval.append(latency)
                    i += 1
            if yval != []:
                latency_max = "Max:" + str(np.amax(yval)) + " ms\n"
                latency_ave = "Average:" + str(round(np.average(yval),3)) + " ms\n"
                latency_min = "Min:" + str(round(np.amin(yval),3)) + " ms"
                labelString = "\n\n\nLatency \n"+latency_max + latency_ave + latency_min
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
        plt.title(title+" CDF example", size=9)
        plt.legend(frameon=False, loc='upper right', fontsize=9)

        latencyPlotName = latencyFileName[:-4] + "-cdf.pdf"
        print "save file : " + latencyPlotName
        plt.savefig(latencyPlotName, format='pdf')
        plt.close()

if __name__=="__main__":
    enable_mbwr_file = '/root/zhaohsun/cdf/enable_mbwr.txt'
    Statistic().draw_pdf(enable_mbwr_file,"Enable BWR")
    Statistic().draw_cdf(enable_mbwr_file,"Enable BWR")

    disable_mbwr_file = '/root/zhaohsun/cdf/disable_mbwr.txt'
    Statistic().draw_pdf(disable_mbwr_file,"Disable BWR")
    Statistic().draw_cdf(disable_mbwr_file,"Disable BWR")

