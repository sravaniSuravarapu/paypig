from django.db import models
import uuid
# Create your models here.

    



class Contact(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
    


class EarnerImage(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to="images/")
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title 
    
class VideoUpload(models.Model):
    title = models.CharField(max_length =255)
    video = models.FileField(upload_to="videos/")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE,related_name="video")
    
    class Meta:
        ordering =['-created_on']

    def __str__(self):
        return self.title



















