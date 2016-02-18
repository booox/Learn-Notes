

# Audio-video add-on tutorial

## Add-on structure

### Directory Name

* Your directory name should follow this convention: `<addon-type>[.<media-type>].<your-plugin-name>`
* *Add-on Type*
    * *repository* : add new repositories to the Kodi addon manager.
    * *plugin* : Plugins appear under the relevant media section of the main home menu.
    * *script* : A runnable program file that will appear in the Program section of the main home menu.
    * *skin* : An Kodi skin definition and its supporting script files.
    * *resource* : An addon that will provide additional files (language files, images, uisounds).
* *Media Type*
    * *plugin.audio* : 
    * *plugin.video* : 
    * *plugin.picture* : 
    * *plugin.weather* : 
    * *script.module* : 
    * *script.service* : 
    
    
### Directory structure

* The directory should be structured as follows:
    ```
    addon.py
    addon.xml
    changelog.txt
    fanart.jpg
    icon.png
    LICENSE.txt
    resources/
       settings.xml
       language/
       lib/
       data/
       media/    
    ```
* *addon.py* : the main Python code for your add-on.
    * You'll define this in *addon.xml*
* *addon.xml* : gives Kodi important metadata about your add-on, such as:
    * what the add-on provides
    * what the add-on relies on to work
    * what script to run when it is fired up
* *changelog.txt* : A text file that contains a description of the changes you make to the add-on for each release.
    * Here is a sample changelog.txt:
        ```
            v0.1.3 (2015-12-25)
            - Update with 15.0 Isengard

            v0.1.2  (2014-1-15)
            - Add notification for Ubuntu users checking through apt command

            v0.1.1  (2014-1-1)
            - Initial version        
        ```
* *icon.png* : his is an icon used to represent your add-on in various parts of XBMC. 
    * icon size must be: 256x256 pixels
    * file format: PNG
    * background must be: 100% solid. Just make sure there is no transparency.
    * Kepp the logo as simple as possible
* *fanart.jpg* 

* *LICENSE.txt* : This file should contain the text of whatever software license you've chosen to release your add-on under (e.g. GPLv2).
    
* *resources/* : The resources/ subdirectory is the preferred place to put any files that the add-on uses that don't need to be stored in the root directory.
    * *resources/settings.xml* : defines the user-configurable settings used by the add-on.
    * *resources/language/* : 
        * *Translation tools:*
        * *String ID range:* 
    * *resources/lib/* : Put any module definitions or third party software libraries into this directory.
    * *resources/data/* : Store any other static data structures your application requires here.
    * *resources/media/* : Store any static media (picture, audio, video etc.) files in this directory.
    
    
    
    
# HOW-TO:HelloWorld addon


* download the zip file (for installation in Kodi) here: [hello-world](https://github.com/zag2me/script.hello.world/archive/master.zip)
* Installing
    * System-Addon-install from the zip
* Testing
    * System >> Add-Ons >> Enabled Add-Ons >> Program Add-Ons >> Hello World.
    * You should now see a popup with 3 lines of text.
* Modifying the Add-On
    * you can simply go to the appdata folder and live edit it!
    * On windows this will be in: `C:\Users\user\AppData\Roaming\XBMC\addons\script.hello.world`
* Structure
    * *addon.py* : This is the actual python code for your Add-On
    * *addon.xml* : This is the Add-Ons metadata
    * *changelog.txt* : This is a text file with any change-log information in it. We advise updating this on each release.
    * *icon.png* : A PNG icon for the add-on. It can be 256x256 or 512x512 pixels big.
    * *LICENSE.txt* : Another text file with the Add-On license text.
    

    
# Q & A

* *failed to install dependency script.module.chardet*
    * download chardet addon from : [script.module.chardet-2.1.2.zip](http://mirrors.xbmc.org/addons/frodo/)
    * installed it, and resolve the error.
    
    
 

[todo] (http://bbs.htpc1.com/viewthread.php?tid=198731&page=2&authorid=511430)
    
    
    
    
    
    
    
