from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile', blank=True, null=True)
    age = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.user.username
# Create your models here.
