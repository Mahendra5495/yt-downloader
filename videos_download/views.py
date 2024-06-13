from django.shortcuts import render, redirect

# from django.urls import reverse
from .forms import YoutubeForm
from .service import get_resolutions


def home(request):
    if request.method == "POST":
        form = YoutubeForm(request.POST)
        if form.is_valid():
            url = request.POST.get("url")
            available_resolutions = get_resolutions(url)
            request.session["video_url"] = url
            request.session["resolutions"] = available_resolutions
            return redirect(download)

    form = YoutubeForm()
    return render(request, "videos_download/home.html", {"form": form})


def download(request):
    context = {
        "resolutions": request.session.get("resolutions"),
    }
    return render(request, "videos_download/download_page.html", context)
