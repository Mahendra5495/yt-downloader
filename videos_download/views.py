from django.shortcuts import render, redirect

# from django.urls import reverse
from .forms import YoutubeForm


def home(request):
    if request.method == "POST":
        form = YoutubeForm(request.POST)
        if form.is_valid():
            url = request.POST.get("url")
            request.session["video_url"] = url
            return redirect(download)

    form = YoutubeForm()
    return render(request, "videos_download/home.html", {"form": form})


def download(request):
    temp = request.session.get("url")
    return render(request, "videos_download/download_page.html", {"data": temp})
