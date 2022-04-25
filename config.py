subreddit = "funny"  # exclude 'r/'

reddit_login = {  # more info to set up rovided by reddit api documentation
	'client_id': '',
	'client_secret': '',
	'password': '',
	'user_agent': '',
	'username': ''
}


youtube = {
	'title': '',
	'description': '',
	'tags': '',
	'category': 23,  # has to be an int, more about category below
	'status': ''  # {public, private, unlisted}
}

video = {
	'dimensions': (1080, 1920),  # (horizontal, vertical), currently set vertically for tiktok
	'blur': True  # blur non-perfect-fit clip
}


"""
for category: has to be an int, refer to YouTube Data 4 API's documentation, but as of Jan 2022,
checkout https://techpostplus.com/youtube-video-categories-list-faqs-and-solutions/
"""
