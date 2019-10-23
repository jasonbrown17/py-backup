#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__  = "Jason Brown"
__email__   = "jason@jasonbrown.us"
__version__ = "0.1"
__license__ = "Apache ver. 2.0"
__status__  = "Test"
__date__    = "20191023"


import os, tarfile

def main():

    backupdir = ""
    tarname = ""
    transferdir = ""

    with tarfile.open(tarname, "w:gz") as tar:
        tar.add(backupdir, arcname=os.path.basename("backup"))


if __name__ == '__main__':

    try:
        main()
    except:
        print ("No such file or directory")
