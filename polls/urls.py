from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('points', views.BasketballPoints.as_view(), name='bbpoints'),
    path('rebounds', views.BasketballRebounds.as_view(), name='bbrebounds'),
    path('login', views.Login.as_view(), name='bblogin')
]

#urls to go to three different views
