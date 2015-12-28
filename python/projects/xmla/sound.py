#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xmly
from xmly_session import XMLYSession

if __name__ == '__main__':
    
    # flesh database
    # conn, cur = xmly.openDB()
    # xmly.initDB(cur)
    
    session = XMLYSession()
    url = 'http://www.ximalaya.com/zhubo/8889234/'
    url = 'http://www.ximalaya.com/zhubo/1000120/'
    url = 'http://www.ximalaya.com/8889234/album/'
    
    # zhubo = session.getZhuboProfile(url)
    # print zhubo.album, zhubo.follow, zhubo.fans 

    page_count = session.getPageCount(url)
    print page_count
    
    
    # close database
    # xmly.closeDB(conn)
