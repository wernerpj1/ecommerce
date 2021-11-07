from usuarios import views
from django.urls import path



urlpatterns = [
    
    path('signup/', views.signup),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
   
]