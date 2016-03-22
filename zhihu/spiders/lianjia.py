# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["http://nb.lianjia.com/chengjiao"]
    start_urls = (
        'http://www.http://nb.lianjia.com/chengjiao/',
    )

    def parse(self, response):
        pass
