from django.db import models
from UserLogic.models import Clients

class Track(models.Model):
    id = models.PositiveIntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length= 100)
    author = models.ForeignKey(Clients , on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    duration = models.PositiveIntegerField()
    photo = models.FileField(upload_to='Photo/Track')
    postDate = models.DateField()
    genre = models.CharField(max_length=40)
    path = models.FileField(upload_to=f'Songs/{genre}')
    likes = models.PositiveIntegerField()

    
    def __str__(self):
        responce = f"Id:{self.id}\n"
        responce += f"Name:{self.name}\n"
        responce += f"Author:{self.author}\n"
        responce += f"Likes:{self.likes}\n"
        responce += f"Duration:{self.duration}\n"
        responce += f"Posted at:{self.postDate}\n"
        responce += f"Genre:{self.genre}\n"
        responce += f"Description:{self.description}\n"
        responce += f"File:{self.path}\n"
        responce += f"Photo:{self.photo}\n"

                
        return responce
