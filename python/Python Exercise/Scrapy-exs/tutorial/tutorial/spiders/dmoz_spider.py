# -*- coding: utf-8 -*-

import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    
    def parse(self, response):
    
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            print '\t\t ----- ', url
            yield scrapy.Request(url, callback = self.parse_dir_contents)
            
    def parse_dir_contents(self, response):        
        
        tag_wrap = response.xpath('//ul[@class="directory-url"]/li')
        for tag in tag_wrap:
            item = DmozItem()
            item['title'] = tag.xpath('a/text()').extract()
            item['link'] = tag.xpath('a/@href').extract()
            item['desc'] = tag.xpath('text()').extract()
            yield item
            
            
            
       
            
            
            