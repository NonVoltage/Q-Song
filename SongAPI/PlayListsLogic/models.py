from django.db import models
import uuid
import os

def playlist_photo_path(instance, filename):
    filetype = os.path.splitext(filename)[1].lower()
    return f"photo/playlists/{uuid.uuid4()}{filetype}"


class PlayList(models.Model):
    id = models.PositiveIntegerField(primary_key=True,unique=True)
    owner = models.ForeignKey(to='UserLogic.Clients' , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300,default='')
    number_of_track = models.PositiveIntegerField()
    createDate = models.DateField()
    tracks = models.ManyToManyField(to='TrackLogic.Track')
    photo = models.ImageField(upload_to=playlist_photo_path)


    def __str__(self):
        responce = f"Id:{self.id}\n"
        responce += f"Name:{self.name}\n"
        responce += f"Author:{self.owner}\n"
        responce += f"Tracks:{self.number_of_track}\n"
        responce += f"Posted at:{self.createDate}\n"
        responce += f"List of tracks:{self.tracks}\n"
        responce += f"Description:{self.description}\n"

                
        return responce
