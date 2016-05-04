# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:36:15 2016

@author: GOLDI-PC
"""

#import numpy as np
#from bs4 import BeautifulSoup
#import urllib
#r = urllib.urlopen('http://news.detik.com/internasional/3200969/rusuh-sabtu-malam-di-makkah-pekerja-konstruksi-bin-laden-bakar-9-bus').read()
#soup = BeautifulSoup(r)

"""for link in soup.find_all('a'):
    m=(link.get('href'))
    print m"""
    
#for list in range(0,5):

"""https://www.detik.com
for link in soup.find_all('a'):
    m=(link.get('href'))
    print m
    
for link in soup.find_all('a'):
    print(link.get('href'))
    
from HTMLParser import HTMLParser
class ekstraklink(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   print name, "=", value

parser = ekstraklink()
for line in soup:
    parser.feed(line)
    
    
<h1 class="title" href="http://mashable.com/2016/05/02/standing-desk-kids/">Standing desk for kids basically rewards squirming</h1>
"""
from bs4 import BeautifulSoup

import mechanize
br =  mechanize.Browser()

for daftar in selectedLinks:
    htmltext = br.open(daftar).read()
    soup = BeautifulSoup(htmltext)
    artikel = ""
    for tag in soup.findAll('p'):
        artikel += tag.text
    print soup.title.string, artikel



'''
parser = ekstraklink()
parser.feed('https://www.detik.com')
    '''