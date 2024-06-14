from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("video-list/", views.video_list, name="video_list"),
    path("download/", views.download, name="download"),
]
