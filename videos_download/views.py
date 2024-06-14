from django.shortcuts import render, redirect

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
            return redirect(list_videos)

    form = YoutubeForm()
    return render(request, "videos_download/home.html", {"form": form})


def list_videos(request):
    context = {
        "videos": request.session.get("videos"),
    }
    return render(request, "videos_download/download_page.html", context)


def dowload(request, id):
    pass
