from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='start_quiz'),
    path('submit_answers/', views.submit_answers, name='submit_answers'),
    path('add_question/', views.add_question, name='add_question'),
    path('add_choice/', views.add_choice, name='add_choice'),
]
