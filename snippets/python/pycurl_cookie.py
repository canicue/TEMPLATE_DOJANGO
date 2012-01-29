#!/usr/bin/python
# -*- coding: utf-8; mode: python -*-

import sys
import pycurl

print 'Using PycURL %s version' % pycurl.version

if len(sys.argv) < 3:
    print "Usage: %s url cookie_file\n" % __file__
    sys.exit(1)

url, cookie_file = sys.argv[1:3]

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.COOKIEFILE, cookie_file)

c.perform()
c.close()