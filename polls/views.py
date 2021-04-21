from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.contrib.auth.models import User

from .models import NBATeam, NBAPlayer, Profile



def basketballPoints(request):
    return render(request, 'polls/points.html', {})

def basketballRebounds(request):
    return render(request, 'polls/rebounds.html', {})


class IndexView(View):
    players = NBAPlayer.objects.all()

    def get(self, request):  #should change to def post after changing everything else to post
    # use an if statement to detect data
    # always use post if there is data, and use get when there is not data
    # use if 'POST" in request/keys(); for an easy true or false
    # need to be able to deal with 4 branches
        #logged in
        #not logged in
        #incomming data
        #no data

        context = {
            'players': self.players,

        }
        print(context)
        print(request.GET)

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
