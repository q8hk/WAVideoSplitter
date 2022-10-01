from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import csv
import os
import moviepy.editor as mp

# name of output file
naming = 'trim_'
def get_sec(time_str):
    """Get Seconds from time."""
    time = time_str.split(':')
    if(len(time)==3):
        h = time[0]
        m = time[1]
        s = time[2]
        return int(h) * 3600 + int(m) * 60 + int(s)
    else:
        m = time[0]
        s = time[1]
        return int(m) * 60 + int(s)
print (os.getcwd())
file_name = "video.mp4"
duration = mp.VideoFileClip("video.mp4").duration
counter = 0
while duration > 30:
    end = 30
    if duration <= 30:
        end = duration
    else:
        end = (counter + 1) * 30
    start = counter * 30
    outname = "%s.mp4" % (counter)
    ffmpeg_extract_subclip(file_name, start, end, targetname=outname)
    counter = counter + 1
    duration = duration - 30