from django.contrib import admin

# Register your models here.

from .models import Profile, NBAPlayer, NBATeam, NBAPlayer2

admin.site.register(Profile)
admin.site.register(NBAPlayer)
admin.site.register(NBATeam)
admin.site.register(NBAPlayer2)
