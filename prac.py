from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, AudioFileClip, concatenate_audioclips
import random


def merge_sc_audio(audio_file_title, comments, sc_title):
    video_clip = VideoFileClip("game1.mp4")
    id = audio_file_title.split("_")[0]
    audio_clip = AudioFileClip(audio_file_title)
    audio_duration = audio_clip.duration
    comment_clip = AudioFileClip(comments[0]+".mp3")
    comment_title = comments[0]+".png"
    comment_clip_duration = comment_clip.duration


    lower_limit = random.randint(0, int(video_clip.duration) - int(audio_duration) - int(comment_clip_duration) ) 
    
    video_clip = video_clip.subclip(lower_limit, lower_limit + int(audio_duration) + int(comment_clip_duration)+2) 


    overlay_image = ImageClip(sc_title)
    overlay_width = video_clip.w - 45
    overlay_height = video_clip.h - 105
    overlay_image = overlay_image.resize(width=300, height=200)

    overlay_duration = audio_duration 
    overlay_image = overlay_image.set_duration(overlay_duration)
    overlay_image = overlay_image.set_position(('center'))
    audio_clip = audio_clip.subclip(0, audio_duration)

    overlay_image2 = ImageClip(comment_title)
    overlay_width2 = video_clip.w - 1105
    # overlay_image2 = overlay_image2.resize()

    overlay_duration2 = comment_clip_duration
    start_time = audio_duration  

    
    overlay_image2 = overlay_image2.set_start(start_time)
    overlay_image2 = overlay_image2.set_duration(overlay_duration2)
    overlay_image2 = overlay_image2.set_position(('center'))
    comment_clip = comment_clip.subclip(0, comment_clip_duration)


    final_audio_clip = concatenate_audioclips([audio_clip, comment_clip])
    composite_clip = CompositeVideoClip([video_clip, overlay_image, overlay_image2])
    final_clip = composite_clip.set_audio(final_audio_clip)
    final_clip.write_videofile(f'final_video_{id}.mp4', codec='libx264', audio_codec='aac')

