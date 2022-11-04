from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.http import JsonResponse
from .models import HngSlackDetails

# class HngDetailsList(generics.ListAPIView):
#     serializer_class = serializers.HngSerializer
#     queryset = models.HngSlackDetails.objects.all()

class HngDetailsList(APIView):
    def post(self, request, *args, **kwargs):
        posted_data = self.request.data
        city = posted_data['city']
        return_data = [ 
            {'city': city}
        ]

        

        return Response(status = 200, data = return_data)
