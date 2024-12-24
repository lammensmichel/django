from django.db import models
from django.contrib.auth.models import User

class TodoUserProfile(models.Model):

    account = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=16)
    lucky_number = models.IntegerField()