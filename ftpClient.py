#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import ftplib, socket, os

HOST = 'ftp.sjtu.edu.cn'
DIRN = 'pub/software'
FILE = 'initrd.lz'

def main():
    try:
        f = ftplib.FTP(HOST)   #CONNENT TO FTP SERVER: 'ftp.sjtu.edu.cn'
    except (socket.error, socket.gaierror) as e:
        print('ERROR: cannot reach "%s"' % HOST)
        return
    print('*** connect to host "%s"' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login anonymmously')
        f.quit()
        return
    print('*** Logged in as "anonymous"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print('*** CD "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE,
                     open(FILE, 'wb').write)
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('*** Downloaded "%s"' % FILE)
    f.quit()

if __name__ == '__main__':
    main()