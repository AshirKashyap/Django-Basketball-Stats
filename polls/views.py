from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.contrib.auth.models import User

from .models import NBATeam, NBAPlayer, Profile



class BasketballPoints(View):
    # The post and get methods automatically seperate the data accordingly\

    points = NBAPlayer.objects.all()

    # def post(self, request):
    #     return render(request, 'polls/points.html', {})

    def post(self, request):
        if request.method == 'POST':
            print(request.POST['totalPoints'])
            context = {
                'points': self.points,
                'point': request.POST['totalPoints'],
            }

            return render(request, 'polls/points.html', context)

    def get(self, request):
        return render(request, 'polls/points.html', {})


class BasketballRebounds(View):
    # The post and get methods automatically seperate the data accordingly
    def post(self, request):
        return render(request, 'polls/rebounds.html', {})

    def get(self, request):
        return render(request, 'polls/rebounds.html', {})


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
                'name': request.GET.get('firstName')
             }

             return render(request, 'polls/index.html', context)
