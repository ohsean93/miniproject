from django.contrib import admin
from django.urls import path
from . import views

app_name = 'eithers'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),  # Question C
    path('<int:pk>/detail/', views.detail, name='detail'),  # Question R
    path('<int:pk>/<int:pick>/answers_create/', views.answers_create, name='answers_create'),  # Answer C
    path('<int:pk>/detail_answer/', views.detail_answer, name='detail_answer'),  # Answer R
    path('<int:pk>/answers_delete/', views.answers_delete, name='answers_delete'),  # Answer D
    path('random', views.random, name='random')
]

# index / new / detail / answers_create / answers_delete / random
