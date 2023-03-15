from django.db import models
class Members(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    email = models.EmailField()
    # def __str__(self):
    #     return self.first_name
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)