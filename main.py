import os, shutil, glob
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
            print("Video chosen:")
            for key, value in vid.items(): print(key, value)
            reddit_scraper.download_vid(vid["url"], "temp_clips")
            break

    # Check if a suitable video was found
    if not os.listdir("temp_clips"):
        print("No videos less than 180s found!")
        return False

    os.rename(glob.glob(os.path.join('temp_clips', '*.mp4'))[0], os.path.join('temp_clips', 'main_clip.mp4'))
    render.render("temp_clips", "main_clip.mp4", "output.mp4", config.video["dimensions"])

    # Upload the video to YouTube
    config.youtube["title"] = vid["title"] + " #shorts"
    config.youtube["description"] = "video by: " + vid["author"]
    uploaded = upload.upload("temp_clips/output.mp4", config.youtube)

    # Update the database with the uploaded video's URL
    with open(config.database, "a") as f:
        f.write(f"{vid['url']},")

    return uploaded


if __name__ == "__main__":
    max_attempts = 10
    success = False
    for attempt in range(max_attempts):
        try:
            success = main()
            if success:
                print("Upload Success!")
                break
        except Exception as e:
            print(f"An error occurred in main() on attempt {attempt+1}: {e}")
    
    if not success:
        print(f"Attempted to upload {max_attempts} times with no luck... ending script.")
