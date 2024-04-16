from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Details
from .serializers import DetailsSerializer
from rest_framework import generics

# Create your views here.

class DetailsCreateAPIView(generics.ListCreateAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer