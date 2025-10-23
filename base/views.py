from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser,VideoFile
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import VideoFileSerializer

class VideoViewSet(viewsets.ViewSet):
    def create ()
