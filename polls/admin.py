from django.contrib import admin

# Register your models here.

from .models import Profile, NBAPlayer, NBATeam

admin.site.register(Profile)
admin.site.register(NBAPlayer)
admin.site.register(NBATeam)
