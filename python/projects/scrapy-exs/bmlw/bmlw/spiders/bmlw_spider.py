# -*- coding: utf-8 -*-

import scrapy
import random
import time

from bmlw.items import BmlwItem

class BmlwSpider(scrapy.Spider):
    name = "bmlw"
    allowed_domains = ["www.ebama.net/"]
    start_urls = [
        "http://www.ebama.net/home.php?mod=space&uid=1020&do=thread&view=me&order=dateline&from=space",
    ]
    
        
    def parse(self, response):
        """
            simulate user login
        """
        
        # time.sleep(random.random())
        
        return scrapy.FormRequest.from_response(
            response,
            formdata = {'username': '', 'password': ''},
            callback = self.after_login
        )
        
    
    def after_login(self, response):
        # check login succeed before going on
        
        if "action=login" in response.body:
            self.logger.error("Login failed")
            print 'Login failed.'
            return
            
        # continue scraping with authenticated session... 
        print 'Login In!'
        
    
        # for href in response.xpath('//span[@class="atc_title"]/a'):
            # _url = href.xpath('@href')[0].extract()
            # url = response.urljoin(_url)
            # print url
            # yield scrapy.Request(url, callback=self.parse_blog_contents)
        
        # next_page = response.xpath('//li[@class="SG_pgnext"]/a/@href')
        # if next_page:
            # url = response.urljoin(next_page[0].extract())
            # yield scrapy.Request(url, self.parse)
            
    # def parse_blog_contents(self, response):        
        
        # title = response.xpath('//h2/text()')[0].extract()
        # link = response.url
        # pub_time = response.xpath('//span[@class="time SG_txtc"]/text()')[0].extract()
        # pub_time = pub_time[1:-1]       # 2015-05-12 08:21:59
        # tags = response.xpath('//td[@class="blog_tag"]/h3/a/text()').extract()  # [u'\u8d22\u7ecf', u'\u7ecf\u6d4e\u5b66']
        # cates = response.xpath('//td[@class="blog_class"]/a/text()')[0].extract()
        # read_count = None           # javascript content 
        # comment_count = None       # selenium 
        # bookmark_count = None
        # quote_count = None
        # _recommend = response.xpath('//img[@class="SG_icon SG_icon107"]')
        # if _recommend:
            # recommend = 1
        # else:
            # recommend = 0
        # content = response.xpath('//div[@id="sina_keyword_ad_area2"]').extract()
        
        # item = ZhwcItem()
        
        # item['title'] = title
        # item['link'] = link
        # item['pub_time'] = pub_time
        # item['tags'] = tags
        # item['cates'] = cates
        # item['read_count'] = read_count
        # item['comment_count'] = comment_count
        # item['bookmark_count'] = bookmark_count
        # item['quote_count'] = quote_count
        # item['recommend'] = recommend
        # item['content'] = content
         
            
        # yield item
            
            
            
       
            
            
            