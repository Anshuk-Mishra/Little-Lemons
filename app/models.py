from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField() 
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name
    
class Book(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    date = models.DateField()
    time = models.IntegerField()