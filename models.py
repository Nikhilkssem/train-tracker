from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train_no = models.CharField(max_length=10)
    train_name = models.CharField(max_length=100)