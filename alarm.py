import sys
import os
from urllib.request import urlretrieve
import feedparser
import pygame
from datetime import datetime

from podcasts import podcasts

# Use quotes around argument
podcast = sys.argv[1]

feed = feedparser.parse(f'https://www.npr.org/rss/podcast.php?id={str(podcasts[podcast])}')
items = feed['entries']
podcast_ep = items[0].title
podcast_url = items[0].links[0].href

def play(podcast, podcast_ep):
    '''Plays mp3 files'''
    pygame.init()
    pygame.mixer.music.load(f'archive/{podcast}/{podcast_ep}.mp3')
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)

# download file and save to archive
if os.path.isdir(f'archive/{podcast}'):
    urlretrieve(podcast_url, 
               f'archive/{podcast}/{podcast_ep}.mp3')
    play(podcast, podcast_ep)
else:
    os.mkdir(f'archive/{podcast}')
    urlretrieve(podcast_url,
                f'archive/{podcast}/{podcast_ep}.mp3')
    play(podcast, podcast_ep)


