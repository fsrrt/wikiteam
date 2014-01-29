#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2011-2012 WikiTeam
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Script to check if a list of wikis are alive or dead

import thread
import time
import sys
import urllib2
import exceptions
import re

# Configuration
delay = 30 # Seconds before timing out on request
limit = 100

def printapi(api):
    print api, 'is alive'
    open('wikisalive.txt', 'a').write(('%s\n' % api.strip()).encode('utf-8'))

def checkcore(api):
    req = urllib2.Request(api, None)
    try:
        raw = urllib2.urlopen(req, None, delay).read()
    except IOError: # http://docs.python.org/2/howto/urllib2.html#handling-exceptions
        print api, 'is dead or has errors'
        return
    # RSD is available since 1.17, bug 25648
    rsd = re.search(r'(?:link rel="EditURI".+href=")(?:https?:)?(.+api.php)\?action=rsd', raw)
    # Feeds are available, with varying format, in 1.8 or earlier
    feed = re.search(r'(?:link rel="alternate" type="application/)(?:atom|rss)(?:\+xml[^>]+href="/)([^>]*index.php)(?:\?title=[^>]+&amp;)(?:feed|format)', raw)
    # Sometimes they're missing though, this should catch the rest but goes out of <head>
    login = re.search(r'(?:<li id="pt-login"><a href="/)([^>]*index.php)', raw)
    domain = re.search(r'(https?://.[^/]+/)', api)
    # TODO: Simplistic check for API. The docs page can be returned even if everything else
    # is choking on database or PHP errors (hundreds online wikis fatal on every request).
    if 'This is an auto-generated MediaWiki API documentation page' in raw:
        printapi(api)
    elif rsd:
        api = 'http:' + rsd.group(1)
        printapi(api)
    elif feed:
        index = domain.group(1) + feed.group(1)
        printapi(index)
    elif login:
        index = domain.group(1) + login.group(1)
        printapi(index)
    else:
        print api, 'is not a MediaWiki wiki'

def check(apis):
    for api in apis:
        thread.start_new_thread(checkcore, (api,))
        time.sleep(0.1)
    time.sleep(delay+1)

apis = []
for api in open('wikistocheck.txt', 'r').read().strip().splitlines():
    if not api in apis:
        apis.append(api)
    if len(apis) >= limit:
        check(apis)
        apis = []

check(apis)
