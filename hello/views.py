from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def location_crash(request):
    return render(request, "location_crash_pad.html")


def tarifs(request):
    return render(request, "tarifs.html")


def tarif_grid(request):
    return render(request, "tarif_grid.html")



def photos(request):
    return render(request, "photos.html")