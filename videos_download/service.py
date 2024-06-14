from pytube import YouTube
from django.conf import settings
import os

DOWNLOAD_DIR = "videos/"


def fetch_videos(url):
    all_videos = YouTube(url)
    videos = all_videos.streams.filter(progressive=True)
    video_files = download_videos(videos, all_videos)
    return video_files


def download_videos(videos, yt):
    video_files = []
    for stream in videos:
        file_name = f"{yt.video_id}_{stream.resolution}.mp4"
        file_path = os.path.join(settings.MEDIA_ROOT, DOWNLOAD_DIR, file_name)

        if not os.path.exists(file_path):
            stream.download(
                output_path=os.path.join(settings.MEDIA_ROOT, DOWNLOAD_DIR),
                filename=file_name,
            )
        video_files.append(
            {
                "resolution": stream.resolution,
                "url": os.path.join(settings.MEDIA_URL, DOWNLOAD_DIR, file_name),
            }
        )
    return video_files
