from skimage.filters import gaussian
from moviepy.editor import VideoFileClip, CompositeVideoClip, vfx
import os

import config


def blur(image):
    """Returns a blurred (radius=2 pixels) version of the image."""
    return gaussian(image.astype(float), sigma=25)


def render(directory, clip_name, output_name, resolution):
    """
    Resizes, centers, and renders a video clip with optional edge blur if needed.

    Args:
        directory (str): Directory path of the clip.
        clip_name (str): Name of the clip file.
        output_name (str): Desired name of the output file.
        resolution (tuple): Tuple of the desired resolution of the video.

    Returns:
        int: 0 for successful rendering and 1 if the video fits the desired format already.
    """
    if resolution is None:
        print("Config set to pass clip as is. Obliging, passing render.")
        os.rename(os.path.join(directory, "main_clip.mp4"), os.path.join(directory, "output.mp4"))
        return 1

    clip_dir = os.path.join(directory, clip_name)
    main_clip = VideoFileClip(clip_dir)

    exact_ratio = main_clip.size[0] / main_clip.size[1]
    theoretical_ratio = resolution[0] / resolution[1]
    
    if theoretical_ratio * 0.95 < exact_ratio < theoretical_ratio * 1.05:
        print(f"Clip is very close to theoretical aspect ratio!\n"
              f"Exact: {exact_ratio}\n"
              f"Theoretical: {theoretical_ratio}")
        os.rename(os.path.join(directory, "main_clip.mp4"), os.path.join(directory, "output.mp4"))
        return 1

    # Make background a blurred and darkened version of clip
    bg = VideoFileClip(clip_dir).resize(resolution)
    bg = bg.fx(vfx.colorx, 0.1)
    if config.video['blur']:
        bg = bg.fl_image(blur)

    main_clip = main_clip.resize(width=resolution[0])
    main_clip = main_clip.set_start(0)

    video = CompositeVideoClip([bg, main_clip.set_position("center", "center")])
    video.write_videofile(os.path.join(directory, output_name), audio_codec='aac')

    return 0
