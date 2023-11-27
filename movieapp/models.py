from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    Year = models.CharField(max_length=250)
    price= models.CharField(max_length=250)
    img  =  models.ImageField(upload_to='pic')
    
    def __str__(self):
        return self.name
