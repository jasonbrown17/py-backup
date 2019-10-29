#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__  = "Jason Brown"
__email__   = "jason@jasonbrown.us"
__version__ = "0.1"
__license__ = "Apache ver. 2.0"
__status__  = "Test"
__date__    = "20191023"

import os, tarfile, datetime, sys
from shutil import move

def main():

    try:
        currentdate = datetime.datetime.now()
        todaysdate = currentdate.strftime("%Y%m%d")

        backupdir = ""
        tarname = "backup_"+todaysdate+".tar.gz"
        transferdir = ""

        with tarfile.open(tarname, "w:gz") as tar:
            tar.add(backupdir, arcname=os.path.basename("backup"))

        move(tarname, transferdir)

    except Exception as e:
        print (e)
        sys.exit(1)


if __name__ == '__main__':
    main()
