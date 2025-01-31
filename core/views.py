from django.shortcuts import render
from rest_framework import generics
from .models import Dreamer
from .serializer import DreamerSerializer

# Create your views here.

class DreamerList(generics.ListAPIView):
    queryset = Dreamer.objects.all()
    serializer_class = DreamerSerializer
