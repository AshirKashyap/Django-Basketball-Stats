from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.contrib.auth.models import User

from .models import NBATeam, NBAPlayer, Profile



class BasketballPoints(View):
    # The post and get methods automatically seperate the data accordingly
    def post(self, request):
        return render(request, 'polls/points.html', {})

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
            print(request.GET['firstName'])
            context = {
                'players': self.players,
                'name': request.GET['firstName'],
            }

        return render(request, 'polls/index.html', context)


    













#
# class index(View):
#     def get(self, request):
#         template = loader.get_template('polls/index.html')
#         context = {}
#         return HTTPResponse(template.render(context, request))
#
#
# class basketballPoints(View):
#     def get(self, request):
#         template = loader.get_template('polls/points.html')
#         context = {}
#         return HTTPResponse(template.render(context, request))
#
# class basketballRebounds(View):
#     def get(self, request):
#         template = loader.get_template('polls/rebounds.html')
#         context = {}
#         return HTTPResponse(template.render(context, request))


# Create your views here.


# from .models import Question
# # ...
# def index(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
