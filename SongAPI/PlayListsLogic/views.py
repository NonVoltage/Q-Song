from django.shortcuts import render

from django.http import HttpResponse , Http404
from .models import PlayList



def getAllPlayListOfClient(request,userId):
    try:
        playlist = PlayList.objects.get(owner = userId)
        return HttpResponse("Here your track %s"%playlist)
    except PlayList.DoesNotExist :
        raise Http404("You dont have any playlsit")

def getSpecificTrack(request,track_id):
    try:
        track= PlayList.objects.get(pk=track_id)
    except PlayList.DoesNotExist:
        raise Http404("Track doesnt exist") 
    return HttpResponse("Here your track %s"%track)


