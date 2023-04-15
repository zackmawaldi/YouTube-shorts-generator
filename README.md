<img width="750" alt="portfolio_view" src="https://construyenpais.com/wp-content/uploads/YouTube-y-Reddit-las-redes-que-mas-crecieron-en-EE.UU-durante-la-pandemia.png">

# Automatic YouTube Shorts Generator and Uploader

### Background
I had the initial idea that content between platform is very transformative. A lot of Youtube content could be transformed into TikTok content, Instagram to Facebook, Reddit to YouTube, etc. I decided to start with a slice of this idea. Reddit to Youtube. I chose to make the videos in Youtube shorts format since it's a new field on Youtube, less established, more likely to gain following.

At the same time, I wanted to work with automated video editing, and learning to manage code and files in a more pythonic and organized way.

### Usage
I designed the code so that it could be uploaded to an AWS EC2 to make this process fully automatic and in the background.

`main.py` is designed to do the following:
Get posts from PRAW API via `reddit_scraper.py` → download first post that's under 3 min (shorts limit) → render video in vertical format via `render.py` → upload to youtube via `upload.py`

`upload.py` is heavily modified sample code from Google's YouTube Data 4 API

Edit `config.py` for desired settings. Please edit it or the code won't work.

Reddit API and YouTube Data 4 API are used. YouTube API is kind of a pain to set up; there are videos on it on YouTube (meta!). Replace `client_secrets.json` key with key provided by YouTube Data 4 API. Ensure that 'Manage your YouTube videos' is enabled.

To get the ability to make your videos public, your program has to go through audit process.
Check out this: https://support.google.com/youtube/contact/yt_api_form

### Dependencies
- httplib2
- apiclient
- oauth2client
- moviepy → you will need ffmpeg with it
- skimage → for effects in `render.py` (such as blur)
- praw
- redvid

### Rights
Feel free to fork and play around with it. You can not use the code commercially before negotiating a deal with me.

### UPDATE
*2023-04-15*
Google's authentication has changed, and now it's much harder to authenticate through the terminal. I recommend using a computer with a user interface to authenticate and run the program! So, imo, don't bother with EC2, and just use an old/spare laptop if you have one.

I wrote this project early in my programming career, and thought I'd come back to it to re-write most of the code to make it much more readable and dynamic. Hope this helps with the issues!