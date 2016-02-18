# -*- coding: utf-8 -*-
# helloworld.py
# hello world demo
import xbmcplugin
import xbmcgui

# url='http://tv1.btv.com.cn/asset/2012/03/27/BTV1_20120327_183405049_742928_23560.mp4'
url = 'http://111.1.61.53/hc.yinyuetai.com/uploads/videos/common/2B290152ED2E24DAC111BC91AC4A2D8F.flv?sc=43e8780c324425a5&br=783&vid=2499516&aid=39679&area=US&vst=0&ptp=mv&rd=yinyuetai.com'


handle=int(sys.argv[1])
listitem=xbmcgui.ListItem('Hello, World!')

xbmcplugin.addDirectoryItem(handle, url, listitem)
xbmcplugin.endOfDirectory(handle)