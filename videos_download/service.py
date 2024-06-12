from pytube import YouTube

def get_resolutions(url):
    all_videos = YouTube(url)
    videos = all_videos.streams.filter(progressive=True)
    availabe_resolutions = [video.resolution for video in videos]
    return availabe_resolutions