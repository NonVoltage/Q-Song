from django.db import models
from TrackLogic.models import Track
from UserLogic.models import Clients

class PlayList(models.Model):
    id = models.PositiveIntegerField(primary_key=True,unique=True)
    owner = models.ForeignKey(Clients , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300,default='')
    number_of_track = models.PositiveIntegerField()
    createDate = models.DateField("date published")
    tracks = models.ManyToManyField(Track)


    def __str__(self):
        responce = f"Id:{self.id}\n"
        responce += f"Name:{self.name}\n"
        responce += f"Author:{self.owner}\n"
        responce += f"Tracks:{self.number_of_track}\n"
        responce += f"Posted at:{self.createDate}\n"
        responce += f"List of tracks:{self.tracks}\n"
        responce += f"Description:{self.description}\n"

                
        return responce
