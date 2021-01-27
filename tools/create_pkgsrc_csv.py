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
    netbsd_writer.writerow(['version', 'branch', 'release', 'eol'])
    netbsd_writer.writerow(['2015Q1', 'stable-2015Q1', '14-04-2015', ''])
    netbsd_writer.writerow(['2015Q2', 'stable-2015Q2', '06-07-2015', ''])
    netbsd_writer.writerow(['2015Q3', 'stable-2015Q3', '30-09-2015', ''])
    netbsd_writer.writerow(['2016Q1', 'stable-2016Q1', '09-05-2016', ''])
    netbsd_writer.writerow(['2016Q1', 'stable-2016Q1', '09-05-2016', ''])
    netbsd_writer.writerow(['2018Q4', 'stable-2018Q4', '31-12-2018', ''])
    netbsd_writer.writerow(['2019Q3', 'stable-2019Q43', '03-10-2019', ''])
    
