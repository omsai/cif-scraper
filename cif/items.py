# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


KEYS = ['cif_id', 'methane_grav', 'methane_vol', 'void_fraction', 'sa_vol', 'num_interp_frameworks', 'url']

class CifItem(scrapy.Item):
    cif_id = scrapy.Field()
    methane_grav = scrapy.Field()
    methane_vol = scrapy.Field()
    void_fraction = scrapy.Field()
    sa_vol = scrapy.Field()
    num_interp_frameworks = scrapy.Field()
    url = scrapy.Field()
