from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('points', views.basketballPoints.as_view(), name='bbpoints'),
    path('rebounds', views.basketballRebounds.as_view(), name='bbrebounds'),
]

#urls to go to two different views
