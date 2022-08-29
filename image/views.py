from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Image_usSerializer
from .models import Image_u
class ImagesViewSet(viewsets.ModelViewSet):
    queryset=Image_u.objects.all().order_by('-id')
    serializer_class=Image_usSerializer
    
