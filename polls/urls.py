from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('points', views.basketballPoints, name='bbpoints'),
    path('rebounds', views.basketballRebounds, name='bbrebounds'),
]

#urls to go to two different views
