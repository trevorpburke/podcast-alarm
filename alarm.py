import urllib
import feedparser
from podcasts import podcasts

feed=feedparser.parse(f'https://www.npr.org/rss/podcast.php?id={str(podcasts[podcast])}')
items = feed['entries']
podcast_date = items[0].title
podcast_url = items[0].links[0].href

# download file and save to archive
urllib.request.urlretrieve(podcast_url,
                           f'/home/tburke/npr-wakeup/archive/{podcast_date}.mp3')
