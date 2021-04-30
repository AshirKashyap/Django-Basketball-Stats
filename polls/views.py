from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import NBATeam, NBAPlayer, Profile

class Login(View):
    def post(self, request):
        if 'inputUsername' in request.POST.keys():
            # IF so, try to authentircate
            user = authenticate(username=request.POST['inputUsername'],
                password=request.POST['inputPassword'])
            if user is not None:
                # IF success, then use the login function so the session persists.
                login(request, user)
            else:
                pass
                # Message for failed login.
        # This tests if the form is the log *out* form
        elif 'logout' in request.POST.keys():
            # If so, don't need to check anything else, just kill the session.
            logout(request)
        # After we check the forms, set a flag for use in the template.
        if request.user.is_authenticated:
            loggedIn = True
        else:
            loggedIn = False
        # Find the template
        template = loader.get_template('posts/index.html')

        # The home page will show *all* posts for now.
        allPosts = Post.objects.order_by('-pubDate')
        # The Post model only contains the username, so we go and fetch the
        # first and last names from the User model and add that information.
        for post in allPosts:
            poster = post.userPosted
            post.firstName = poster.first_name
            post.lastName = poster.last_name
        # Now all the data is ready to pass to the template so set up the context.
        context = {
            'allPosts': allPosts,
            'loggedIn': loggedIn,
            'user': request.user,
            }
        # And go!
        return render(template.render(context, request))

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
