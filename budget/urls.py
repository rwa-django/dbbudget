from django.urls import path

from . import views

app_name = 'budget'
urlpatterns = [
    path('', views.index, name='index'),
]
