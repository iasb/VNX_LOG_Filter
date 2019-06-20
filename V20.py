# -*- coding: latin-1 -*-
#
#
#
#
#   19_jun_2018   Ver1
#
#   v1_1  - work as a subroutines  24-06-2018
#   v1_2 - added num_lines + Histogram
#   v15 - compiled VCForPython27.msi  required Microsoft Visual C++ Compiler for Python 2.7
#       https://www.microsoft.com/en-us/download/details.aspx?id=44266
#
#   C:\Python27\Scripts>pyinstaller.exe --onefile  V14.py
#   C:\Python27\Scripts>pyinstaller.exe -F V20.py
#
#   V17 -- Upper-Lovercase in line
#   v18 - call epoch converter
#   V19 - work with common file
#   V20 -create directory
#

import time
import calendar
import getopt
import re
import datetime
# from datetime import datetime as dt
# from dateutil.parser import parse
# import pandas as pd
import math
import matplotlib
from pylab import *
from matplotlib import pyplot
# import numpy as np
# import datefinder
# import dateparser
# import re
import os

'''
# ===============================================
#   05/13/2016 15:05:26
test_datetime = '05/13/2016 10:05:26'
datepattern = '%m/%d/%Y %H:%M:%S'
datepattern_1 = '%Y-%m-%d %H:%M:%S'

utc_epoch = calendar.timegm(time.strptime(test_datetime, datepattern))
'''


# print test_datetime
# print utc_epoch
# ===============================================

# ===============================================
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# ===============================================

# def uptime_analyses(array_uptime):
#    for line in array_uptime:
# match = re.search('\d{4}-\d{2}-\d{2}', line)

#        print (line)
#       if "Disk soft media error" not in line:
#           array_b.append(line)
# file_out2.write(line)


# ===============================================
#
#     write_analyses_file(name):  ##
#
# ===============================================
def write_analyses_file(name):
    file_name = open('{}.txt'.format(name), 'w')

    n = 0

    for line in array_a:
        # array.append(line)
        ll = line.lower()
        name_l = name.lower()

        #        if name in line:
        if name_l in ll:
            file_name.write(line)
            n = n + 1

    file_name = close('{}.txt'.format(name))

    file_inexes.write(name + "    " + str(n) + '\n')
    print " write ---> " + name


# ===============================================

# ===============================================
#
#     Plot_analyses_file(name):
#
# ===============================================
def plot_analyses_file(name):
    file_name = open('{}.txt'.format(name), 'w')

    for line in array_a:
        # array.append(line)
        if name in line:
            file_name.write(line)


# ===============================================

# ===============================================
#
#     Clean_log
#
# =============================================
def clean_log(name):
    global array_shorten
    global array_b

    array_shorten = array_b
    array_b = []

    name_l = name.lower()

    for line in array_shorten:
        ll = line.lower()
        # array.append(line)
        if name_l not in ll:
            array_b.append(line)
            # file_out2.write(line)
    print "   cleaned --> " + name


# =============================================



# ===============================================
# file_in = open('SPA_navi_getlog.txt', 'r')



file_inexes = open('navi_indexes.txt', 'w')

file_inexes.write('\n')
file_inexes.write('\n')

# ===============================================
file_array_alive = open('heartbeat event.txt', 'w')
# ===============================================
file_disk_softmedia = open('disk_softmedia.txt', 'w')
# ===============================================
file_out2 = open('_Parced_LOG.txt', 'w')
# ===============================================
# file_cache = open('cache.txt', 'w')
# ===============================================


# =============================================

print "  EPOCH_time "

os.system(r'"EPOCH_V3.exe"')

print "  open files "

file_Log_parsing = open('  Log_parsing_process.txt', 'w')

file_Log_parsing.write(" " + '\n')

file_in = open('SPAB_navi_EPOCH_sorted.txt', 'r')

file_Log_parsing.write(" " + '\n')
file_Log_parsing.write("   EPOCH  convering" + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
n_start = datetime.datetime.now()
file_Log_parsing.write("   Log parsing Start time:   %s" % n_start)
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')

# =============================================
#
#   write files
#   feel arrays
#
# =============================================
array_a = []
line_time = []
array_b = []
# array_uptime = []
num_lines = 0

#   @@@@@@@@@@@@@@@@@@@@@@

date_new = ""
date_old = ""

for line in file_in:
    array_b.append(line)
    date_old = date_new
    #    matches = list(datefinder.find_dates(line))
    #    date = matches[0]
    #    print date

    #    utc_epoch = calendar.timegm(time.strptime(test_datetime, datepattern))

    #    print " line", num_lines, " date ", date, " old ", date_old, " new ", date_new, " d ",d
    num_lines = num_lines + 1

    # file_out.write(line)
# =============================================
#   numbering from 0 to end ...
# =============================================
num_lines = num_lines - 2

# =============================================

# =============================================
array_a = array_b
# =============================================

for line in array_a:
    # array.append(line)
    if "The array is alive" in line:
        file_array_alive.write(line)
# =============================================
#
#       Disk soft media error  & Soft SCSI Bus Error
#
#        zerodisk
#
# =============================================

for line in array_a:
    # array.append(line)
    if "Disk soft media error" in line:
        file_disk_softmedia.write(line)
    if "Soft SCSI Bus Error" in line:
        file_disk_softmedia.write(line)
    if "zerodisk" in line:
        file_disk_softmedia.write(line)
    if re.search('Bus' + '.*?' + '\\d+' + '.*?' + 'Enclosure' + '.*?' + '\\d+' + '.*?' + 'Disk', line):
        file_disk_softmedia.write(line)
    if re.search('Bus' + '.*?' + '\\d+' + '.*?' + 'Encl' + '.*?' + '\\d+' + '.*?' + 'Slot', line):
        file_disk_softmedia.write(line)

# =============================================
# =============================================

for line in array_a:
    # array.append(line)
    if "Unit Shutdown for Trespass" in line:
        file_disk_softmedia.write(line)
# =============================================
#
#       cache
#
# =============================================

file_cache = open('cache.txt', 'w')

for line in array_a:
    # array.append(line)
    if "Cache" in line:
        file_cache.write(line)
    if "cache" in line:
        file_cache.write(line)
# =============================================






# uptime_analyses(array_uptime)]


write_analyses_file("Power")
write_analyses_file("LUN")
write_analyses_file("oldest archive file")
write_analyses_file("Trespass")
write_analyses_file("snapshot")
write_analyses_file("The system uptime")
write_analyses_file("Relocation")
write_analyses_file("Time Synchronization")
write_analyses_file("Synchronization of Clone")
write_analyses_file("Microsoft-Windows")

# =============================================
# =============================================
#
#   Cleaning LOG
#
# =============================================
# =============================================


array_b = array_a

clean_log("Internal information only")
clean_log("ioportconfig")
clean_log("Unit Shutdown for Trespass")
clean_log("MiddleRedirector")
clean_log("called by")
clean_log("Microsoft-Windows-Security-Audit")
clean_log("Microsoft-Windows-Kernel-General")
clean_log("Microsoft-Windows-User Profiles")
clean_log("NTP Time Synchronization")
clean_log("Audit Logging Service")
clean_log("Service Control Manager")
clean_log("SSH connection")
clean_log("Power")
clean_log("Battery")
clean_log("SPS")
clean_log("Relocation")
clean_log("relocation")
clean_log("uptime")
clean_log("Informational message")
clean_log("The array is alive")
clean_log("Rule exec")
clean_log("LUN")
clean_log("oldest archive file was deleted")
clean_log("Trespass")
clean_log("snapshot")
clean_log("Disk soft media error")
clean_log("CRU Ready")
clean_log("Soft SCSI Bus Error")
clean_log("Cache")
clean_log("cache")
clean_log("Unit Shutdown for Trespass")
clean_log("Soft Media Error")
clean_log("Sector Reconstructed")
clean_log("Synchronization of Clone")

# =============================================
#
#   write result file
#
# =============================================

for line in array_b:

    if not re.search('Bus' + '.*?' + '\\d+' + '.*?' + 'Enclosure' + '.*?' + '\\d+' + '.*?' + 'Disk',
                     line) and not re.search('Bus' + '.*?' + '\\d+' + '.*?' + 'Encl' + '.*?' + '\\d+' + '.*?' + 'Slot',
                                             line):
        #    print line
        file_out2.write(line)

# =============================================


# =============================================
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
n_end = datetime.datetime.now()
file_Log_parsing.write("   Log parsing End time:   %s" % n_end)
file_Log_parsing.write(" " + '\n')

n_delta = n_end - n_start

file_Log_parsing.write("   Log parsing delta:   %s" % n_delta)
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write("   Lines in LOG %s " % num_lines + "  ( x2 SP-A + SP-B )")
file_Log_parsing.write(" " + '\n')
file_Log_parsing.write(" " + '\n')

file_inexes.write(" "   '\n')

k = file_len("disk_softmedia.txt")

file_inexes.write("disk_softmedia  " + "\t" + str(k) + '\n')

file_inexes.write(" "   '\n')
file_inexes.write(" "   '\n')
file_inexes.write("num_lines  " + str(num_lines) + '\n')

file_Log_parsing.write(" " + '\n')
file_Log_parsing.write("     V19 + EPOCH_V3" + '\n')
file_Log_parsing.write("     IASYNB 2018" + '\n')
file_Log_parsing.write(" " + '\n')

"""
file_Log_parsing.write("  line 1  %s" % array_a[0])
file_Log_parsing.write("  line  %s" % num_lines)
file_Log_parsing.write("  last line   %s" % array_a[num_lines])

# file_Log_parsing.write("  line  %s" %num_lines %array_a[num_lines-1])
# =============================================
"""
# =============================================
#  simple histogram
# =============================================
# hist(randn(10000), bins=30)
# show()
# pyplot.xticks((1.5, 2.5, 3.5, 4.5, 5.5), ('January', 'February', 'March', 'April', 'May'))
# pyplot.hist((1.5, 2.5, 3.5, 4.5, 5.5))
# pyplot.plot
# show()
# =============================================



# from pylab import *

file_in.close()
