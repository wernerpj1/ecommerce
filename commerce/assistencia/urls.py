from django.urls import path, include
from assistencia import views

urlpatterns = [
     path('assistencia/', views.post_service)
]