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
__date__      = '20/03/2013'

from BeautifulSoup import BeautifulSoup
import urllib2,sys,os

class client():
    def __init__(self, confidence='0', support='0'):
        self.confidence = confidence
        self.support = support
        self.serverURL = 'http://dbpedia-spotlight.math.auth.gr:2222/rest/'
	self.wikipediaBaseURL = 'http://el.wikipedia.org/wiki/'
        self.stopwords = open('stopwords.txt', 'r').read()

    def annotate(self, Input, inputType = 'text', types = []):
        if inputType == 'text':
            Input = urllib2.quote(Input)
            annotationURL = self.serverURL + 'annotate?text=' + Input + '&confidence=' + self.confidence + '&support=' + self.support
        elif inputType == 'url':
            annotationURL = self.serverURL + 'annotate?url=' + Input + '&confidence=' + self.confidence + '&support=' + self.support
        else:
            print 'Input type not recognized... exiting'
            return False
        if types:
            annotationURL += '&types=' + ','.join(types)
        #print annotationURL
        page = urllib2.urlopen(annotationURL).read()
        soup = BeautifulSoup(page,fromEncoding='UTF-8')
        #div = soup.find('div')
        entities = soup.findAll('resource')
        annotations = []
        for entity in entities:
            uri = entity.attrs[0][1]
            identifier = uri.split('/')[-1]
            wikipediaURL = self.wikipediaBaseURL + identifier
            resource = entity.attrs[3][1]
            types = entity.attrs[2][1]
            if not resource in self.stopwords:
                annotations.append((resource,uri,wikipediaURL,types))
        return annotations

    def spot(self, Input, inputType = 'text'):
        if inputType == 'text':
            Input = urllib2.quote(Input)
            annotationURL = self.serverURL + 'spot?text=' + Input + '&confidence=' + self.confidence + '&support=' + self.support
        elif inputType == 'url':
            annotationURL = self.serverURL + 'spot?url=' + Input + '&confidence=' + self.confidence + '&support=' + self.support
        else:
            print 'Input type not recognized... exiting'
            return False
        #print annotationURL
        page = urllib2.urlopen(annotationURL).read()
        soup = BeautifulSoup(page,fromEncoding='UTF-8')
        annotation = soup.find('annotation')
        surfaceForms = annotation.findAll('surfaceform')
        spots = []
        for surfaceForm in surfaceForms:
            #print surfaceForm
            name = surfaceForm.attrs[0][1]
            offset = surfaceForm.attrs[1][1]
            if not name in self.stopwords:
                spots.append((name,offset))
        return spots



