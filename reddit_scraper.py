import praw
from redvid import Downloader
import os

import config


def download_vid(url, directory):  # Download reddit vid given URL and directory
    download = Downloader(url, max_q=True)
    download.path = directory
    download.download()
    print(os.listdir(directory))


def reddit_scraper(subreddit):  # pulls out top reddit posts
    print("Logging into Reddit...")

    red = praw.Reddit(client_id=config.reddit_login['client_id'],
                      client_secret=config.reddit_login['client_secret'],
                      password=config.reddit_login['password'],
                      user_agent=config.reddit_login['user_agent'],
                      username=config.reddit_login['username'])

    print("Log in success! Retrieving post info...")

    sub = red.subreddit(subreddit).top("week", limit=25)

    output = []

    for i in sub:
        print(f"{i.title}")
        if not i.stickied and not i.over_18:
            url = i.url
            if url.split('.')[0] != 'https://v':
                continue
            title = i.title
            print('{}  {}  {}\n{}\n'.format(title, i.subreddit, i.author.name, url))
            output.append((url, title, i.author.name))

    return output


""" Testing code below """
# login_info_text = open('reddit_login_info.txt', mode='r').read().split(',')
# lst = reddit_scraper(login_info_text, "arabfunny", 1)
# print(lst)
# download_vid(lst[0][0], "/Users/zack/PycharmProjects/tiktokGen/clips/")
