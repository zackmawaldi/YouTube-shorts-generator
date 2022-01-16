from moviepy.editor import *
from skimage.filters import gaussian

import config


def blur(image):
    """ Returns a blurred (radius=2 pixels) version of the image """
    return gaussian(image.astype(float), sigma=25)


def render(directory,
           clip_name,
           output_name,
           resolution):  # dir and names are strings, resolution is a tuple

    blur = config.video['blur']
    
    clip_dir = directory + clip_name
    main_clip = VideoFileClip(clip_dir)

    ratio = main_clip.size[0]/main_clip.size[1]
    if 0.56 < ratio < 0.565:
        print(f"clip is very close to 9:16!\n"
              f"exact: {ratio}\n"
              f"theoretical: 0.5625")
        os.rename(directory + "main_clip.mp4", directory + "output.mp4")
        return 1

    """ Make bg be a blurred and darkened version of clip """
    bg = VideoFileClip(clip_dir).resize(resolution)
    bg = bg.fx(vfx.colorx, 0.5)
    if blur:
        bg = bg.fl_image(blur)
    """"""

    main_clip = main_clip.resize(width=resolution[0])  # resize clip to fit screen
    main_clip = main_clip.set_start(0)

    video = CompositeVideoClip([bg, main_clip.set_position("center", "center")])  # combine bg and clip with centering
    video.write_videofile(directory + output_name, audio_codec='aac')  # render clip given directory
    return 0


""" Example usage below """
# render("/Users/zack/PycharmProjects/tiktokGen/clips/", "0.mp4", "functionTest.mp4", (576, 1024))
