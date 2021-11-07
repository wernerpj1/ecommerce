from django.http import response
from rest_framework.views import APIView
from .serializers import ServiceOrderSerializer, SugestionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def post_service(request):    
    serializer = ServiceOrderSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def post_sugestion(request):    
    serializer = SugestionSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)