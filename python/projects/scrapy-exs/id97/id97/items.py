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
    tags = scrapy.Field()
    dl_links = scrapy.Field()   #download links
    infos = scrapy.Field()
    
    # director = scrapy.Field()
    # writer = scrapy.Field()
    # stars = scrapy.Field()
    # type = scrapy.Field()
    # country = scrapy.Field()
    # language = scrapy.Field()
    # release_dates = scrapy.Field()
    # duration = scrapy.Field()
    # other_name = scrapy.Field()
    # douban_score = scrapy.Field()
    # douban_url = scrapy.Field()
    # imdb_score = scrapy.Field()
    
