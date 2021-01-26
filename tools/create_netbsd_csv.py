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
    netbsd_writer.writerow(['0.8', 'netbsd-0', 'stable', '', '20-05-1993', 'major', ''])
    netbsd_writer.writerow(['0.8', 'netbsd-0', 'stable', '', '20-05-1994', 'major', ''])
    netbsd_writer.writerow(['1.2.1', 'netbsd-1', 'maintenence/security', '', '20-05-1997', 'minor', ''])
    netbsd_writer.writerow(['2.0.1', 'netbsd-1', 'maintenence/security', '', '20-05-1997', 'minor', ''])
    netbsd_writer.writerow(['2.1', 'netbsd-2', 'stable', '', '02-11-2005', 'minor', '21-08-2008'])
    netbsd_writer.writerow(['6.0', 'netbsd-6', 'stable', '', '22-09-2014', 'major', '21-08-2008'])
    netbsd_writer.writerow(['6.0.6', 'netbsd-6', 'stable', '', '02-11-2005', 'minor', '21-08-2008'])
    netbsd_writer.writerow(['7.1.1', 'netbsd-7', 'stable', '', '02-11-2005', 'minor', '21-08-2008'])
    netbsd_writer.writerow(['9.0', 'netbsd-9', 'stable', '', '14-02-2020', 'major', ''])
    
    
    
