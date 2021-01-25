#!/usr/bin/env python3
#

'''
http://www.netbsd.org/about/history.html
https://www.netbsd.org/releases/release-map.html
'''

import csv
with open('netbsd.csv', mode='w') as netbsd_f:
    netbsd_writer = csv.writer(netbsd_f, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
    #version,codename,series,created,release,eol
    netbsd_writer.writerow(['version', 'codename','branch', 'series', 'created', 'release', 'eos'])
    netbsd_writer.writerow(['8.0', 'netbsd-8', 'stable', '', '20-05-1993', '', ''])
    netbsd_writer.writerow(['8.0', 'netbsd-8', 'stable', '', '20-05-1993', '', ''])
    netbsd_writer.writerow(['8.0', 'netbsd-8', 'stable', '', '20-05-1994', '', ''])
    netbsd_writer.writerow(['1.2.1', 'netbsd-1', 'maintenence/security', '', '20-05-1997', 'NetBSD', ''])
    netbsd_writer.writerow(['2.0.1', 'netbsd-1', 'maintenence/security', '', '20-05-1997', 'NetBSD', ''])
    netbsd_writer.writerow(['2.1', 'netbsd-2', 'stable', '', '02-11-2005', '', '21-08-2008'])
    
