import os, shutil, glob, traceback
from redvid import Downloader

import render
import reddit_scraper
import upload
import config


def main():
    # Open comma separated database. If doesn't exist, make it.
    try:
        database = open(config.database, 'r').read().split(',')
    except FileNotFoundError:
        database = ''
        open(config.database, 'x')

    # Delete temp_clips and remake it to empty the content
    if os.path.exists("temp_clips"):
        shutil.rmtree("temp_clips")
    os.makedirs("temp_clips")

    # Get list of videos from Reddit
    vid_list = reddit_scraper.scrape_reddit(config.subreddit)

    # Download the first video that is less than 180s and not in the database
    for vid in vid_list:
        reddit = Downloader(max_q=True)
        reddit.url = vid["url"]
        if (reddit.duration < 180) and (vid["url"] not in database):
            break
        else:
            vid = None

    # Check if a suitable video was found
    if not vid:
        print("No videos less than 180s found!")
        return False

    print("Video chosen:", vid)
    
    # Update the database with the video's URL
    # If upload fails or succeed, video will not be picked again.
    with open(config.database, "a") as f:
        f.write(f"{vid['url']},")

    reddit_scraper.download_vid(vid["url"], "temp_clips")

    shutil.copy(glob.glob(os.path.join('temp_clips', '*.mp4'))[0], os.path.join('temp_clips', 'main_clip.mp4'))
    render.render("temp_clips", "main_clip.mp4", "output.mp4", config.video["dimensions"])

    # Upload the video to YouTube
    config.youtube["title"] = vid["title"] + " #shorts"
    config.youtube["description"] = "Video by: " + vid["author"]
    
    print("Uploading...")
    uploaded = upload.upload("temp_clips/output.mp4", config.youtube)

    return uploaded


if __name__ == "__main__":
    # Attempt 10 attempts before quitting
    # This is due to packages this project relies on are not being reliable
    success = None
    for attempt in range(10):
        try:
            success = main()
        except Exception as e:
            print(f"Error occured on {attempt + 1}:\n", traceback.format_exc(), "\nRetrying...")

        if success:
            print("Video uploaded successfully! Check YouTube :)")
            break
