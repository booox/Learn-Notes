# -*- coding: utf-8 -*-

import scrapy
import random
import time
import sys
from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule
import requests

from bmlw.items import BmlwItem

class BmlwSpider(InitSpider):
    name = "bmlw"
    allowed_domains = ["www.ebama.net"]
    login_page = 'http://www.ebama.net/member.php?mod=logging&action=login'
    start_urls = [
        "http://www.ebama.net/home.php?mod=space&uid=1020&do=thread&view=me&order=dateline&from=space",
    ]
    
    rules = (
        Rule(SgmlLinkExtractor(allow=()), callback='parse_item', follow=True
        ),
    )
    
    def get_cookies(self):
        """ Get cookies from requests session"""
        headers = { 
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        } 
        form_data={"username": 'a',"password":'a',"loginsubmit":'true'} 
        s = requests.Session() 
        r = s.post(self.login_page, data=form_data, headers=headers) 
        cookies = r.cookies
        cookie_dict = {}
        for k,v in r.cookies.items():
            cookie_dict[k] = v
            
            
        return cookie_dict
    
    def init_request(self):
        """This function is called before crawling starts. """
        print '=======================INIT======================='
        return Request(
            url=self.login_page, 
            cookies = self.get_cookies(),
            callback=self.check_login_response)
        
    # def login(self, response):
        """ Generate a login request. """
        # print '=======================LOGIN======================='
        # return FormRequest.from_response(
            # response,
            # formdata={},
            # callback=self.check_login_response
        # )
        
    def check_login_response(self, response):
        """ Check the response returned by a login request to see if we are 
        successfully logged in.        
        """
        print '=======================CHECK LOGIN======================='
        
        if "action=login" in response.body:
            self.logger.error("Login Failed!")
            print "============== Bad times :( ===============" 
            return
        
        # Now the crawling can begin..
        self.log("Successfully logged in. Let's Moving!")
        print "========= Successfully logged in. ========="
        
        yield Request(self.start_urls[0], callback=self.parse_item) 
        
        
    
    def parse_item(self, response):
        # Scrape data from page
        
        print "============== PARSE ITEM =========================="
        for href in response.xpath('//th/a'):
            title = href.xpath('text()')[0].extract()
            _url = href.xpath('@href')[0].extract()
            print ' - ' * 15, type(_url), _url
            print ' - ' * 15, type(title), title
            url = response.urljoin(_url)
            print url
            yield Request(url, callback=self.parse_thread_contents)
    
        
        next_page = response.xpath('//a[@class="nxt"]/@href')
        if next_page:
            next_url = response.urljoin(next_page[0].extract())
            print next_url
            yield Request(next_url, self.parse_item)
    
    
    def parse_thread_contents(self, response):
        item = BmlwItem()
        
        cates = response.xpath('//h1/a/text()')[0].extract()[1:-1]
        title = response.xpath('//h1/a/text()')[1].extract()
        link = response.url        
        forum = response.xpath('//div[@id="pt"]/div/a/text()')[2].extract()
        content = response.xpath('//div[@class="t_fsz"]')[0].extract()
        
        print cates, title, forum, link
        print content[:20]
        
        item['title'] = title
        item['link'] = link
        item['cates'] = cates
        item['forum'] = forum
        item['content'] = content
        
        yield item
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

            
            
       
            
            
            