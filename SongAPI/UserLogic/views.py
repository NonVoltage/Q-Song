from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Clients , Author
from django.contrib.auth.hashers import make_password,check_password


def getAllUsers(request):
    try :
        users = Clients.objects.all()
        return users
    except:
        return Http404("Database isnt avalilable")
    
def getUserById(request,id):
    try:
        user = Clients.objects.get(pk=id)
        return user
    except: 
        return Http404("User doesnt exist")
    
def getUserByAuth(request):
    return HttpResponse("Yooo! Hallo!")

def createUser(request,newName,newPassword,newEmail,newPhoto):
    try:
        Clients.objects.create(name=newName,
                           password=make_password(newPassword),
                           email=newEmail,
                           photo=newPhoto)
    except:
        return Http404('Some arguments isnt right')
    

def showUserInfoById(request,userId):
    try:
        user = Clients.objects.get(pk=userId)
        context = {
            'name':user.name,
            'email':user.email,
            'photoPath': user.photo
        }
        return render(request , "users/dislayUser.html",context)
    except:
        raise Http404("User doesnt exist!")


