from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.IntegerField(default=0)
    liked_users = models.ManyToManyField(User, related_name = "liked_users")

class Hashtag(models.Model):
    hashtag = models.CharField(max_length=200) 
    tweets = models.ManyToManyField(Tweet)
