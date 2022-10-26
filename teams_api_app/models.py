from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    Conference = models.CharField(max_length=100)
    wins = models.IntegerField()
    loses = models.IntegerField()

class Player(models.Model):
    name = models.CharField(max_length=100)
    positon = models.CharField(max_length=100)
    age = models.IntegerField()
    injured = models.BooleanField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')