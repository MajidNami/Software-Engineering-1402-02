from django.urls import path

from .views import *


urlpatterns = [
    path('home/', homePage, name='home'),
    path('start-chat/', startChat, name='startChat'),
    path('get-history/', getHistory, name='getHistory')
]
