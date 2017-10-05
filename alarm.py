import sys
import os
from urllib.request import urlretrieve
import feedparser
from pygame import mixer
from podcasts import podcasts

# Use quotes around argument
podcast = sys.argv[1]

feed=feedparser.parse(f'https://www.npr.org/rss/podcast.php?id={str(podcasts[podcast])}')
items = feed['entries']
podcast_name = items[0].title
podcast_url = items[0].links[0].href

# download file and save to archive
if os.path.isdir(f'archive/{podcast}'):
    urlretrieve(podcast_url, 
                f'/home/tburke/podcast-alarm/archive/{podcast}/{podcast_name}.mp3')
else:
    os.mkdir(f'archive/{podcast}')
    urlretrieve(podcast_url,
                f'/home/tburke/podcast-alarm/archive/{podcast}/{podcast_name}.mp3')

# TODO play mp3

def play_podcast(podcast):
    mixer.init()
    mixer.music.play(f'archive/{podcast}/{podcast_name}.mp3')
    mixer.music.stop()

if __name__ == '__main__':
    play_podcast(podcast)
