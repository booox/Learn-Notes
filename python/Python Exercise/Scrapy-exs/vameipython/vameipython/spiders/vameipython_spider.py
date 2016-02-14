# -*- coding: utf-8 -*-

import scrapy

from vameipython.items import VameipythonItem

class VameipythonSpider(scrapy.Spider):
    name = "vameipython"
    allowed_domains = ["www.cnblogs.com"]
    start_urls = [
        "http://www.cnblogs.com/vamei/archive/2012/09/13/2682778.html"
    ]
    
    def parse(self, response):
        for href in response.xpath('//div[@id="cnblogs_post_body"]/p/span/a/@href'):
            url = response.urljoin(href.extract())
            print url
            yield scrapy.Request(url, callback=self.parse_post_contents)
        
        # for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            # url = response.urljoin(href.extract())
            # print '\t\t ----- ', url
            # yield scrapy.Request(url, callback = self.parse_dir_contents)
            
    
    def parse_post_contents(self, response):
        item = VameipythonItem()
        item['title'] = response.xpath('//h1/a/text()').extract()
        item['link'] = response.url
        print '\t\t', response.url
        item['content'] = response.xpath('//div[@id="cnblogs_post_body"]').extract()
        
        yield item
            
            
            
       
            
            
            