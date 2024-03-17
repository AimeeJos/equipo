from django.urls import path, include
from assignment_1 import views


app_name = "assignment_1"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("assign1/", views.assign1, name="assign1"),
    path(
        "download_file/<str:taskid>",
        views.DownloadFileViews.as_view(),
        name="file_download",
    ),
]
