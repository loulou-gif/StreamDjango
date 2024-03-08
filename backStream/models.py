from django.db import models

# Create your models here.

class Streams(models.Model):
    name= models.CharField(max_length=50)
    authors= models.CharField(max_length=50)
    licence= models.CharField(max_length=50)
    studio= models.CharField(max_length=50)
    kind= models.CharField(max_length=50)
    time= models.CharField(max_length=50)
    synopsys= models.CharField(max_length=50)
    type= models.CharField(max_length=50)
    episode= models.CharField(max_length=50)
    banner= models.ImageField(upload_to='images/')
    video= models.ImageField(upload_to='videos/')
    poster= models.ImageField(upload_to='images/')
    season= models.CharField(max_length=50)
    
class News(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to='news/')