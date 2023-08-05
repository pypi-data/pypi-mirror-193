""" Generate content from new rss entries.
"""
import logging
from urllib.parse import urlparse

import click
import feedparser
from bs4 import BeautifulSoup

from byb.core import Bot, PostContent
from byb.bots.core import platform_opt
from byb.utils import browser

log = logging.getLogger(__name__)

class RssFeedBot(Bot):

    def _parse_feed_entry(self, rss_feed, entry) -> PostContent:
        domain = urlparse(rss_feed).netloc
        feed_link = entry.get("link", "")
        html_content = entry.get("content", [{}])[0].get("value", "")
        text_content = browser.strip_tags(html_content)
        soup = BeautifulSoup(html_content)
        img_tag = None
        # img_tag = soup.find("img")
        if not img_tag:
            log.info(f"no image found, screenshotting {feed_link}")
            media = browser.screenshot(feed_link)
        else:
            media = img_tag['src']
            if media.startswith("/"):
                media = f"https://{domain}{media}"
            log.info(f"found image: {media}")
            media = browser.download_file(media)
        text = f"""
        New post on {domain} ...

        {text_content[0:640]}

        .
        .
        .
        #bot #byb #rss_feed #{domain.replace('.', '_')}
        """
        return PostContent(media, text, urls=[feed_link])


    def generate(self, **kwargs) -> PostContent:

        rss_feed = kwargs.get("rss_feed")
        entries = []
        if not rss_feed:
            raise ValueError(f"{self.name} requires an 'rss_feed'")
        try:
            entries = feedparser.parse(rss_feed).entries
        except Exception as e:
            log.error(f"Could not parse feed {rss_feed} because of {e}. Returning None")
            return None
        # TODO exclude recent by checking cache somwehre?
        return self._parse_feed_entry(rss_feed, entries[1])



@click.command()
@click.option("-r", "--rss-feed", help="The rss feed to check.")
@platform_opt
def cli(**kwargs):
    RssFeedBot().post_content_to_platforms(**kwargs)
