from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
class Members(models.Model):
    first_name = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    email = models.EmailField()
    year = models.IntegerField()
    image=models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return f"{self.first_name}"
