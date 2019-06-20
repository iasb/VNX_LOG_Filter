#=================================================
#
#   join SPA_navi_getlog  + SPB_navi_getlog
#   create SPAB_navi_EPOCH.txt
#   sort SPAB_navi_EPOCH_sorted.txt by time
#
#
#   IASYNB     30.06.18
#
#=================================================
import time
#import sys
#import re, datetime
#from dateutil import parser
#import datefinder
#import calendar
#from datetime import datetime
#from date_extractor import extract_dates

#=================================================
#   A
#=================================================
file_in_a = open('SPA_navi_getlog.txt', 'r')
#file_out_a = open('SPA_navi_EPOCH.txt', 'w')
file_common = open('SPAB_navi_EPOCH.txt', 'w')
file_common_sorted = open('SPAB_navi_EPOCH_sorted.txt', 'w')

for line in file_in_a:


    p = "%m/%d/%Y %H:%M:%S"
    if  line[:19]  != '\n':
#        sys.exit(0)
        dates = int(time.mktime(time.strptime(line[:19], p)))

#    dates = extract_dates(line[:19])
#    print line[:19]
    #print  (str(dates) + "  " + line[:19])
#        file_out_a.write(str(dates) + " A "+ line)
        file_common.write(str(dates) + " A " + line)

#=================================================
#   B
#=================================================


file_in_b = open('SPB_navi_getlog.txt', 'r')
#file_out_b = open('SPB_navi_EPOCH.txt', 'w')

for line in file_in_b:


    p = "%m/%d/%Y %H:%M:%S"
    if  line[:19]  != '\n':
 #       sys.exit(0)
        dates = int(time.mktime(time.strptime(line[:19], p)))


#    dates = extract_dates(line[:19])
#    print line[:19]
    #print  (str(dates) + "  " + line[:19])
#        file_out_b.write(str(dates) + " B "+ line)
        file_common.write(str(dates) + " B " + line)

file_common.close()


file_common = open('SPAB_navi_EPOCH.txt', 'r')

array_unsorted = []
array_sorted = []
#
#  read common logs  a+b
#
for line in file_common:
    array_unsorted.append(line)
    #print(line[:10])

#
#  read common logs  a+b
#

array_sorted =  sorted(array_unsorted)

    #print(sorted(array_unsorted[:10]))

# =============================================

for line in array_sorted :
    # array.append(line)
    #print(line)
    file_common_sorted.write(line)
