# -*- coding: utf-8 -*-

"""
Name                    : mocheckso
Description             : imports a csv file from ftp server, makes a minimal check and sends errors via email
Date                    : 2015-12-21
copyright               : (C) 2015 by Tobias Reber / Stefan Ziegler
email                   : tobias.reber / stefan.ziegler (at) bd.so.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/

 sys.exit(3) = UNKNOWN
 sys.exit(2) = ERROR
 sys.exit(1) = WARNING
 sys.exit(0) = OK

"""

try:
    import os
    import sys
    import logging
    import psycopg2
    import ftplib
    from ftplib import FTP

except ImportError, strerror:
    print strerror
    sys.exit(2)

#VARS
TMP_DIR = '/home/stefan/tmpa/'
CSV_FILE_LOCAL = os.path.join(TMP_DIR, 'mocheckso_errors.csv')
CSV_FILE_SERVER = 'DM01AVSO24/ERROR/MOCHECKSO_ERRORS.CSV'

# Logging
# ....

def main():


    try:
        error_file = open(CSV_FILE_LOCAL, 'w')

        ftp = FTP('ftp.infogrips.ch', 'vaso', 'vaso123')
        ftp.retrbinary('RETR ' + CSV_FILE_SERVER, error_file.write)

        error_file.close()
        ftp.quit()

    except IOError, strerror:
        print strerror
        print "fuu"
        sys.exit(2)

    except ftplib.all_errors, strerror:
        print strerror
        sys.exit(2)


    print "Hallo Stefan."

if __name__ == '__main__':
    sys.exit(main())
