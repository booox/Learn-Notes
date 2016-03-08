# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Id97Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    year = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    stars = scrapy.Field()
    type = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    release_dates = scrapy.Field()
    duration = scrapy.Field()
    rate_douban = scrapy.Field()
    rate_imdb = scrapy.Field()
    tags = scrapy.Field()
    d_links = scrapy.Field()
    
