from django.urls import path, include
from . import views


urlpatterns = [
    path('music/', views.SongList.as_view()),
]