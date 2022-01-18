<img width="750" alt="portfolio_view" src="https://construyenpais.com/wp-content/uploads/YouTube-y-Reddit-las-redes-que-mas-crecieron-en-EE.UU-durante-la-pandemia.png">

# Automatic YouTube Shorts Generator and Uploader (From Trending Reddit Videos)

### Background
I had the initial idea that content between platform is very transformative. A lot of Youtube content could be transformed into TikTok content, Instagram to Facebook, Reddit to YouTube, etc. So I decided to start with a slice of this idea. Reddit to Youtube. I chose to make the videos in Youtube shorts format since it's a new field on Youtube, less established, more likely to gain following.

At the same time, I wanted to work with automated video editing, EC2 and SSH, and managing code and files in more pythonic and organized way.

### Usage
I designed the code so that it could be uploaded to an AWS EC2 to make this process fully automatic and in the background.

`main.py` is designed to do the following:
Get posts from PRAW API via `reddit_scraper.py` → download first post that's under 3 min (shorts limit) → render video in vertical format via `render.py` → upload to youtube via `uploadYT.py`

`uploadYT.py` is modified sample code from Google's YouTube Data 4 API

edit `config.py` for desired setttings

Reddit API and YouTube Data 4 API are used. YouTube API is kind of a pain to set up; there are videos on it on YouTube (meta!). Replace `client_secrets.json` key with key provided by YouTube Data 4 API. Ensure that 'Manage your YouTube videos' is enabled.

### Dependencies
- httplib2
- apiclient
- oauth2client
- moviepy → you will need ffmpeg with it
- skimage → for effects in `render.py` (such as blur)
- praw
- redvid

### Rights
Feel free to fork and play around with it. If you're going to use the code commercially, let me know.
