from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.http import JsonResponse
from .models import HngSlackDetails

# class HngDetailsList(generics.ListAPIView):
#     serializer_class = serializers.HngSerializer
#     queryset = models.HngSlackDetails.objects.all()

class HngDetailsList(APIView):
    def get(self, *args, **kwargs):
        data = {
            "slackUsername": "Aniche",
            "backend": True,
            "age": 28,
            "bio": "I am a python developer"
        } 

        return JsonResponse(data)
