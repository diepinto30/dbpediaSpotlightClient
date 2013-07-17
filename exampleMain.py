#!/usr/bin/env python
#-*- coding: UTF-8 -*-
# File: getStockData.py
# Copyright (c) 2012 by None
#
# GNU General Public Licence (GPL)
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
__author__    = 'Ioannis Avraam <iavraam@gmail.com>'
__docformat__ = 'plaintext'
__date__      = '26/03/2013'

## import the library
from dbpediaSpotlightClient import client
import sys

## this is a simple main function example

if __name__=='__main__':
    reload(sys)
    sys.setdefaultencoding('utf-8')
## first create a client object
    clt = client()
## the input should either be text or url (for tuning annotation parameters see dbpediaSpotlightClient.py)

    print 'Text input...\n'
    Input = 'Η Δράμα βρίσκεται στο γεωγραφικό διαμέρισμα της Μακεδονίας.'
    a=clt.annotate(Input, 'text')
    for i in a:
        print i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + i[3]

    print '\n\n\n'

## specify the types you are interested in as a 3rd argumnent in list
    print 'with type restriction(Person)...\n'
    a=clt.annotate(Input, 'text', ['Place'])
    for i in a:
        print i[0] + '\t' + i[1] + '\t' + i[2]

    print '\n\n\n'

## set URL as input
    print 'URL input\n'
    Input = 'http://news.in.gr/economy/article/?aid=1231240443'
    b=clt.annotate(Input,'url')
    for i in b:
        print i[0],'\t',i[1],'\t',i[2],'\t',i[3]
    print '\n\n\n'

##  spotting service
    print 'Spotting...\n'
    Input = 'http://news.in.gr/economy/article/?aid=1231240443'
    b=clt.spot(Input,'url')
    for i in b:
        print i[0],'\t',i[1]

