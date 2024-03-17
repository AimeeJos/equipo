from django.shortcuts import render
from django.views.generic import View
from assignment_1.extract_data import extract_data
from common.helpers import download_file


class Home(View):

    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


def assign1(request):
    context = extract_data()
    return render(request, "assign1.html", {"context": context})


class DownloadFileViews(View):

    def get(self, request, taskid):
        response = download_file("downloads", f"{taskid}.xlsx")
        return response
