from django.shortcuts import render
from rest_framework import generics
from . import serializers, models

class HngDetailsList(generics.ListAPIView):
    serializer_class = serializers.HngSerializer
    queryset = models.HngSlackDetails.objects.all()
    
