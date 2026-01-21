from django.db import models
import uuid
import os

def track_photo_path(instance, filename):
    filetype = os.path.splitext(filename)[1].lower()
    return f"photo/tracks/{uuid.uuid4()}{filetype}"

def track_file_path(instance, filename):
    filetype = os.path.splitext(filename)[1].lower()
    genre = instance.genre.slug 
    return f"tracks/{genre}/{uuid.uuid4()}{filetype}"


class Track(models.Model):
    id = models.PositiveIntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length= 100)
    authors = models.ForeignKey(to='UserLogic.Author' , on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    duration = models.PositiveIntegerField()
    photo = models.ImageField(upload_to=track_photo_path)
    postDate = models.DateField()
    genre = models.CharField(max_length=40)
    path = models.FileField(upload_to=track_file_path)
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
