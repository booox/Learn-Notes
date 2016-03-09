# -*- coding: utf-8 -*-


import requests
import sys

import scrapy
from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest

from id97.items import Id97Item


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
        
        if "page=6" in response.url:
            self.pretty_print('CTRL+C', 1)
            sys.exit(0)
        
        for href in response.xpath('//div[@class="movie-item-in"]/a'):
            _url = href.xpath('@href')[0].extract()
            url = response.urljoin(_url)
            self.pretty_print(url, 2)
            
            yield scrapy.Request(_url, callback=self.parse_movie_info)
            
        next_page = response.xpath('//a[@rel="next"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            self.pretty_print(url, 3)
            
            yield scrapy.Request(url, self.parse_item)
        
    def parse_movie_info(self, response):
        """ Scrape data from detail page """
        # pass
        
        # #### Init the infos dictionary
        infos = {}
        
        # ### get all the items ##### 
        title = response.xpath('//h1/text()')[0].extract()
        year = response.xpath('//h1/span/text()')[0].extract()[1:-1]
        
        # tags
        tag_wrap = response.xpath('//div[@class="col-md-12 tags"]/a/text()')        
        tags = []
        for tag in tag_wrap:
            tags.append(tag.extract())
            
        # dowoload links
        movie_id = response.url.split('/')[-1][:-5]
        tag_wrap = response.xpath('//a[@mid="%s"]' % movie_id)
        dl_links = []
        
        #   # if there are download links
        if tag_wrap:            
            for tag in tag_wrap:
                dl_title = tag.xpath('@title').extract()[0]
                dl_href = tag.xpath('@href').extract()[0]
                
                dl_links.append([dl_title, dl_href])
        
        # movie scores - douban
        douban_score = response.xpath('//a[@class="score"]/text()')[0].extract()[-3:]
        douban_url = response.xpath('//a[@class="score"]/@href')[0].extract()
        
        # movie scores - imdb
        imdb = response.xpath('//a[@class="imdb"]/@href')
        imdb_score = ''
        imdb_url = ''        
        #   # change imdb info, if imdb exist
        if imdb:
            imdb_score = response.xpath('//a[@class="imdb"]/text()')[0].extract()[-3:]
            imdb_url = response.xpath('//a[@class="imdb"]/@href')[0].extract()
        
        
        # #### Add info into infos dictionary
        infos['douban_score'] = douban_score
        infos['douban_url'] = douban_url
        infos['imdb_score'] = imdb_score
        infos['imdb_url'] = imdb_url
        
        
        # ### get other infos, such as director, writer, etc.
        tds = response.xpath('//table[@class="movie-info-table"]/tbody/tr/td')
        
        infos_field = {
            "导演": "xpath('a/text()').extract()",
            "编剧": "xpath('a/text()').extract()",
            "主演": "xpath('a/text()').extract()",
            "类型": "xpath('a/text()').extract()",
            "国家": "xpath('a/text()').extract()",
            "语言": "xpath('text()').extract()",
            "时间": "xpath('text()').extract()",
            "片长": "xpath('text()').extract()",
            "又名": "xpath('text()').extract()",
        }
        
        
        # get the index of the field name
        info_field_index = [x for x in range(0, len(tds)) if x % 2 == 0]
        # not include the score, douban & imdb
        for x in info_field_index[:-1]:
            field = tds[x].xpath('span/text()').extract()[0][:-1]
            
            self.pretty_print(len(field), 2)
            self.pretty_print(type(field), 2)
            # self.pretty_print(type("导演"), 2)
            # self.pretty_print(len("导演"), 2)
            
            # self.pretty_print(field, 2)
            field = field.encode('gbk')
            self.pretty_print(len(field), 2)
            self.pretty_print(type(field), 2)
            # self.pretty_print('AF:' + type(field), 2)
            # self.pretty_print(field, 2)
            # self.pretty_print(infos_field["导演"], 2)
            
            self.pretty_print("tds[x+1]." + infos_field[field], 2)
            result = eval("tds[x+1]." + infos_field[field])
            
            infos[field] = result
            
            
            
        
        item = Id97Item()
        
        item['title'] = title
        item['year'] = year
        item['tags'] = tags
        item['dl_links'] = dl_links
        item['infos'] = infos
        
        
        yield item
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        