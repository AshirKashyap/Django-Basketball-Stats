from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Importing the User model as well as some other important things

from .models import NBATeam, NBAPlayer, Profile, NBAPlayer2
# Importing the models

# Side note: I had four views (BaseView, Index, Points and Rebounds)
# However, for concision and because it made more sense, I deleted the Points and Rebounds
# views, templates, and urls in order to make it all into the Index view
# So, I had to delete a lot of code which made it more streamlined

class BaseView(View):
    # Purpose: This function works to display the base.html template
    # Parameters: The only parameter is View which is a built in view model from django
    # Return: There is a return that renders base.html (in other words loads that page)

    # The post and get methods automatically seperate the data accordingly
    def post(self, request):
        context = {}

        return render(request, 'polls/base.html', context)
        # renders the polls/base.html page (which basically just loads that page)

    def get(self, request):
        context = {}

        return render(request, 'polls/base.html', context)
        # renders the polls/base.html page (which basically just loads that page)


        # f = open("data.txt", "r")
        #
        #
        # for line in f:
        #     strSpl = line.split(",")
        #     fname = strSpl[0]
        #     lname = strSpl[1]
        #     team = strSpl[4]
        #     gamesPlayed = int(strSpl[7])
        #     twoPointPer = float(strSpl[18]) * 100
        #     threePointPer = float(strSpl[15]) * 100
        #     rebounds = float(strSpl[25])
        #     ppg = float(strSpl[31])
        #
        #
        #
        #     newPlayer = NBAPlayer(totalRebounds = rebounds, totalPoints = ppg, firstName = fname, lastName = lname)
        #     newPlayer = NBATeam(teamName = team)
        #     newPlayer = NBAPlayer2(gamesPlayed = gamesPlayed, twoPointPer = twoPointPer, threePointPer = threePointPer)
        #     newPlayer.save()
        #
        #
        #
        #
        # f.close()

        # This code reads in data from the data.txt file and seperates it using split
        # While looping through each line of data, it creates a new player with the appropriate data

class IndexView(View):
    # Purpose: This function works to display the index.html template and its data
    # Parameters: The only parameter is View which is a built in view model from django
    # Return: There is a return that renders index.html (in other words loads that page)

    # The post and get methods automatically seperate the data accordingly
    players = NBAPlayer.objects.all()

    def post(self, request):
        foundPlayer = False
        # Checking to see if it found the right player
        for player in self.players:
            if str(player.firstName) + " " + str(player.lastName) == str(request.POST['firstName']):
                # This if statement checks to see if the first and last name match the full name of the player
                # (the key firstName refers to the full name of the player)
                selectedPlayer = player
                selectedPlayer2 = NBAPlayer2.objects.get(player = selectedPlayer)
                # selected player 2 is for the NBAPlayer2 objects
                # -- a workaround because i cannot edit the NBAPlayer model
                context = {
                    'players': self.players,
                    'selectedPlayer': selectedPlayer,
                    'addedFields': selectedPlayer2,
                }
                foundPlayer = True
                # If it finds the right player, sets foundPlayer to True
        if not foundPlayer:
            context = {}
            # This prevents the program from crashing because it ensures that either way context is defined

        return render(request, 'polls/index.html', context)
        # renders the polls/index.html page (which basically just loads that page)


    def get(self, request):
         context = {
            'players': self.players,
         }

         return render(request, 'polls/index.html', context)
         # renders the polls/index.html page (which basically just loads that page)
