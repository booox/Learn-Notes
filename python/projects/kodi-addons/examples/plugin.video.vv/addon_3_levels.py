# -*- coding: utf-8 -*-
# helloworld.py
# hello world demo
import xbmcplugin
import xbmcgui
# import sys

# url='http://tv1.btv.com.cn/asset/2012/03/27/BTV1_20120327_183405049_742928_23560.mp4'
url_v = 'http://111.1.61.53/hc.yinyuetai.com/uploads/videos/common/2B290152ED2E24DAC111BC91AC4A2D8F.flv?sc=43e8780c324425a5&br=783&vid=2499516&aid=39679&area=US&vst=0&ptp=mv&rd=yinyuetai.com'

dirs = [('大栏目', 3), ('小栏目', 5), ('视频', 10)]

print '---- BEGIN -----'
handle=int(sys.argv[1])
dir_level = 0
is_folder = True

if sys.argv[2] != '':
    dir_level = int(sys.argv[2][1:])
    
url = sys.argv[0] + '?' + str(dir_level + 1)

if dir_level == 2:
    is_folder = False
    url = url_v

print "sys.argv [0]: %s, [1]: %s, [2]: %s" % (sys.argv[0], sys.argv[1], sys.argv[2])
print "name : %s " % dirs[dir_level][0]

for count in range(dirs[dir_level][1]):
    list_item = xbmcgui.ListItem(dirs[dir_level][0] + str(count + 1))
    xbmcplugin.addDirectoryItem(handle, url, list_item, is_folder)
    
xbmcplugin.endOfDirectory(handle)

print '---- END -----'