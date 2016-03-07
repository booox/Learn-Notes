
# Links
    * [FFmpeg Offical Site](http://ffmpeg.org/)
    * [FFmpeg download site](http://ffmpeg.zeranoe.com/builds/)
    * [FFmpeg Docs]


* How to Install FFmpeg on Windows
    *  [How to Install FFmpeg on Windows](http://adaptivesamples.com/how-to-install-ffmpeg-on-windows/)
    * STEPS:
        * Download Static Version: [http://ffmpeg.zeranoe.com/builds/](http://ffmpeg.zeranoe.com/builds/)
        * Unzip to a folder that's easy to find, (and you can rename it to *ffmpeg* )
        * Add to Windows Path and Reboot: *FFMPEG_DIR\bin* 
        * 
    * Examples
        * Make video from image sequence:
        `ffmpeg -i frame_%04d.png -c:v h264 test.mp4 – ‘%04d’ is the padding, like ‘frame_0001.png’`

        * lossless h264:
        `ffmpeg -i frame%04d.png -c:v libx264 -preset veryslow -qp 0 vid.mkv`
        `ffmpeg -i frame%04d.png -c:v libx264 -preset ultrafast -qp 0 vid.mkv` – larger file size, but quicker to encode

        * quicktime (camtasia can use these):
        `ffmpeg -i frame%04d.png -c:v prores vid_prores.mov`
        `ffmpeg -i frame%04d.png -c:v qtrle qtrle.mov` – possibly lossless compression

        * HTML5 supported video:
        `ffmpeg -i frame%04d.png -c:v libx264 -b:v 1M -c:a aac -r 10 output.mp4` 
            * `-r 10`  specifies a framerate of 10 fps
        `ffmpeg -i frame%04d.png -c:v libvpx -b:v 2M -c:a libvorbis -r 10 output.webm`
        `ffmpeg -i frame%04d.png -vf scale=680:-1 -c:v libvpx -b:v 2M output.webm`
            * – 680p (auto height), no audio

        * Make image sequence from video:
        `ffmpeg -i video.avi image%04d.png`
        `ffmpeg -i video.avi .\imgs\image%04d.png` 
            * – outputs the images to a folder (the folder must already exist!)

        * Get info on video:
        `ffmpeg -i video.avi`

        * Deshake video (stabalize):
        `ffmpeg -i input.mov -vf deshake output.mov`

        `Side-by-side:`
        `ffmpeg -i left_video.mov -vf "[in] scale=iw/2:ih/2, pad=2*iw:ih [left];movie=right_video.mov, scale=iw/2:ih/2 [right];[left][right] overlay=main_w/2:0 [out]" sidebyside.mov`
        
        
        音频转换：

        1.转换amr到mp3：

        ffmpeg -i shenhuxi.amr amr2mp3.mp3
        2.转换amr到wav：

        ffmpeg -acodec libamr_nb -i shenhuxi.amr amr2wav.wav
        3.转换mp3到wav：

        ffmpeg -i DING.mp3 -f wav test.wav
        4.转换wav到amr：

        ffmpeg -i test.wav -acodec libamr_nb -ab 12.2k -ar 8000 -ac 1 wav2amr.amr
        5.转换wav到mp3：

        ffmpeg -i test.wav -f mp3 -acodec libmp3lame -y wav2mp3.mp3
        视频转换：

        1.转换wmv到mp4：

        ffmpeg -i sample.wmv -vcodec libx264 -acodec aac out.mp4
        2.抓取H264视频流：

        ffmpeg -i sample.flv -vcodec copy -vbsf h264_mp4toannexb -an out.h264
         2.1 vbsf为过滤方法，即将flv规定的H264组织方式转换回H264协议书规定的字节流格式
         2.2 -an 禁掉源文件中的音频，因为出来的码流不需要音频
         2.3 vcodec copy这个是必然的

        3.将H264视频流转为mp4:

        ffmpeg -i sample.h264 -f mp4 haha.mp4
        4.接收rtsp并存为视频文件：

        ffmpeg -rtsp_transport tcp -i rtsp://streaming1.osu.edu/media2/ufsap/ufsap.mov -vcodec copy -acodec copy -t 30 -f mp4 rtsp-out.mp4
        4.1 -rtsp_transport tcp:指明传输方式是tcp方式(也可以是udp)

        4.2 -t 30：指明我录制30秒
        
        
        
* 

[m4a to mp3 with python and ffmpeg](http://stackoverflow.com/questions/11649918/convert-aac-m4a-files-to-mp3-in-directory)
```

#!/usr/bin/env python

import os
import os.path
import sys
import subprocess

OUTPUT_DIR = '/Users/matt/Desktop/mp3/'

def main():
    path = os.getcwd()
    filenames = [
        filename
        for filename
        in os.listdir(path)
        if filename.endswith('.m4a')
        ]

    for filename in filenames:
        subprocess.call([
            "ffmpeg", "-i",
            os.path.join(path, filename),
            "-acodec", "libmp3lame", "-ab", "256k",
            os.path.join(OUTPUT_DIR, '%s.mp3' % filename[:-4])
            ])
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)


```


[wav to mp3 ](http://stackoverflow.com/questions/6969464/write-a-simple-python-script-to-convert-all-wav-files-in-a-specific-folder-to)
```
import os
import os.path
import sys
from subprocess import call

def main():
    path = '/path/to/directory/'
    filenames = [
        filename
        for filename
        in os.listdir(path)
        if filename.endswith('.wav')
        ]
    for filename in filenames:
        call(['lame', '-V0',
              os.path.join(path, filename),
              os.path.join(path, '%s.mp3' % filename[:-4])
              ])
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)



```