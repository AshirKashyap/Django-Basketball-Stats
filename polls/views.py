from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Importing the User model as well as some other important things

from .models import NBATeam, NBAPlayer, Profile
# Importing the models

class BaseView(View):
    # Purpose: This function works to display the base.html template and its data
    # Parameters: The only parameter is View which is a built in view model from django
    # Return: There is a return that renders base.html (in other words loads that page)
    points = NBAPlayer.objects.all()
    print(points)

    def post(self, request):
        if 'totalPoints' in request.POST.keys():
            print(request.POST['totalPoints'])
            context = {
                'points': self.points,
                'point': request.POST['totalPoints'],
            }

            print(totalPoints)
            return render(request, 'polls/points.html', context)

        else:
            return render(request, 'polls/points.html', context)

    def get(self, request):
        # print(request.GET.get('totalPoints'))
        context = {
            'points': self.points,
            # never printing points through get function
        }
        # f = open("data.txt", "r")
        #
        #
        # for line in f:
        #     strSpl = line.split(",")
        #     rebounds = float(strSpl[23])
        #     ppg = float(strSpl[29])
        #
        #     newPlayer = NBAPlayer(totalRebounds = rebounds, totalPoints = ppg)
        #
        #     newPlayer.save()
        #
        #
        # f.close()

        # This code reads in data from the data.txt file and seperates it using split
        # While looping through each line of data, it creates a new player with the appropriate data

        return render(request, 'polls/base.html', context)

class BasketballPoints(View):
    # Purpose: This function works to display the points.html template and its data
    # Parameters: The only parameter is View which is a built in view model from django
    # Return: There is a return that renders points.html (in other words loads that page)

    # The post and get methods automatically seperate the data accordingly
    points = NBAPlayer.objects.all()

    def post(self, request):
        if request.method == 'POST':
            print(request.POST['totalPoints'])
            context = {
                'points': self.points,
                'point': request.POST['totalPoints'],
            }

            return render(request, 'polls/points.html', context)

    def get(self, request):
        if request.method == 'GET':
            print(request.GET.get('totalPoints'))
            context = {
                'points': self.points,
                # never printing points through get function
            }

            return render(request, 'polls/points.html', context)



class BasketballRebounds(View):
    # Purpose: This function works to display the rebounds.html template and its data
    # Parameters: The only parameter is View which is a built in view model from django
    # Return: There is a return that renders rebounds.html (in other words loads that page)

    # The post and get methods automatically seperate the data accordingly

    rebounds = NBAPlayer.objects.all()

    def post(self, request):
        if request.method == 'POST':
            print(request.POST['totalRebounds'])
            context = {
                'rebounds': self.rebounds,
                'rebound': request.POST['totalRebounds'],
            }

            return render(request, 'polls/rebounds.html', context)


    def get(self, request):
        if request.method == 'GET':
            print(request.GET.get('totalRebounds'))
            context = {
                'rebounds': self.rebounds,
                # never printing the rebounds from the get function
            }

            return render(request, 'polls/rebounds.html', context)



class IndexView(View):
    # Purpose: This function works to display the index.html template and its data
    # Parameters: The only parameter is View which is a built in view model from django
    # Return: There is a return that renders index.html (in other words loads that page)

    # The post and get methods automatically seperate the data accordingly
    players = NBAPlayer.objects.all()

    def post(self, request):
        if request.method == 'POST':
            print(request.POST['firstName'])
            context = {
                'players': self.players,
                'name': request.POST['firstName'],
            }

            return render(request, 'polls/index.html', context)


    def get(self, request):
         if request.method == 'GET':
             print(request.GET.get('firstName'))
             context = {
                'players': self.players,
                #never printing name from get function
             }

             return render(request, 'polls/index.html', context)
