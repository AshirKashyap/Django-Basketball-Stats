from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.contrib.auth.models import User

from .models import NBATeam, NBAPlayer, Profile



class BasketballPoints(View):
    # The post and get methods automatically seperate the data accordingly\
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
