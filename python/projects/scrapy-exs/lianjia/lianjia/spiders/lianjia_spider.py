# -*- coding: utf-8 -*-

import scrapy

from scrapy.spiders.init import InitSpider

from lianjia_shub.items import LianjiaShubItem



class LianjiaSpider(InitSpider):

    name = "lianjia"

    allowed_domains = ["http://bj.lianjia.com/chengjiao/"]

    start_urls = []



    def init_request(self):

        return scrapy.Request('http://bj.lianjia.com/chengjiao/pg1/', callback=self.parse_detail_links)



    def parse_detail_links(self, response):

        house_lis = response.css('.clinch-list li')

        for house_li in house_lis:

            link = house_li.css('.info-panel h2 a::attr("href")').extract_first().encode('utf-8')

            self.start_urls.append(link)

        return self.initialized()



    def parse(self, response):

        house = LianjiaShubItem()

        house['link'] = response.url

        house['id'] = response.url.split('/')[-1].split('.')[0]

        image_url = response.css('.pic-panel img::attr(src)').extract_first()

        # image是一个list。在Scrapinghub中显示的时候会把image里所有的图片显示出来。

        house['image'] = [image_url, image_url]

        house['title'] = response.css('.title-box h1::text').extract_first()

        house['addr'] = response.css('.info-item01 a::text').extract_first()

        house['price'] = response.css('.love-money::text').extract_first()

        return house