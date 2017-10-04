import sys
import os
from urllib.request import urlretrieve
import feedparser
from podcasts import podcasts

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
