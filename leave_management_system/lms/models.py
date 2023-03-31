from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Members(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    email = models.EmailField()
    year = models.IntegerField()
    mentee = models.CharField(max_length=100)    
    mentor = models.CharField(max_length=100)
    mentoremail=models.CharField(max_length=100)
    start_date= models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    reason= models.TextField()
    image=models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return f"{self.first_name}"
