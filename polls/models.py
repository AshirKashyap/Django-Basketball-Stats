from django.db import models
from django.contrib.auth.models import User

class NBATeam(models.Model):
    teamName = models.CharField(max_length=70, default="")
    city = models.CharField(max_length=50, default="")
    mascot = models.CharField(max_length=50, default="")

class Profile(models.Model):
    favTeam = models.ForeignKey(NBATeam,
    on_delete = models.CASCADE)

class NBAPlayer(models.Model):
    firstName = models.CharField(max_length=50, default="")
    lastName = models.CharField(max_length=50, default="")
    jerseyNumber = models.IntegerField(default=0)
    team = models.ForeignKey(NBATeam,
    on_delete = models.CASCADE)
    totalPoints = models.IntegerField(default=0)
    totalRebounds = models.IntegerField(default=0)

#do migrations every time you edit any models


#python manage.py makemigrations
#python manage.py migrate
