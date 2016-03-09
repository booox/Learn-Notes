# -*- coding: utf-8 -*-

import scrapy

import requests
from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest

from bmlw.items import BmlwItem


class Id97Spider(InitSpider):
    name = "id97"
    allowed_domains = ["www.id97.com"]
    start_urls = [
        "http://www.id97.com/videos/movie?page=1",
    ]

    def pretty_print(self, string, level):
        print '\t' * (level - 1), '=' * 5, string, '=' * 5
        
    def get_cookies(self):
        """ Get cookies from requests session"""
        
        self.pretty_print('get_cookies start', 1)
        
        headers = { 
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
        } 
        # form_data={"username": 'a',"password":'a',"loginsubmit":'true'} 
        s = requests.Session() 
        # r = s.post(self.login_page, data=form_data, headers=headers) 
        r = s.get(self.start_urls[0], headers=headers)
        cookies = r.cookies
        cookie_dict = {}
        for k,v in r.cookies.items():
            cookie_dict[k] = v
            
            
        return cookie_dict
    
    def init_request(self):
        """This function is called before crawling starts. """
        
        self.pretty_print('init_request start', 1)

        return Request(
            url=self.start_urls[0],
            cookies = self.get_cookies(),
            callback=self.parse_item)
            
    def parse_item(self, response):
        """ Scrape data from list page """
        self.pretty_print('parse_item start', 1)
        
        for href in response.xpath('//div[@class="movie-item-in"]/a'):
            _url = href.xpath('@href')[0].extract()
            self.pretty_print(_url, 2)
            
        
    def parse_movie_info(self, response):
        """ Scrape data from detail page """
        
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        