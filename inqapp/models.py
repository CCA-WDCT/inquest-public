from django.db import models
import os
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from datetime import datetime


def default_score():
    return 0


class CustomUser(AbstractUser):
    user_name = models.CharField(blank=False, max_length=10)
    name = models.CharField(blank=False, max_length=20)
    score=models.IntegerField(default=default_score())
    college=models.CharField(max_length=30,blank=False,null=False)
    email_confirmed = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now_add=False,null=True)
    def __str__(self):
        return self.name
    def publish(self):
        self.save()

class Question(models.Model):
    question=models.CharField(max_length=300)
    image=models.ImageField(upload_to='images/',help_text='Please upload an image',blank=True)
    answer=models.CharField(max_length=50,blank=False)
    message=models.CharField(max_length=300,blank=True)
    def publish(self):
        self.save()

    def __str__(self):
        return self.question


class Event(models.Model):
    Event_name=models.CharField(default="inquest",max_length=50,blank=False)
    event_start=models.DateTimeField(auto_now_add=False)
    event_end=models.DateTimeField(auto_now_add=False)
