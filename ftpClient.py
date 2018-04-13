#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import ftplib, socket, os

HOST = 'ftp.sjtu.edu.cn'
DIRN = 'pub/software'
FILE = 'initrd.lz'

def main():
    try:
        f = ftplib.FTP(HOST)   #Connect TO FTP SERVER: 'ftp.sjtu.edu.cn'
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('*** connect to host "%s"' % HOST)

    try:
        f.login()             #login with annonymously
    except ftplib.error_perm:
        print('ERROR: cannot login anonymously')
        f.quit()
        return
    print('*** Logged in as "anonymous"')

    try:
        f.cwd(DIRN)          #Change dir
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** CD "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE,
                     open(FILE, 'wb').write)    #Donlowd file with CMD 'RETR'
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('*** Downloaded "%s"' % FILE)
    f.quit()

if __name__ == '__main__':
    main()
