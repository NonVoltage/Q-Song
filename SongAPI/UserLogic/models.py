from django.db import models

class Clients(models.Model):
    id = models.PositiveIntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    photo = models.FileField(upload_to='Photo/User')

    def __str__(self):
        responce = f"Id:{self.id}\n"
        responce += f"Name:{self.name}\n"
        responce += f"Email:{self.email}\n"
        responce += f"Photo:{self.photo}\n"
        try:
            aut = Author.objects.get(id = self.id)
            responce += f'Is author'
        except:
            responce += f'Isnt author'
                
        return responce


class Author(models.Model):
    user = models.ForeignKey(Clients , on_delete=models.CASCADE)
    tracks = models.ManyToManyField("tracks.TrackLogic")
