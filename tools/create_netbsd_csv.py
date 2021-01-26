#!/usr/bin/env python3
#

'''
http://www.netbsd.org/about/history.html
https://www.netbsd.org/releases/release-map.html
https://www.netbsd.org/releases/formal-6/NetBSD-6.1.5.html
https://www.pkgsrc.org/pkgsrcCon/2007/slides/salo/releng-pkgsrc.html
'''

import csv
with open('netbsd.csv', mode='w') as netbsd_f:
    netbsd_writer = csv.writer(netbsd_f, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_MINIMAL)
    #version,branch,codename, series, created,release,eor
    netbsd_writer.writerow(['version', 'branch', 'series', 'release', 'eor'])
    netbsd_writer.writerow(['0.8', 'netbsd-0', 'major', '20-05-1993', 'major', 'death'])
    netbsd_writer.writerow(['0.9', 'netbsd-0', 'major', '', '23-08-1993', 'major', 'death'])
    netbsd_writer.writerow(['1.0', 'netbsd-1', 'major', '', '26-10-1993', 'major', 'death'])
    netbsd_writer.writerow(['1.2.1', 'netbsd-1.2', 'minor', '', '20-05-1997', 'minor', ''])
    netbsd_writer.writerow(['2.0.1', 'netbsd-2', 'security', '', '20-05-1997', 'minor', ''])
    netbsd_writer.writerow(['2.1', 'netbsd-2.1', 'stable', '', '02-11-2005', 'minor', '21-08-2008'])
    netbsd_writer.writerow(['6.0', 'netbsd-6', 'stable', '', '22-09-2014', 'major', '21-08-2008'])
    netbsd_writer.writerow(['6.0.5', 'netbsd-6', 'maintenance', 'sec/critical', '', 'minor', 'death'])
    netbsd_writer.writerow(['6.0.6', 'netbsd-6', '', '', '02-11-2005', 'minor', 'death'])
    netbsd_writer.writerow(['6.1', 'netbsd-6.1', 'stable', '', '18-05-2013', 'minor', 'death'])
    netbsd_writer.writerow(['6.1.5', 'netbsd-6.1', 'stable', '', '18-05-2013', 'minor', '21-08-2008'])
    netbsd_writer.writerow(['7.1.1', 'netbsd-7.1', 'stable', '', '02-11-2005', 'minor', '21-08-2008'])
    netbsd_writer.writerow(['9.0', 'netbsd-9', 'stable', '', '14-02-2020', 'major', ''])
    netbsd_writer.writerow(['9.1', 'netbsd-9', 'update', '', '18-10-2020', 'major', ''])
    netbsd_writer.writerow(['N.99.M', 'NetBSD-daily', 'devel/current', '', 'daily', '', ''])
    netbsd_writer.writerow(['N.99.M', 'NetBSD-current', 'devel', '', '', 'major', ''])
    
    
    
