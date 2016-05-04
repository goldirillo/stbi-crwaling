# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:25:22 2016

@author: user


import sys
sys.path.append('/usr/lib/python2.7/dist-packages/')
from bs4 import BeautifulSoup
"""

from lxml import html
import requests
laman = requests.get('http://mashable.com/2016/05/02/standing-desk-kids/')
pohon = html.fromstring(laman.content)
judul = pohon.xpath('//h1[@class="title"]/text()')

"""
http://www.imdb.com/
page = requests.get('http://www.detik.com/')
tree = html.fromstring(page.content)

<div title="buyer-name">Carson Busses</div>
<span class="item-price">$29.95</span>

http://www.detik.com/

#username
<a href="/channel/UCwxso1rgEhmTePGJbQdmSVw" class="yt-uix-sessionlink comment-author-text g-hovercard      spf-link " data-sessionlink="itct=CMUCELZ1IhMI5bj_-f-1zAIVQpJoCh3YRQo0" data-ytid="UCwxso1rgEhmTePGJbQdmSVw">Haise Leonhardt</a>
#komen
<div class="comment-renderer-text-content">Khaleesi you're supposed to rule!!!!﻿</div>

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')

print 'Buyers: ', buyers
print 'Prices: ', prices


//*[@id="productlistcontainer"]/li[1]/a/span[1]/span[1]
<span class="prod-itm-fullname">APPLE iPhone 6 64Gb (Garansi Apple International) - White</span>
produk = tree.xpath('//span[@class="prod-itm-fullname"]/text()')

<a href="//news.detik.com" data-category="GA WP New Detikcom 2015" data-action="Navbar Atas" data-label="detikNews">detikNews</a>
tautan = tree.xpath('//a[@href]text()')

<span id="ctl00_content_rptProduct_ctl05_lblSalePrice" class="prod-itm-price">Rp 14,995,000</span>
prod-itm-price
harga = tree.xpath('//span[@class="prod-itm-price"]/text()')

komentar = tree.xpath('//span[@class="comment-renderer-text-content"]/text()')

http://www.bhinneka.com/search.aspx?Search=iphone


page = requests.get('http://www.bhinneka.com/search.aspx?Search=iphone')

In [27]: tree = html.fromstring(page.content)

In [28]: tree
Out[28]: <Element html at 0x1573b048>

In [29]: harga = tree.xpath('//span[@class="prod-itm-price"]/text()')

In [30]: harga

page = requests.get('http://www.bhinneka.com/search.aspx?Search=iphone')
tree = html.fromstring(page.content)

tree.xpath()
"""