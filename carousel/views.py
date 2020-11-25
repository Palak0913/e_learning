from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarouselSerializer
from .models import Carousel

# Create your views here.
class CarouselView(viewsets.ModelViewSet):
    serializer_class = CarouselSerializer
    queryset = Carousel.objects.all()