from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("video-list/", views.list_videos, name="list_videos"),
    path("download/<int:id>", views.dowload, name="download"),
]
