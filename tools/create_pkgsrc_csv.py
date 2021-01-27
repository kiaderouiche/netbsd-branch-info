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
    netbsd_writer.writerow(['version', 'branch', 'release', 'eol'])
    netbsd_writer.writerow(['2007Q4', 'pkgsrc-2007Q4', '05-01-2008', '',])
    netbsd_writer.writerow(['2008Q1', 'pkgsrc-2008Q1', '02-01-2008', '',])
    netbsd_writer.writerow(['2010Q1', 'pkgsrc-2010Q1', '20-04-2010', '',])
    netbsd_writer.writerow(['2010Q2', 'pkgsrc-2010Q2', '02-01-2015', '',])
    netbsd_writer.writerow(['2011Q1', 'pkgsrc-2011Q1', '06-04-2011', '',])
    netbsd_writer.writerow(['2011Q3', 'pkgsrc-2011Q3', '03-10-2011', '',])
    netbsd_writer.writerow(['2012Q1', 'pkgsrc-2012Q1', '07-04-2012', '',])
    netbsd_writer.writerow(['2012Q2', 'pkgsrc-2012Q2', '03-07-2012', '',])
    netbsd_writer.writerow(['2012Q3', 'pkgsrc-2012Q3', '01-10-2012', '',])
    netbsd_writer.writerow(['2012Q4', 'pkgsrc-2012Q4', '11-01-2013', '',])
    netbsd_writer.writerow(['2013Q1', 'pkgsrc-2013Q1', '01-04-2013', '',])
    netbsd_writer.writerow(['2013Q2', 'pkgsrc-2013Q2', '04-07-2013', '',])
    netbsd_writer.writerow(['2012Q4', 'pkgsrc-2012Q4', '11-01-2013', '',])
    netbsd_writer.writerow(['2013Q3', 'pkgsrc-2013Q3', '04-10-2013', '',])
    netbsd_writer.writerow(['2013Q4', 'pkgsrc-2013Q4', '31-12-2013', '',])
    netbsd_writer.writerow(['2014Q2', 'pkgsrc-2015Q2', '03-07-2014', '',])
    netbsd_writer.writerow(['2014Q4', 'pkgsrc-2015Q4', '02-01-2015', '',])
    netbsd_writer.writerow(['2015Q1', 'pkgsrc-2015Q1', '14-04-2015', '',])
    netbsd_writer.writerow(['2015Q2', 'pkgsrc-2015Q2', '06-07-2015', '',])
    netbsd_writer.writerow(['2015Q3', 'pkgsrc-2015Q3', '30-09-2015', '',])
    netbsd_writer.writerow(['2016Q1', 'pkgsrc-2016Q1', '09-05-2016', '',])
    netbsd_writer.writerow(['2016Q4', 'pkgsrc-2016Q4', '04-01-2016', '',])
    netbsd_writer.writerow(['2017Q1', 'pkgsrc-2017Q1', '03-04-2017', '',])
    netbsd_writer.writerow(['2018Q4', 'pkgsrc-2018Q4', '31-12-2018', '',])
    netbsd_writer.writerow(['2019Q3', 'pkgsrc-2019Q3', '03-10-2019', '',])
    netbsd_writer.writerow(['2020Q2', 'pkgsrc-2020Q2', '30-06-2020', '',])
    netbsd_writer.writerow(['2020Q3', 'pkgsrc-2020Q3', '09-10-2020', '',])
    netbsd_writer.writerow(['2020Q4', 'pkgsrc-2020Q4', '07-01-2021', '',])
    
