from django.http import response
from rest_framework.views import APIView
from .serializers import ServiceOrderSerializer, SugestionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

@api_view(['POST'])

def post_service(request):

    
    serializer = ServiceOrderSerializer(data=request.data, many=True)
    try:
        if serializer.is_valid():

            return Response(print(serializer.data), status=status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        