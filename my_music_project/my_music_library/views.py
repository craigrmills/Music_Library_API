from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework import viewsets


class SongList(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
