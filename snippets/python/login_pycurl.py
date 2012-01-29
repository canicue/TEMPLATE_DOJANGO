#!/usr/bin/python2.6
# -*- coding: utf-8; mode: python -*-

import sys, urllib

import pycurl

print 'Using PycURL %s version' % pycurl.version

if len(sys.argv) < 4:
    print '''Usage:\t%s url user pass [cookie_file_name]\n
If no cookie file name is given, it will write the cookie on /tmp/cookie.txt
''' % __file__
    sys.exit(1)

url, user, pwd  = sys.argv[1:4]

try:
    cookie_file = sys.argv[4]
except IndexError:
    cookie_file = '/tmp/cookie.txt'

post_values = {'name': user,
               'pass': pwd,
               'form_id': 'user_login'}

c = pycurl.Curl()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.POSTFIELDS, urllib.urlencode(post_values))
c.setopt(pycurl.COOKIEJAR, cookie_file)

c.perform()
c.close()