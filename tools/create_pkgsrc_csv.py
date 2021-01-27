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
    netbsd_writer.writerow(['2008Q1', 'pkgsrc-2008Q1', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', ''])
    netbsd_writer.writerow(['2015Q1', 'pkgsrc-2015Q1', '14-04-2015', ''])
    netbsd_writer.writerow(['2015Q2', 'pkgsrc-2015Q2', '06-07-2015', ''])
    netbsd_writer.writerow(['2015Q3', 'pkgsrc-2015Q3', '30-09-2015', ''])
    netbsd_writer.writerow(['2016Q1', 'pkgsrc-2016Q1', '09-05-2016', ''])
    netbsd_writer.writerow(['2016Q4', 'pkgsrc-2016Q4', '04-01-2016', ''])
    netbsd_writer.writerow(['2017Q1', 'pkgsrc-2017Q1', '03-04-2017', ''])
    netbsd_writer.writerow(['2018Q4', 'pkgsrc-2018Q4', '31-12-2018', ''])
    netbsd_writer.writerow(['2019Q3', 'pkgsrc-2019Q3', '03-10-2019', ''])
    netbsd_writer.writerow(['2020Q2', 'pkgsrc-2020Q2', '30-06-2020', ''])
    netbsd_writer.writerow(['2020Q3', 'pkgsrc-2020Q3', '09-10-2020', ''])
    netbsd_writer.writerow(['2020Q4', 'pkgsrc-2020Q4', '07-01-2021', ''])
    
