#!/usr/bin/env python3
#

'''
http://www.netbsd.org/about/history.html
https://www.netbsd.org/releases/release-map.html
'''

import csv
with open('pkgsrc.csv', mode='w') as pkgsrc_f:
    netbsd_writer = csv.writer(pkgsrc_f, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
    #version,codename,series,created,release,eol
    netbsd_writer.writerow(['version', 'codename','branch', 'series', 'created', 'release', 'eos'])
    netbsd_writer.writerow(['0.8', 'netbsd-0', 'stable', '', '20-05-1993', 'major', ''])
    netbsd_writer.writerow(['0.8', 'netbsd-0', 'stable', '', '20-05-1994', 'major', ''])
    netbsd_writer.writerow(['1.2.1', 'netbsd-1', 'maintenence/security', '', '20-05-1997', 'minor', ''])
    netbsd_writer.writerow(['2.0.1', 'netbsd-1', 'maintenence/security', '', '20-05-1997', 'minor', ''])
    netbsd_writer.writerow(['2.1', 'netbsd-2', 'stable', '', '02-11-2005', 'minor', '21-08-2008'])
    
