import praw
import config
import subprocess
from redvid import Downloader


def download_vid(url, directory):
    """
    Download a video from a given URL and save it to a specified directory.

    Args:
    url (str): The URL of the video to download.
    directory (str): The directory to save the downloaded video

    Returns:
    None
    """
    print(f"Attempting to download the following reddit video: {url}")
    
    download = Downloader(url, max_q=True)
    download.path = directory
    download.download()


def scrape_reddit(subreddit):
    """
    Scrape top posts from a specified subreddit and return a list of dictionaries containing post information.

    Args:
    subreddit (str): The name of the subreddit to scrape.

    Returns:
    A list of dictionaries containing post information.
    """
    print("Logging into Reddit...")
    red = praw.Reddit(**config.reddit_login)
    print("Log in success! Retrieving post info...")
    sub = red.subreddit(subreddit).top("week", limit=99)
    output = []

    for i in sub:
        if not i.stickied and not i.over_18:
            url = i.url
            if url.split('.')[0] != 'https://v':
                continue
            output.append({
                'url': url,
                'title': i.title,
                'author': i.author.name
            })

    print("Scraping reddit success! Returning list of info back to main.")
    return output
