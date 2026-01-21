from django.shortcuts import render

from django.http import HttpResponse , Http404
from .models import Track

def getAllTracks(request):
    try:
        all = Track.objects.all()
    except Track.DoesNotExist:
        raise Http404('Sorry we dont have anything')
    return HttpResponse(all)

def getSpecificTrack(request,track_id):
    try:
        track = Track.objects.get(pk=track_id)
    except Track.DoesNotExist:
        raise Http404("Track doesnt exist") 
    return HttpResponse(track)

