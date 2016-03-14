from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Question(models.Model):
  title = models.Charfield(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  rating = models.IntegerField() 
  author = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
  likes = models.ManyToManyField(User)
  


class Answer(models.Model):
  text = models.TextField()
  added_at = models.DateTimeField(auto_now_add=True)
  question = models.ForeignKey(Question)
  author = models.ManyToManyField(User)


 

