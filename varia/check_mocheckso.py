#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ftplib import FTP
import datetime

ftp = FTP('ftp.infogrips.ch', 'xxxx', 'yyyyy')

ts = datetime.datetime.now().isoformat()
print ts

gFile = open("/home/stefan/Projekte/mocheckso/errors_" + ts + ".csv", "w")
ftp.retrbinary('RETR DM01AVSO24/ERROR/MOCHECKSO_ERRORS.CSV', gFile.write)
gFile.close()
ftp.quit()
