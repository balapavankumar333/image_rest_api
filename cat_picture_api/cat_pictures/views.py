from django.shortcuts import render

# Create your views here.



from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import CatPicture
from .serializers import CatPictureSerializer

class CatPictureListCreateAPIView(generics.ListCreateAPIView):
    queryset = CatPicture.objects.all()
    serializer_class = CatPictureSerializer

class CatPictureRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CatPicture.objects.all()
    serializer_class = CatPictureSerializer

