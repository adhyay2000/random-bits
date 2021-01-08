from __future__ import unicode_literals
import youtube_dl
import datetime
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        with open(songs_dir+'/logger.txt','a') as log:
            log.write('{} ERROR:{}\n'.format(str(datetime.datetime.now()),msg))
def my_hook(d):
    if d['status'] == 'finished':
        with open(songs_dir+'/logger.txt','a') as log:
            log.write('{} INFO:Video File for {} is downloaded\n'.format(str(datetime.datetime.now()),d['filename']))
songs_dir = '' #Your songs directory goes here
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'download_archive':songs_dir+'/content.txt',
    'logger': MyLogger(),
    'outtmpl':songs_dir+'/%(title)s.%(ext)s',
    'progress_hooks': [my_hook]
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([
        # INSERT YOUR PLAYLIST(S) HERE IN COMMA-SEPERATED FORM
    ])