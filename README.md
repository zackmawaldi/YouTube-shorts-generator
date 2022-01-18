# YouTube shorts generator from trending Reddit videos

### Background
I had the initial idea that content between platform is very transformative. A lot of Youtube content could be transformed into TikTok content, Instagram to Facebook, Reddit to YouTube, etc. So I decided to start with a slice of this idea. Reddit to Youtube. I chose to make the videos in Youtube shorts format since it's a new field on Youtube, less established, more likely to gain following.

### Usage
I designed the code so that it could be uploaded to an AWS EC2 to make this process fully automatic and in the background.


### Dependencies
- httplib2
- apiclient
- oauth2client
- moviepy → you will need ffmpeg with it
- skimage → for effects in render.py (such as blur)
- praw
- redvid
