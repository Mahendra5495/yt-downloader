from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
import os

# from django.urls import reverse
from .forms import YoutubeForm
from .service import fetch_videos


def home(request):
    if request.method == "POST":
        form = YoutubeForm(request.POST)
        if form.is_valid():
            url = request.POST.get("url")
            videos = fetch_videos(url)

            request.session["videos"] = videos
            request.session["id"] = videos["id"]
            return redirect(video_list)

    form = YoutubeForm()
    return render(request, "videos_download/home.html", {"form": form})


def video_list(request):
    if request.method == "POST":
        resolution = request.POST.get("resolution")
        id = request.session["id"]
        request.session["reso"] = resolution
        return redirect(download)
    context = request.session.get("videos")
    return render(request, "videos_download/download_page.html", context)


def download(request):
    id = request.session.get("id")
    resolution = request.session.get("reso")
    if not id or not resolution:
        return HttpResponse("Invalid Request", status=400)
    file_name = f"{id}_{resolution}.mp4"
    file_path = os.path.join(settings.MEDIA_ROOT, settings.DOWNLOAD_DIR, file_name)
    if not os.path.exists(file_path):
        return HttpResponse("File not found", status=404)

    response = HttpResponse(open(file_path, "rb").read(), content_type="video/mp4")
    response["Content-Disposition"] = f'attachment; filename="{file_name}"'
    return response
