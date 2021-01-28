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
    #version,branch,series, created(for major version, begin Candidat_1,2 and Patch),release,eol
    netbsd_writer.writerow(['version', 'branch', 'series', 'created', 'release', 'eol'])
    netbsd_writer.writerow(['0.8', 'netbsd-0', 'major','', '20-04-1993', ''])
    netbsd_writer.writerow(['0.9', 'netbsd-0', 'major','', '23-08-1993', ''])
    netbsd_writer.writerow(['1.0', 'netbsd-1', 'major','', '26-10-1994', ''])
    netbsd_writer.writerow(['1.1', 'netbsd-1', 'major','', '26-11-1995', ''])
    netbsd_writer.writerow(['1.2', 'netbsd-1', 'major','', '04-10-1996', ''])
    netbsd_writer.writerow(['1.2.1', 'netbsd-1.2', 'minor','', '20-05-1997', ''])
    netbsd_writer.writerow(['1.3', 'netbsd-1.3', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.3.1', 'netbsd-1.3', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.3.2', 'netbsd-1.3', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.3.3', 'netbsd-1.3', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.4', 'netbsd-1.3', 'minor','', '12-05-1999', ''])
    netbsd_writer.writerow(['1.4.1', 'netbsd-1.3', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.4.2', 'netbsd-1.3', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.4.3', 'netbsd-1.3', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.5', 'netbsd-1.5', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.5.1', 'netbsd-1.5', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.5.2', 'netbsd-1.5', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.5.3', 'netbsd-1.5', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.6', 'netbsd-1.6', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.6.1', 'netbsd-1.6', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['1.6.2', 'netbsd-1.6', 'minor','', '09-03-1998', ''])
    netbsd_writer.writerow(['2.0', 'netbsd-2', 'minor', '', '20-05-1997', '30-04-2008'])
    netbsd_writer.writerow(['2.0.1', 'netbsd-2', 'minor', '', '20-05-1997', '30-04-2008'])
    netbsd_writer.writerow(['2.0.3', 'netbsd-2', 'minor', '', '02-11-2005', '30-04-2008'])
    netbsd_writer.writerow(['2.1', 'netbsd-2.1', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['3.0', 'netbsd-3', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['3.0.1', 'netbsd-3', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['3.0.2', 'netbsd-3', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['4.0', 'netbsd-4', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['4.0.1', 'netbsd-4', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['5.0', 'netbsd-5', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['5.0.1', 'netbsd-5', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['5.0.2', 'netbsd-5', 'minor', '', '14-10-2008', '30-04-2008'])
    netbsd_writer.writerow(['5.1', 'netbsd-5.1', 'minor', '', '11-02-2010',''])
    netbsd_writer.writerow(['5.1.2', 'netbsd-5.1', 'minor', '', '10-02-2012',''])
    netbsd_writer.writerow(['5.1.3', 'netbsd-5.1', 'minor', '', '28-09-2013',''])
    netbsd_writer.writerow(['5.1.5', 'netbsd-5.1', 'minor', '', '25-01-2014',''])
    netbsd_writer.writerow(['5.2', 'netbsd-5.2', 'minor', '', '25-01-2014',''])
    netbsd_writer.writerow(['5.2.1', 'netbsd-5.2', 'minor', '', '28-09-2013',''])
    netbsd_writer.writerow(['6.0', 'netbsd-6', 'major', '30-08-2012', '17-10-2012',''])
    netbsd_writer.writerow(['6.0.1', 'netbsd-6', 'minor', '', '26-12-2012',''])
    netbsd_writer.writerow(['6.1', 'netbsd-6.1', 'minor', '', '18-05-2013', ''])
    netbsd_writer.writerow(['6.1.1', 'netbsd-6.1', 'minor','', '21-08-2013', ''])
    netbsd_writer.writerow(['7.0', 'netbsd-7', 'major', '', '08-10-2015', ''])
    netbsd_writer.writerow(['7.0.1', 'netbsd-7', 'minor', '', '28-05-2016', ''])
    netbsd_writer.writerow(['7.0.2', 'netbsd-7', 'minor', '', '21-10-2016', ''])
    netbsd_writer.writerow(['7.1', 'netbsd-7.1', 'minor', '', '11-03-2017', ''])
    netbsd_writer.writerow(['7.1.1', 'netbsd-7.1', 'minor', '', '22-12-2017', ''])
    netbsd_writer.writerow(['7.1.2', 'netbsd-7.1', 'minor', '', '15-03-2018', ''])
    netbsd_writer.writerow(['7.2', 'netbsd-7.2', 'minor', '', '29-08-2018', ''])
    netbsd_writer.writerow(['8.0', 'netbsd-8', 'major', '', '17-07-2018', ''])
    netbsd_writer.writerow(['8.1', 'netbsd-8.1', 'minor', '', '31-05-2019', ''])
    netbsd_writer.writerow(['8.2', 'netbsd-8.2', 'minor', '', '31-03-2020', ''])
    netbsd_writer.writerow(['9.0', 'netbsd-9', 'major', '', '14-02-2020', ''])
    netbsd_writer.writerow(['9.1', 'netbsd-9.1', 'minor', '', '18-10-2020', ''])
    netbsd_writer.writerow(['N.99.M', 'NetBSD-daily', 'current', '', 'daily', ''])
    netbsd_writer.writerow(['N.99.M', 'NetBSD-current', 'devel', '', '', ''])
    
    
    
