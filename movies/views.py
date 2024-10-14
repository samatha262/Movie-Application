from functools import cache
import requests
import os
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from movies.middleware import RequestCounterMiddleware  # Updated import

from .models import Collection
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

API_URL = "https://demo.credy.in/api/v1/maya/movies/"

def fetch_movies(page=1):
    response = requests.get(API_URL, auth=(os.getenv('API_USERNAME'), os.getenv('API_PASSWORD')))
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(username=username, password=password)
    refresh = RefreshToken.for_user(user)
    return Response({'access_token': str(refresh.access_token)}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_movies(request):
    movies = fetch_movies()
    return Response(movies, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_collection(request):
    collections = Collection.objects.filter(user=request.user)
    top_genres = ...  # Logic to find top 3 favorite genres
    data = {
        "collections": [{"title": col.title, "uuid": col.id, "description": col.description} for col in collections],
        "favourite_genres": top_genres,
    }
    return Response({"is_success": True, "data": data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_collection(request):
    collection = Collection.objects.create(user=request.user, **request.data)
    return Response({"collection_uuid": collection.id}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_collection(request, collection_uuid):
    try:
        collection = Collection.objects.get(id=collection_uuid, user=request.user)
        for attr, value in request.data.items():
            setattr(collection, attr, value)
        collection.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_collection_details(request, collection_uuid):
    try:
        collection = Collection.objects.get(id=collection_uuid, user=request.user)
        return Response({
            "title": collection.title,
            "description": collection.description,
            "movies": collection.movies
        }, status=status.HTTP_200_OK)
    except Collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_collection(request, collection_uuid):
    try:
        collection = Collection.objects.get(id=collection_uuid, user=request.user)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Collection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def request_count(request):
    count = RequestCounterMiddleware.get_request_count()
    return Response({"requests": count})

@api_view(['POST'])
def reset_request_count(request):
    RequestCounterMiddleware.reset_request_count()  # Resetting the request count
    return Response({"message": "Request count reset successfully"})

class CustomTokenObtainPairView(TokenObtainPairView):
    # You can customize the token response here if needed
    pass