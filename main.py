import os
from redvid import Downloader

import render as r
import reddit_scraper as rs
import uploadYT as yt

import config

subreddit = config.subreddit  # subreddit wanted here


login_info_text = open('reddit_login_info.txt', mode='r').read().split(',')
directory = "temp_clips/"

for file in os.listdir(directory):
    os.remove(directory + file)

vid_list = rs.reddit_scraper(subreddit)

print(vid_list)

x = 0
while True:
    if x == len(vid_list):
        print("no vid less than 60s found!")
        break
    reddit = Downloader(max_q=True)
    reddit.url = vid_list[x][0]
    reddit.check()
    if reddit.duration < 180:
        rs.download_vid(vid_list[x][0], directory)
        break
    x += 1

os.rename(directory + os.listdir(directory)[0], directory + "main_clip.mp4")

r.render(directory, "main_clip.mp4", "output.mp4", config.video['dimensions'])

yt.upload2YT(directory + "output.mp4", config.youtube)

