from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage


def main(request):
    return render(request, "Home.html")


def data(request):
    print(request.POST)
    return render(request, "reg.html")


def register(request):
    return render(request, "Home.html")
