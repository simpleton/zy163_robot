#!/usr/bin/env python

import re
import urllib, urllib2
import httplib

URL = "http://www.zy163.net/qq/index.asp"

def judgeMan(uin, name, conn=None):
    params = urllib.urlencode({'key': uin})
    req = urllib2.Request(URL, params)
    data = urllib2.urlopen(req).read()
    if data.find(uin) == -1:
        return "GOOD"
    else:
        return "BAD"

if __name__ == "__main__":
    fin = open("data.in", 'r')
    fout = open('data.out', 'w')

    prog = re.compile('\((\d+)\)')

    try:
        lines = fin.readlines()
        for i in xrange(1,len(lines)):
            line = lines[i]
            m = prog.search(line)
            if m is not None:
                uin = m.group(1)
                man_status = judgeMan(uin, lines[i-1])
                print uin, man_status
                fout.write( ",".join([uin, man_status]))
    finally:
        fin.close()
        fout.close()
