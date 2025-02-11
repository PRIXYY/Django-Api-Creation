from django.db import models

# Create your models here.
class Moviedata(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    Dname = models.CharField(max_length=200,default='Nolan')
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200,default='action')
    image = models.ImageField(upload_to='Images/',default="Images/None/Noimg.jpg")