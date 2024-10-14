from django.urls import path
from .views import (
    register,
    list_movies,
    get_collection,
    create_collection,
    update_collection,
    get_collection_details,
    delete_collection,
    request_count,
    reset_request_count,
    CustomTokenObtainPairView,
)

urlpatterns = [
   path('api/register/', register, name='register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/movies/', list_movies, name='list_movies'),  # Ensure this matches
    path('api/collection/', get_collection, name='get_collection'),
    path('api/collection/', create_collection, name='create_collection'),  # You might need to specify methods
    path('api/collection/<int:collection_uuid>/', update_collection, name='update_collection'),  # Update for collection
    path('api/collection/<int:collection_uuid>/', get_collection_details, name='get_collection_details'),
    path('api/collection/<int:collection_uuid>/', delete_collection, name='delete_collection'),
    path('api/request-count/', request_count, name='request_count'),  # Ensure this is correct
    path('api/request-count/reset/', reset_request_count, name='reset_request_count'),  # Ensure this is correct
]
