from django.urls import path

from . import views
from django.views.generic import RedirectView

app_name = 'budget'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.Profile, name='profile'),
]
urlpatterns += [
    path('my', RedirectView.as_view(url='/budget/profile')),
]

