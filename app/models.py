from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField() 
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.name

ts = [
    (1,"11:00AM - 12:00AM"),
    (2,"12:00AM - 1:00PM"),
    (3,"1:00PM - 2:00PM"),
    (4,"2:00PM - 3:00PM"),
    (5,"3:00PM - 4:00PM"),
    (6,"4:00PM - 5:00PM"),
    (7,"5:00PM - 6:00PM"),
    (8,"6:00PM - 7:00PM"),
    (9,"7:00PM - 8:00PM"),
    (10,"8:00PM - 9:00PM"),
    (11,"9:00PM - 10:00PM"),
]
class Book(models.Model):
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    date = models.DateField()
    time = models.IntegerField(choices=ts)