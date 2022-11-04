from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from django.http import JsonResponse
from .models import HngSlackDetails
from rest_framework import status
from .serializers import ArithmeticSerializer

# class HngDetailsList(generics.ListAPIView):
#     serializer_class = serializers.HngSerializer
#     queryset = models.HngSlackDetails.objects.all()
@api_view(['POST', 'GET'])
def arithmeticApi(request):
    serializer = ArithmeticSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    operation_type = serializer.validated_data['operation_type']
    x = serializer.validated_data['x']
    y = serializer.validated_data['y']


    if operation_type == 'addition':
        result = x + y
    elif operation_type == 'subtraction':
        result = x-y
    else:
        result = x * y
    context = {
        "slackUsername": "Aniche",
        'operation_type': operation_type,
        'result': result
    }
    return Response(context, status=status.HTTP_200_OK)
