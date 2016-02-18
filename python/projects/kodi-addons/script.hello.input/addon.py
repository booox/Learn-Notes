import xbmc
import xbmcaddon
import xbmcgui
 
addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

your_name = xbmc.Keyboard("", "Please Input your Name:", False)
your_name.doModal()
if your_name.isConfirmed() and your_name.getText() != "":
    message1 = 'Hello World!'
    message2 = 'Nice to meet you %s' % (your_name.getText())
    message3 = 'Welcome to Kodi!'
 
    xbmcgui.Dialog().ok(addonname, message1, message2, message3)