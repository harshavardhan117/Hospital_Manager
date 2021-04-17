from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE,default = None)
    name = models.CharField( max_length=100)
    disease= models.CharField( max_length=50)
    firstappointment = models.DateField(auto_now=False, auto_now_add=False, )
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.name

