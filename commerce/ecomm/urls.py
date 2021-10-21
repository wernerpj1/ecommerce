from django.urls import path, include
from ecomm import views

urlpatterns = [
        path('frete/', views.buscarCep), 
        path('lista/', views.ProductList.as_view()),
        path('products/search/', views.search),
        path('products/categoria/<slug:category_slug>/', views.CategoryDetail.as_view()),
        path('marca/<slug:marca_slug>/', views.MarcaDetail.as_view()),
        path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]