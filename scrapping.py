# -*- coding: utf-8 -*-
"""
Created on Tue May 03 17:35:22 2016

@author: user
"""

from lxml import html
import requests
import mechanize
from bs4 import BeautifulSoup

result = []

def cleanLinks(baseUrl, links):
    cleaned = []
    for link in links:
        if(link):
            if(link[0] == 'h'):
                cleaned.append(link)
            elif(link[0] == '/'):
                cleaned.append(baseUrl + link)
    return cleaned
'''    
def crawl(url, referal, depth):
    if(depth > 0):'''
                
baseUrl = 'http://mashable.com'   
url = 'http://mashable.com/2016/05/02/standing-desk-kids/'
basePage = requests.get(url)
basePageTree = html.fromstring(basePage.content)
basePageLinks = [t.get('href') for t in basePageTree.xpath('//a')]
basePageLinks = cleanLinks(baseUrl, basePageLinks)

selectedLinks = basePageLinks[58:60]

lists = []
br =  mechanize.Browser()
for lists in selectedLinks:
    htmltext = br.open(lists).read()
    soup = BeautifulSoup(htmltext)
    artikel = ""
    for tag in soup.findAll('p'):
        artikel += tag.text
    print soup.title.string, artikel