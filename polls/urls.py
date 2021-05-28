from django.urls import path


from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('base', views.BaseView.as_view(), name='base'),
    ]

#urls to go to two different views
