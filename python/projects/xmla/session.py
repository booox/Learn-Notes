# encoding: utf-8

#!/usr/bin/env python

import xmly
import json
import re

try:
	import requests
	from bs4 import BeautifulSoup
except:
	print "Library requests/BeautifulSoup NOT FOUND, and We need them."
    
class XMLYSession(requests.Session):
	""" Wrapper of requests.Session at zhihu.com. """

    def __init__(self):
        r = self.get(url=xmly.HOME_URL)
        self._cookies = r.cookies
        
        
    def getZhuboProfile(self, url=None):
        """   Get a zhubo's profile, url is the zhubo's homepage url  """
        
        if url:
            zhubo = xmly.Zhubo()    # create a Zhubo instance
            zhubo.url  = url
            zhubo.zbid = url[len(xmly.HOME_URL + '/zhubo/'):].replace('/', '')
        else:
            
            