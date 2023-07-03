import os
import shutil
from moviepy.editor import *
import wave
import math
from PIL import Image, ImageDraw
import youtube_dl
import random


# Define the file extensions for each section
text_ext = '.txt'
audio_ext = '.mp3'
video_ext = '.mp4'
physical_ext = '.jpg'
visual_ext = '.jpg'

# Define the directory paths for each section
text_dir = 'assets/submissions/text'
audio_dir = 'assets/submissions/audio'
video_dir = 'assets/submissions/video'
physical_dir = 'assets/submissions/physical'
visual_dir = 'assets/submissions/visual'

# Create the real files for each section
for i in range(10):
    # Create the file names for each section using the index number
    text_file = 'text-file-' + str(i) + text_ext
    audio_file = 'audio-file-' + str(i) + audio_ext
    video_file = 'video-file-' + str(i) + video_ext
    physical_file = 'physical-file-' + str(i) + physical_ext
    visual_file = 'visual-file-' + str(i) + visual_ext

    # Create the real files for each section
    with open(text_dir + '/' + text_file, 'w') as f:
        f.write('This is a text file.')

    # Define the audio duration and sample rate
    duration = 10
    sample_rate = 44100

    # Create a new WAV file with one channel and 16-bit depth
    with wave.open(audio_dir + '/' + audio_file, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)

        # Generate a sine wave with a frequency of 440 Hz
        for j in range(duration * sample_rate):
            value = abs(int(32767 * math.sin(2 * math.pi * 440 * j / sample_rate)))
            f.writeframesraw(value.to_bytes(2, 'little'))


# # Define the directory path for the downloaded videos
#     video_dir = 'assets/videos'

#     # Define the YouTube search query and options
#     query = 'cat'

#     options = {
#         'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
#         'outtmpl': video_dir + '/random-video.%(ext)s',
#         'quiet': True,
#         'no_warnings': True,
#         'prefer_ffmpeg': True,
#         'postprocessors': []
#     }

#     # Search for the videos and download a random one
#     with youtube_dl.YoutubeDL(options) as ydl:
#         results = ydl.extract_info('ytsearch:' + query, download=False)
#         videos = [v for v in results['entries'] if v.get('duration') and v.get('url') and v['duration'] < 120]
#         video = random.choice(videos)
#         ydl.download([video['url']])

#     print('Video downloaded successfully.')

    # Create a video clip with a solid color background
    # background_clip = ColorClip(size=(640, 480), color=(255, 255, 255), duration=10)

    # # Create a text clip with a message
    # text_clip = TextClip(txt='This is a video file.', fontsize=50, color='black').set_position('center').set_duration(10)

    # # Combine the background and text clips
    # final_clip = CompositeVideoClip([background_clip, text_clip])

    # # Write the final clip to a video file
    # final_clip.write_videofile(video_dir + '/' + video_file, fps=25)

    # Create a new image with a solid color
    width = 640
    height = 480
        # Create a new image with a white background
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # Draw a checkerboard pattern with random colors
    draw = ImageDraw.Draw(image)

    for x in range(0, width, 20):
        for y in range(0, height, 20):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            draw.rectangle((x, y, x+10, y+10), fill=color)

    # Save the image to a file
    image.save(physical_dir + '/' + physical_file)

    image.save(visual_dir + '/' + physical_file)



print('Real files created successfully.')