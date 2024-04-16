from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tender(models.Model):
    name = models.CharField(max_length=200)
    close_date = models.DateField()
    open_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
class OEM(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=200)
    rating = models.CharField(max_length=1)
    region = models.CharField(max_length=20)
    notifications = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class TENDERER(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    notifications = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class BIDDER(models.Model):
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    notifications = models.IntegerField(default=0)

    def __str__(self):
        return self.username