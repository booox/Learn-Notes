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

    def getData(self, url, **kwargs):
        res = self.get(url=url, **kwargs)
        self._cookies = res.cookies
        return res
        
	def postData(self, url, data=None, **kwargs):
		data['_xsrf'] = self._cookies['_xsrf']
		return self.post(url=url, data=data, cookies = self._cookies, **kwargs)
        
    def getZhuboProfile(self, url=None):
        """   Get a zhubo's profile, url is the zhubo's homepage url  """
        
        # simple check zhubo url
        url_prefix = xmly.HOME_URL + '/zhubo/'
        _zbid = url[len(xmly.HOME_URL + '/zhubo/'):].replace('/', '')
        if not url.startswith(url_prefix) or not _zbid.isdigit():
            print "[URL ERROR] : Please check the zhubo homepage url."
            pass
            exit(0)
        else:
            zhubo = xmly.Zhubo()    # create a Zhubo instance
            zhubo.url  = url
            zhubo.zbid = _zbid
            
            res = self.getData(zhubo.url)
            soup = BeautifulSoup(res.text)
            
            try:
                # balba
            except:
                raise
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            