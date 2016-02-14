# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhwcItem(scrapy.Item):
    # define the fields for your item here like:
    # pass
    title = scrapy.Field()
    link = scrapy.Field()
    pub_time = scrapy.Field()
    tags = scrapy.Field()
    cates = scrapy.Field()
    read_count = scrapy.Field()
    comment_count = scrapy.Field()
    bookmark_count = scrapy.Field()
    quote_count = scrapy.Field()
    recommend = scrapy.Field()
    content = scrapy.Field()
