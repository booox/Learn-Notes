# import sqlite3
# import pickle
import xmly
import sys
import os
import os.path
import subprocess

title = "some"
M4A_DIR =  'D:\\xmly\\m4a\\' + title  # 'C:\\Users\\username'
MP3_DIR =  'D:\\xmly\\mp3\\' + title  # 'C:\\Users\\username'
FFMPEG = 'd:\software\mycmdbat\ffmpeg\bin\ffmpeg.exe'


def m4aToMp3(m4a_path, mp3_path):
    
    if not os.path.isdir(m4a_path):
        os.makedirs(m4a_path)
    if not os.path.isdir(mp3_path):
        os.makedirs(mp3_path)
    
    filenames = [
        filename for filename in os.listdir(m4a_path)
        if filename.endswith('.m4a')
        ]
        
    for filename in filenames:
        print '\n\nStart'
        subprocess.call([
            "ffmpeg", "-i", 
            os.path.join(m4a_path, filename), 
            "-acodec", "libmp3lame", "-ab", "256k", 
            os.path.join(mp3_path, '%s.mp3' % filename[:-4])
            ])
        print '\n\nEnd#'
    return 0
    
if __name__ == '__main__':
    m4a_path = M4A_DIR
    mp3_path = MP3_DIR
    print m4a_path, mp3_path
    status = m4aToMp3(m4a_path ,mp3_path)
    sys.exit(status)



# conn = sqlite3.connect("xmly.sqlite")
# cur = conn.cursor()

# album_id = '2754031'
# cur.execute("SELECT tag, sound_count, sound_ids, update_time FROM Album WHERE album_id = ?",(album_id, ))

# data = cur.fetchone()

# tag = pickle.loads(data[0])
# sound_count = data[1]
# sound_ids = pickle.loads(data[2])
# update_time = data[3]




# print "\t album_id in database ", album_id
# print update_time, sound_count
# print 'tag:', tag
# print 'Sound ids:', sound_ids

# for t in tag:
    # print t.decode('utf-8')


# sys.stdout = xmly.Logger('log.txt')
# sys.stderr = xmly.Logger('log.txt')
# print "Hello world !" # this is should be saved in yourlogfilename.txt

# try:
    # abc
# except:
    # print 'wrong'
    
# print toi

# for i in range(20):
    # print i
    
# print 'hello world'

# a = raw_input('Enter word:')
# print a
# print 'dflkdfj'