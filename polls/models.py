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
    firstName = models.CharField(max_length=50, default="", null=True)
    lastName = models.CharField(max_length=50, default="", null=True)
    jerseyNumber = models.IntegerField(default=0, null=True)
    team = models.ForeignKey(NBATeam,
    on_delete = models.CASCADE, null=True)
    totalPoints = models.FloatField(default=0.0, null=True)
    totalRebounds = models.FloatField(default=0.0, null=True)




#do migrations every time you edit any models


#python manage.py makemigrations
#python manage.py migrate
