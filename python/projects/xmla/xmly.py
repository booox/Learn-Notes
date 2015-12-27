#coding=utf-8

HOME_URL = 'http://www.ximalaya.com'




class Zhubo(object):
    def __init__(self, 
            zbid      = None,
            name = None,
            url         = None,
            fans        = 0,
            follow   = 0,
            sound      = 0,
            desc        = None ):
        
        self.zbid = zbid
        self.name = name
        self.url = url
        self.fans = fans
        self.follow = follow
        self.sound = sound
        self.desc = desc
        
        
class Album(object):
    def __init__(self,
            aid              = None,
            name        =   None,
            url             =   None,
            category   =   None,
            tag             =   None,
            playcount   =  0,
            sounds      =   0,
            update_time =   None):
            
        self.aid         =   aid
        self.name   =   name
        self.url   =   url
        self.category   =   category
        self.tag   =   tag
        self.playcount   =   playcount
        self.sounds   =   sounds
        self.update_time   =   update_time
        
class Sound(object):
    def __init__(self,
            sid      =   None,
            name    =   None,
            url         =   None,
            playcount  =   0,
            createtime  =   None,
            like        =   0,
            comment     =   0,
            forward         =   0
            ):
        
        self.sid                 =    sid
        self.name           =   name
        self.url                =   url
        self.playcount     =   playcount
        self.createtime    =   createtime
        self.like              =   like
        self.comment     =   comment
        self.forward        =   forward
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        