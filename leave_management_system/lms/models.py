from django.db import models
class Members(models.Model):
    first_name = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    email = models.EmailField()
    year = models.IntegerField()
    image = models.ImageField(upload_to='member_images/', blank=True)
    def __str__(self):
        return f"{self.first_name}"
